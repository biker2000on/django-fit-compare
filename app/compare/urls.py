from django.urls import path, include

from . import views

app_name = 'compare'
urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path('activity/<int:pk>', views.ActivityDetailView.as_view(), name='activity-detail'),
    path('activity/<int:pk>/data', views.json_ride, name='activity-data'),
    path("activity/data", views.json_rides, name="activities-data"), # expects query parameters for 'activities'
    path('activity/compare', views.compareView, name='compare'), # expects query parameters for 'activities'
    path("uploadfile", views.upload_file, name="upload"),
    path('accounts/signup', views.signup, name='signup'),
]