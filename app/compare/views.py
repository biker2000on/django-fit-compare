from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect, JsonResponse
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.utils import timezone
from .fitprocessing import handle_uploaded_file
from .forms import UploadFileForm
from .models import Activity

def image_upload(request):
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)
        return render(request, "upload.html", {
            "image_url": image_url
        })
    return render(request, "upload.html")

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
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

class IndexView(generic.ListView):
    template_name = 'index.html'
    model = Activity

class ActivityDetailView(generic.DetailView):
    template_name = 'activity_detail_uplot.html'
    model = Activity

def compareView(request):
    activities = request.GET.get('activities', None)
    if activities:
        activities = activities.split(',')

    return render(request, 'compare.html', {"activities": activities})