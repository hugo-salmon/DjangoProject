from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Flight
from .models import Hebergement


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
            return render(request, 'existing_user.html')

        user = CustomUser.objects.create_user(username=username, email=email, password=password)
        user.save()
        print("Utilisateur enregistré avec succès:", user.username)
        return redirect('connexion')  

    return render(request, 'inscription.html', {})

    
def existing_user(request):
    """
    Affiche une page pour les utilisateurs existants.
    """
    return render(request, 'existing_user.html')

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
    flights_data = [
    {"departure": "Paris", "destination": "New York", "transport_type": "Avion", "departure_date": "2024-03-01", "return_date": "2024-03-10"},
    {"departure": "Lyon", "destination": "Nice", "transport_type": "Train", "departure_date": "2024-04-15", "return_date": "2024-04-25"},
    {"departure": "Sydney", "destination": "Paris", "transport_type": "Avion", "departure_date": "2024-05-20", "return_date": "2024-05-30"},
    {"departure": "Brest", "destination": "Paris", "transport_type": "Train", "departure_date": "2024-06-10", "return_date": "2024-06-20"},
    {"departure": "Tokyo", "destination": "Londres", "transport_type": "Avion", "departure_date": "2024-07-05", "return_date": "2024-07-15"},
    {"departure": "Marseille", "destination": "Strasbourg", "transport_type": "Train", "departure_date": "2024-08-18", "return_date": "2024-08-28"},
    {"departure": "Madrid", "destination": "Rome", "transport_type": "Avion", "departure_date": "2024-09-12", "return_date": "2024-09-22"},
    {"departure": "Toulon", "destination": "Bordeaux", "transport_type": "Train", "departure_date": "2024-10-03", "return_date": "2024-10-13"},
    {"departure": "Dubai", "destination": "New Delhi", "transport_type": "Avion", "departure_date": "2024-11-24", "return_date": "2024-12-04"},
    {"departure": "Lorient", "destination": "Toulouse", "transport_type": "Train", "departure_date": "2024-12-15", "return_date": "2025-01-02"},
]

    # Enregistrement des données dans la base de données
    for data in flights_data:
        if not Flight.objects.filter(departure=data["departure"], destination=data["destination"], transport_type=data["transport_type"], departure_date=data["departure_date"], return_date=data["return_date"]).exists():
            flight = Flight.objects.create(
                departure=data["departure"],
                destination=data["destination"],
                transport_type=data["transport_type"],
                departure_date=data["departure_date"],
                return_date=data["return_date"]
            )

    return render(request, 'flight_search.html')

def accommodation_reservation(request):
    """
    Affiche la page de réservation d'hébergement.
    """

    accommodation_data = [
    {"destination": "New York", "return_date": "2024-03-01", "departure_date": "2024-03-10", "number_of_guests": 2},
    {"destination": "Nice", "return_date": "2024-04-15", "departure_date": "2024-04-25", "number_of_guests": 1},
    {"destination": "Paris", "return_date": "2024-05-20", "departure_date": "2024-05-30", "number_of_guests": 5},
    {"destination": "Paris", "return_date": "2024-06-10", "departure_date": "2024-06-20", "number_of_guests": 2},
    {"destination": "Londres", "return_date": "2024-07-05", "departure_date": "2024-07-15", "number_of_guests": 4},
    {"destination": "Strasbourg", "return_date": "2024-08-18", "departure_date": "2024-08-28", "number_of_guests": 3},
    {"destination": "Rome", "return_date": "2024-09-12", "departure_date": "2024-09-22", "number_of_guests": 1},
    {"destination": "Bordeaux", "return_date": "2024-10-03", "departure_date": "2024-10-13", "number_of_guests": 2},
    {"destination": "New Delhi", "return_date": "2024-11-24", "departure_date": "2024-12-04", "number_of_guests": 5},
    {"destination": "Toulouse", "return_date": "2025-01-02", "departure_date": "2024-12-15", "number_of_guests": 4},
    ]

 

    # Enregistrement des données dans la base de données
    for data in accommodation_data:
        if not Hebergement.objects.filter(destination=data["destination"], return_date=data["return_date"], departure_date=data["departure_date"], number_of_guests=data["number_of_guests"]).exists():
            accommodation = Hebergement.objects.create(
                destination=data["destination"],
                return_date=data["return_date"],
                departure_date=data["departure_date"],
                number_of_guests=data["number_of_guests"]
            )
    return render(request, 'accommodation_reservation.html')

def travel_itinerary(request):
    """
    Affiche la page d'itinéraire de voyage'.
    """
    return render(request, 'travel_itinerary.html')

def travel_tips(request):
    """
    Affiche la page de conseils de voyage'.
    """
    return render(request, 'travel_tips.html')