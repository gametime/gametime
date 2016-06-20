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
	return render(request, 'website/sport.html',{'sport': sports, 'terrain': terrain})

def contact(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = ContactForm(request.POST)  # Nous reprenons les données

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides

            # Ici nous pouvons traiter les données du formulaire
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']
            envoyeur = form.cleaned_data['envoyeur']
            renvoi = form.cleaned_data['renvoi']

            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer

            envoi = True

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = ContactForm()  # Nous créons un formulaire vide

    return render(request, 'website/contact.html', locals())

