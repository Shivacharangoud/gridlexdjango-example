from django.shortcuts import render
from django.views.generic.edit import UpdateView,DeleteView
from django.views.generic.base import RedirectView,View,TemplateView

from .models import GeeksModel

# Create your views here.
def home(request):
    data = GeeksModel.objects.all()
    return render(request,'editview_app/home.html',{'data':data})
class GeeksUpdateView(UpdateView):
    model = GeeksModel
    fields = ['title','description']
    success_url = '/'

class GeekDeleteView(DeleteView):
    model = GeeksModel
    success_url ='/'
    template_name = "editview_app/geeksmodel_confirm_delete.html"
