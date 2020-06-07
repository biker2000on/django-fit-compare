from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect, JsonResponse
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.utils import timezone
from .fitprocessing import handle_uploaded_file
from .forms import UploadFileForm
from .models import Activity, ActivityGroup

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        files = request.FILES.getlist('files')
        if form.is_valid():
            for f in files:
                handle_uploaded_file(f)
            return HttpResponseRedirect(reverse('compare:upload'))
    else:
        form = UploadFileForm()
    return render(request, 'upload_new.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('compare:index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def json_ride(request, pk):
    records = Activity.objects.get(id=pk).record_set.all().values()
    return JsonResponse(list(records), safe=False)

def json_rides(request):
    activities = request.GET.get('activities', None)
    acts = []
    if activities:
        for act in activities.split(','):
            acts.append(list(Activity.objects.get(id=act).record_set.all().values()))
    return JsonResponse(acts, safe=False)

def group_rides(request, pk):
    activities = list(ActivityGroup.objects.get(id=pk).activity.all().values_list('id', flat=True))
    acts = []
    if activities:
        for act in activities:
            acts.append(list(Activity.objects.get(id=act).record_set.all().values()))
    return JsonResponse(acts, safe=False)

def set_group(request):
    if request.method == 'POST':
        activities = list(request.POST.keys())
        activities = activities[1:len(activities)-1]
        name = request.POST['name']
        group = ActivityGroup(name=name)
        group.save()
        group.activity.add(*activities)
        # for act in activities:
        #     group.acti.add(act)
        # print(request)
    return HttpResponseRedirect(reverse('compare:index'))


class IndexView(generic.ListView):
    template_name = 'index.html'
    model = Activity

class ActivityDetailView(generic.DetailView):
    template_name = 'activity_detail_uplot.html'
    model = Activity

class GroupView(generic.ListView):
    template_name = 'groups.html'
    model = ActivityGroup

def compareView(request, pk):
    # activities = request.GET.get('activities', None)
    group = ActivityGroup.objects.get(id=pk)
    activities = list(group.activity.all().values_list('id', flat=True))
    # if activities:
    #     activities = activities.split(',')

    return render(request, 'compare.html', {"activities": activities, "group": group})