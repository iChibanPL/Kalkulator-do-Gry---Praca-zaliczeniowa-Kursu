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


def registerPage(request):

    """ Jest to funkcja rejestracji użytkownika"""

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


def loginPage(request):

    """ Jest to funkcja logowania użytkownika"""

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


def logoutUser(request):

    """Jest to funkcja wylogowywania użytkownika"""

    logout(request)
    return redirect('login')


def home(request):

    """Przekierowanie na strone główną """

    return render(request, 'roster/dashboard.html')


@login_required(login_url='login')
def armies(request):

    """Funkcja wyświetlania wszystkich utworzonych armii"""

    armys = Army.objects.filter(user=request.user)
    context = {'armys': armys}
    return render(request, 'roster/armies.html', context)


@login_required(login_url='login')
def create_army(request):

    """Funkcja tworzenie nowej armii"""

    form = ArmyForm()
    if request.method == "POST":
        form = ArmyForm(request.POST)
        if form.is_valid():
            army = form.save()
            army.user = request.user
            army.save()
            return redirect('army_edit', army.id)
    context = {'form': form}
    return render(request, 'roster/army_form.html', context)


@login_required(login_url='login')
def delete_army(request, army_id):

    """Funkcja usuwająca całą wybraną armie"""

    army = Army.objects.get(id=army_id)
    army.delete()
    return redirect('armies')


@login_required(login_url='login')
def create_ork_unit(request, army_id):

    """Funkcja tworzenia jednostki w danej armii
(nazwa robocza nie była już poprawiana z braku czasu)
działa dla Orków i Elfów"""

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


@login_required(login_url='login')
def delete_army_unit(request, army_id, unit_id):
    """
    Kasowanie jednostki z armi.
    """

    army = Army.objects.get(id=army_id)

    if army.army_type == 'Ork':
        existing_unit = CustomUnitOrk.objects.get(id=unit_id)
    else:
        existing_unit = CustomUnitElf.objects.get(id=unit_id)

    existing_unit.delete()
    army.calculate_points()

    return redirect('army_edit', army_id)







# """Funkcja do zliczania punktów jednostek"""
# def calculate(request):
#     testowe_ork = CustomUnitOrk.objects.first()
#     testowe_ork.calculate_points()
#     testowe_elf = CustomUnitElf.objects.first()
#     testowe_elf.calculate_points()
#     return render(request, 'roster/dashboard.html')
# Create your views here.
