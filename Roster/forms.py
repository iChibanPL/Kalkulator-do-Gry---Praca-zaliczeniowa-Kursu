from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Army, CustomUnitOrk, ElfUnit, CustomUnitElf
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
"""Formularz tworzenia Usera"""
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ArmyForm(ModelForm):
"""Formularz tworzenia Armii"""
    class Meta:
        model = Army
        exclude = ['total_points', 'user']


class OrkUnitForm(ModelForm):
"""Formularz tworzenia jednostki Orków"""
    class Meta:
        model = CustomUnitOrk
        exclude = ['army', 'total_points']


class ElfUnitForm(ModelForm):
"""Formularz tworzenia jednostki Elfów"""
    class Meta:
        model = CustomUnitElf
        exclude = ['army', 'total_points']
