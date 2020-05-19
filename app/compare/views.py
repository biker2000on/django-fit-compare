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
            return redirect('ltltlt:index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def json_ride(request, pk):
    records = Activity.objects.get(id=pk).record_set.all().values()
    return JsonResponse(list(records), safe=False)

class IndexView(generic.ListView):
    template_name = 'index.html'
    model = Activity
    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return .objects.filter(user=self.request.user) 

class ActivityDetailView(generic.DetailView):
    template_name = 'activity_detail_uplot.html'
    model = Activity
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     prices = Item.objects.get(id=self.kwargs['pk']).price_set.all().values()
    #     context['prices'] = list(prices)
    #     return context

class ActivityDetailUplotView(generic.DetailView):
    template_name = 'activity_detail_uplot.html'
    model = Activity