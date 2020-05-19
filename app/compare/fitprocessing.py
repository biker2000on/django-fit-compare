import fitdecode
from collections import defaultdict
import pandas as pd
from .models import RideFile, Activity, Record, Device
from django.db import transaction
# import geopandas as gpd

def init_kwargs(model, arg_dict):
    model_fields = [f.name for f in model._meta.get_fields()]
    return {k: v for k, v in arg_dict.items() if k in model_fields}

def dict_from_fit(fitfile):
    file = defaultdict(list)
    fit = fitdecode.FitReader(fitfile)
    for frame in fit:
        if isinstance(frame, fitdecode.FitDataMessage):
            fields = {f.name: f.value for f in frame.fields}
            file[frame.name].append(fields)
    return file

# def gdf_from_fit(fitfile, messageType='record', keep_unknown=False):
#     file = dict_from_fit(fitfile)
#     df = pd.DataFrame(file[messageType])
    
#     for col in df.columns[df.columns.str.contains('position')]:
#         df[col] = df[col] / 10000000
    
#     df['geometry'] = df.apply(lambda x: (x['position_long'], x['position_lat']), axis=1)
    
#     if keep_unknown == False:
#         df = df.drop(df.columns[df.columns.str.contains('unknown')], axis=1)

#     ride = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df['position_long'], df['position_lat']))
    
#     return ride

def handle_uploaded_file(file):
    newride = RideFile(file=file)
    newride.save()
    fit = dict_from_fit(newride.file)

    kwargs = init_kwargs(Activity, fit['session'][0])
    newact = Activity(fitfile=newride, **kwargs)
    newact.activity_type = fit['file_id'][0]['type']
    newact.save()

    record_fields = [f.name for f in Record._meta.get_fields()]  

    df = pd.DataFrame(fit['record'])
    df.drop([col.replace('enhanced_','') for col in df.columns if 'enhanced' in col], axis=1, inplace=True)
    df.columns = df.columns.str.replace('enhanced_','')  
    df.loc[:,df.columns.str.contains('position')] = df.loc[:,df.columns.str.contains('position')]/10000000
    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)
    records = df[[col for col in df.columns if col in record_fields]]
    Record.objects.bulk_create(list(records.apply(lambda x: Record(activity=newact, **x), axis=1)))


    

