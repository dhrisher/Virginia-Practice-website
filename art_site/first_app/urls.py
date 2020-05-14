from django.urls import path
from . import views
from first_app.views import ContactView,OwnerListView,OwnerDetailView

app_name = 'first_app'

urlpatterns = [
    path('contact/',views.ContactView.as_view(), name='contact'),
    path('owners/',views.OwnerListView.as_view(), name = 'owners'),
    path('artwork/',views.ArtworkListView.as_view(), name = 'artwork_list'),
    path('artwork/<int:pk>/',views.ArtworkDetailView.as_view(), name = 'artwork_detail'),
    path('owners/<int:pk>/',views.OwnerDetailView.as_view(),name='detail'),
    path('create/',views.OwnerCreateView.as_view(), name = 'create'),



]
