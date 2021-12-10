from django.contrib.auth.models import User
from django.db import models




class Army(models.Model):

    """Klasa armii wraz z funkcją do obliczania jej łącznej ilości punktów"""

    ARMY_TYPE_CHOICES = [
        ('Ork', 'Army of Orks'),
        ('Elf', 'Army of Elfs'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    army_type = models.CharField(choices=ARMY_TYPE_CHOICES, max_length=3)
    total_points = models.PositiveSmallIntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.name

"""Obliczanie łączniej ilości punktów"""
    def calculate_points(self):
        assigned_orks = CustomUnitOrk.objects.filter(army=self)
        assigned_elf = CustomUnitElf.objects.filter(army=self)
        new_total_points = 0
        for ork in assigned_orks:
            new_total_points = new_total_points + ork.total_points
        for elf in assigned_elf:
            new_total_points = new_total_points + elf.total_points
        self.total_points = new_total_points
        self.save()


class Weapon(models.Model):

    """Klasa broni które mogą wykożystywać jednostki"""

    name = models.CharField(max_length=100)
    point_value = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Armor(models.Model):

    """Klasa panceża który mogą wykożystywać jednostki"""

    name = models.CharField(max_length=100)
    point_value = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class ElfUnit(models.Model):

    """Klasa Jednostek z armii Elfów"""

    name = models.CharField(max_length=100)
    point_value = models.PositiveSmallIntegerField()
    weapons = models.ManyToManyField(Weapon, blank=True)
    armor = models.ManyToManyField(Armor, blank=True)

    def __str__(self):
        return self.name


class OrkUnit(models.Model):

    """Klasa Jednostek z armii Orków"""

    name = models.CharField(max_length=100)
    point_value = models.PositiveSmallIntegerField()
    weapons = models.ManyToManyField(Weapon, blank=True)
    armor = models.ManyToManyField(Armor, blank=True)

    def __str__(self):
        return self.name


class CustomUnitOrk(models.Model):

    """Klasa szczegółowego doboru jednostki z armii Orków,
     wraz z funkcją obliczania wartości punktowej utworzonej jednostki"""

    ork = models.ForeignKey(OrkUnit, on_delete=models.CASCADE)
    armor = models.ForeignKey(Armor, on_delete=models.CASCADE)
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    army = models.ForeignKey(Army, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.PositiveSmallIntegerField()
    total_points = models.PositiveSmallIntegerField(blank=True, null=True)


    def calculate_points(self):
        points = (self.ork.point_value+self.armor.point_value+self.weapon.point_value)*self.amount
        self.total_points = points
        self.save()

    def __str__(self):
        return f'{self.ork}, {self.army}'


class CustomUnitElf(models.Model):

    """Klasa szczegółowego doboru jednostki z armii Elfów,
     wraz z funkcją obliczania wartości punktowej utworzonej jednostki"""

    elf = models.ForeignKey(ElfUnit, on_delete=models.CASCADE)
    armor = models.ForeignKey(Armor, on_delete=models.CASCADE)
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    army = models.ForeignKey(Army, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.PositiveSmallIntegerField()
    total_points = models.PositiveSmallIntegerField(blank=True, null=True)

    def calculate_points(self):
        points = (self.elf.point_value+self.armor.point_value+self.weapon.point_value)*self.amount
        self.total_points = points
        self.save()

    def __str__(self):
        return f'{self.elf}, {self.army}'
