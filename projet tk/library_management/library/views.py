from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Livre, Membre

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'library/login.html', {'error': 'Invalid username or password'})
    return render(request, 'library/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    livres = Livre.objects.all()
    membres = Membre.objects.all()
    return render(request, 'library/home.html', {'livres': livres, 'membres': membres})

@login_required
def add_livre(request):
    if request.method == 'POST':
        titre = request.POST['titre']
        auteur = request.POST['auteur']
        quantite = request.POST['quantite']
        isbn = request.POST['isbn']
        Livre.objects.create(titre=titre, auteur=auteur, quantite=quantite, isbn=isbn)
        return redirect('home')
    return render(request, 'library/add_livre.html')

@login_required
def delete_livre(request, id):
    Livre.objects.get(id=id).delete()
    return redirect('home')

@login_required
def modify_livre(request, id):
    livre = get_object_or_404(Livre, id=id)
    if request.method == 'POST':
        livre.titre = request.POST['titre']
        livre.auteur = request.POST['auteur']
        livre.quantite = request.POST['quantite']
        livre.isbn = request.POST['isbn']
        livre.save()
        return redirect('home')
    return render(request, 'library/modify_livre.html', {'livre': livre})

@login_required
def add_member(request):
    if request.method == 'POST':
        nom = request.POST['first_name']
        prenom = request.POST['last_name']
        contact = request.POST['contact']
        Membre.objects.create(nom=nom, prenom=prenom, contact=contact)
        return redirect('home')
    return render(request, 'library/add_members.html')

@login_required
def delete_member(request, id):
    Membre.objects.get(id=id).delete()
    return redirect('home')

@login_required
def modify_member(request, id):
    membre = get_object_or_404(Membre, id=id)
    if request.method == 'POST':
        membre.nom = request.POST['first_name']
        membre.prenom = request.POST['last_name']
        membre.contact = request.POST['contact']
        membre.save()
        return redirect('home')
    return render(request, 'library/modify_member.html', {'membre': membre})