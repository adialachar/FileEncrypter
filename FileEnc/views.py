from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
# Create your views here.


def index(request):
	
	#t = loader.get_template('../templates/index.html')
	#c = None


	return render(request, 'FileEnc/index.html', context = {})
