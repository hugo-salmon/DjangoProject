from django.shortcuts import render, redirect
from .models import CustomUser

def index(request):
    return render(request, 'inscription.html')

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if password != confirm_password:
            return render(request, 'inscription.html', {'error': 'Les mots de passe ne correspondent pas.'})

        if CustomUser.objects.filter(username=username).exists():
            return render(request, 'inscription.html', {'error': 'Ce nom d\'utilisateur est déjà pris.'})

        user = CustomUser.objects.create_user(username=username, email=email, password=password)
        user.save()
        print("Utilisateur enregistré avec succès:", user.username)
        return redirect('confirmation')  # Redirection vers la page de confirmation

    return render(request, 'inscription.html', {})

from django.shortcuts import render

def confirmation(request):
    return render(request, 'confirmation.html')
