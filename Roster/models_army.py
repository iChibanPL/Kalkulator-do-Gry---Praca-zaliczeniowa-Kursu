from django.db import models

from .forms import OrkUnitForm, ElfUnitForm
from .models import CustomUnitOrk


"""Klasa armii wraz z funkcją do obliczania jej łącznej ilości punktów"""


class Army(models.Model):

    ARMY_TYPE_CHOICES = [
        ('Ork', 'Army of Orks'),
        ('Elf', 'Army of Elfs'),
    ]
    name = models.CharField(max_length=100)
    army_type = models.CharField(choices=ARMY_TYPE_CHOICES, max_length=3)
    total_points = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    def calculate_points(self):
        assigned_orks = CustomUnitOrk.objects.filter(army=self)
        new_total_points = 0
        for ork in assigned_orks:
            new_total_points = new_total_points + ork.total_points
        self.total_points = new_total_points
        self.save()

    def get_unit_form(self, request_post=None):
        if self.army_type == 'Ork':
            if request_post:
                form = OrkUnitForm(request_post)
            else:
                form = OrkUnitForm()
        else:
            if request_post:
                form = ElfUnitForm(request_post)
            else:
                form = ElfUnitForm()

        return form
