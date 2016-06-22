from django.shortcuts import render
from website.models import Sport, Terrain
from website.forms import ContactForm

# Create your views here.

def home(request):
	terrain = Terrain.objects.all()
	sport = Sport.objects.all()
	return render(request,'website/home.html',{'terrain': terrain, 'sport': sport})

def sport(request, spt):
	sports = Sport.objects.all()
	terrain = Terrain.objects.filter(sport__nom = spt)
	return render(request, 'website/sport.html',{'terrain': terrain, 'sport': spt})



