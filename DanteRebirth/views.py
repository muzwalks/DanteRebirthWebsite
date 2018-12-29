from django.shortcuts import render

def index(request):
	return render(request,'DanteRebirth/index.html')

def band(request):
	return render(request, 'DanteRebirth/band.html')

def fans(request):
	return render(request, 'DanteRebirth/fans.html', {'fans': ['Send us an email to join the fan mailing list', 'danterebirth_fans@gmail.com']})

def gigs(request):
	return render(request, 'DanteRebirth/gigs.html')

def merchandise(request):
	return render(request, 'DanteRebirth/merchandise.html')





