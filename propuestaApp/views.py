from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

from propuestaApp.models import Aspirante
# Create your views here.

class HomeView(View):
    template_name = "propuestaApp/home.html"
    def get(self,request):
    
        return render(request,self.template_name)

class SobreMiView(View):
    template_name = 'propuestaApp/sobremi.html'

    def get(self,request):
        aspirante = get_object_or_404(Aspirante, pk = 1)
        skills = aspirante.habilidad_set.all()
        ctx = {'aspirante': aspirante,"skills":skills}    
        return render(request,self.template_name,ctx)

class PropuestaValorView(View):
    template_name = 'propuestaApp/propuestavalor.html'
    def get(self,request):
       
        return render(request,self.template_name)



