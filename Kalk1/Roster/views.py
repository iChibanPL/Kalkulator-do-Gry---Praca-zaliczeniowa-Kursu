from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import CreateUserForm
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .utils import get_unit_form_for_army


""" Jest to funkcja rejestracji użytkownika"""


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Utworzono konto dla : ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'roster/register.html', context)


""" Jest to funkcja logowania użytkownika"""


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Nazwa użytkownika lub hasło są niepoprawne')

        context = {}
        return render(request, 'roster/login.html', context)

"""Jest to funkcja wylogowywania użytkownika"""

def logoutUser(request):
    logout(request)
    return redirect('login')


"""Funkcja do zliczania punktów jednostek"""


def calculate(request):
    testowe_ork = CustomUnitOrk.objects.first()
    testowe_ork.calculate_points()
    testowe_elf = CustomUnitElf.objects.first()
    testowe_elf.calculate_points()
    return render(request, 'roster/dashboard.html')


"""Funkcja przekierowująca na stronę główną"""


def home(request):
    return render(request, 'roster/dashboard.html')


"""Funkcja wyświetlania wszystkich utworzonych armii"""


@login_required(login_url='login')
def armies(request):

    armys = Army.objects.all()
    context = {'armys': armys}
    return render(request, 'roster/armies.html', context)


"""Funkcja tworzenie nowej armii"""


def createArmy(request):
    form = ArmyForm()
    if request.method == "POST":
        form = ArmyForm(request.POST)
        if form.is_valid():
            army = form.save()
            return redirect('army_edit', army.id)
    context = {'form': form}
    return render(request, 'roster/army_form.html', context)


"""Funkcja usuwająca całą wybraną armie"""


def deleteArmy(request, army_id):
    army = Army.objects.get(id=army_id)
    army.delete()
    return redirect('armies')


"""Funkcja tworzenia jednostki w danej armii 
(nazwa robocza nie była już poprawiana z braku czasu) 
działa dla Orków i Elfów"""


def createOrkUnit(request, army_id):

    army = Army.objects.get(id=army_id)

    if request.method == "POST":
        unit_form = get_unit_form_for_army(army, request_post=request.POST)

        if unit_form.is_valid():
            army_unit = unit_form.save()
            army_unit.army = army
            army_unit.save()
            army_unit.calculate_points()
            army.calculate_points()
            return redirect('army_edit', army_id)
    else:
        unit_form = get_unit_form_for_army(army)

        if army.army_type == 'Ork':
            existing_units = CustomUnitOrk.objects.filter(army=army)
        else:
            existing_units = CustomUnitElf.objects.filter(army=army)

        context = {
            'form': unit_form,
            'existing_units': existing_units,
            'army': army
        }
        return render(request, 'roster/army_form.html', context)



""""robimy kasowanie jednostki z armi"""

def deleteArmyUnit(request, unit_id, army_id):
    army = Army.objects.get(id=army_id)
    if army.army_type == 'Ork':
        existing_units = CustomUnitOrk.objects.get(id=unit_id)
        existing_units.delete()
        return redirect('army_edit', army_id)
    else:
        existing_units = CustomUnitElf.objects.get(id=unit_id)
        existing_units.delete()
        return redirect('army_edit', army_id)

# Create your views here.
