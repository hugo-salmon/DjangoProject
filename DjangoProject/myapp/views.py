from django.shortcuts import render, redirect
from .models import CustomUser
from django.http import HttpResponseNotFound
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register_user(request):
    """
    Permet à un utilisateur de s'inscrire.
    """
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if password != confirm_password:
            return render(request, 'inscription.html', {'error': 'Les mots de passe ne correspondent pas.'})

        if CustomUser.objects.filter(username=username).exists():
            return render(request, 'existing_url.html')

        user = CustomUser.objects.create_user(username=username, email=email, password=password)
        user.save()
        print("Utilisateur enregistré avec succès:", user.username)
        return redirect('connexion')  

    return render(request, 'inscription.html', {})

    
def existing_user(request):
    """
    Affiche une page pour les utilisateurs existants.
    """
    return render(request, 'existing_url.html')

def login_user(request):
    """
    Permet à un utilisateur de se connecter.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Veuillez remplir tous les champs')
            return render(request, 'connexion.html')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('base')  
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect')
            return render(request, 'connexion.html')  

    return render(request, 'connexion.html')

@login_required
def base(request):
    """
    Affiche la page de base pour les utilisateurs connectés.
    """
    return render(request, 'base.html')

def logout_view(request):
    """
    Permet à un utilisateur de se déconnecter.
    """
    logout(request)
    return redirect('connexion')

def flight_search(request):
    """
    Affiche la page de recherche de vols.
    """
    return render(request, 'flight_search.html')

def accommodation_reservation(request):
    """
    Affiche la page de réservation d'hébergement.
    """
    return render(request, 'accommodation_reservation.html')
