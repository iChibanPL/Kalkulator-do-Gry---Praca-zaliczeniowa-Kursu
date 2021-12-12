from django.test import TestCase
# from django.db import models
from Roster.models import CustomUnitElf, Army, Armor, Weapon, ElfUnit, CustomUnitOrk, OrkUnit
import pytest


class TestCustomUnitElf(TestCase):

    @classmethod
    def setUpTestData(cls):
        Armor.objects.create(name='Helmet', point_value='5')
        Weapon.objects.create(name='Axe', point_value='5')
        ElfUnit.objects.create(name='Elf King', point_value='100')
        OrkUnit.objects.create(name='Ork Boy', point_value='10')
        OrkUnit.objects.create(name='Big Ork', point_value='20')
        # Army.objects.create(name='test_name', user='test_user', army_type='Ork')


    def test_calculate_points_elf(self):
        amount = 1
        armor = Armor.objects.get(id=1)
        weapon = Weapon.objects.get(id=1)
        elf = ElfUnit.objects.get(id=1)
        calc = CustomUnitElf(armor=armor, weapon=weapon, elf=elf, amount=amount)
        calc.calculate_points()
        assert calc.total_points == 110

    def test_calculate_points_ork(self):
        amount = 10
        armor = Armor.objects.get(id=1)
        weapon = Weapon.objects.get(id=1)
        ork = OrkUnit.objects.get(id=1)
        calc = CustomUnitOrk(armor=armor, weapon=weapon, ork=ork, amount=amount)
        calc.calculate_points()
        assert calc.total_points == 200

    # def test_army_calculate_points_ork(self):
    #     army = Army.objects.get(id=1)
    #     calc = Army(user=user, name=name, army_type=army_type)
    #     calc.calculate_points()






