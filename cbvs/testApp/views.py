from typing import Any, Dict
from django.views.generic import View
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
class HelloWorldView(View):
    def get(self,request):
        return HttpResponse('<h1>This is the request from class based view </h1>')
    
class TemplateCBV(TemplateView):
    template_name = 'testApp/index.html'

class TemplateCBV2(TemplateView):
    template_name='testApp/result.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']="kunal"
        context['marks']=100
        return context
