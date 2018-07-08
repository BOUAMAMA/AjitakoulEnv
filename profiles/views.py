from django.shortcuts import render

# Create your views here.
def home(request):
	context = locals()
	template = 'home.html'
	return render(request, template, context)


def About(request):
	context = locals()
	template = 'About.html'
	return render(request, template, context)


def download(request):
	context = locals()
	template = 'download.html'
	return render(request, template, context)

