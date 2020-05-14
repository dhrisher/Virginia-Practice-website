from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.core.mail import send_mail
from django.conf import settings
from. import models

# Create your views here.
def home(request):
    return render(request,'home.html')

class ContactView(TemplateView):
    template_name = "contact.html"

class OwnerListView(ListView):
    model = models.Owner
    template_name = 'owner_list.html'

class ArtworkListView(ListView):
    model = models.Artwork
    template_name = 'Artwork_list.html'

class OwnerDetailView(DetailView):
    context_object_name = 'owner_detail'
    model = models.Owner
    template_name = 'owner_detail.html'

class ArtworkDetailView(DetailView):
    context_object_name = 'artwork_detail'
    model = models.Artwork
    template_name = 'artwork_detail.html'

class OwnerCreateView(CreateView):
    model = models.Owner
    fields = ('name','nationality','age')
    template_name = 'owner_form.html'
