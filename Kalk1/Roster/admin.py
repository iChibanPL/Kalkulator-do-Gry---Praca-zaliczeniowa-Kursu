from django.contrib import admin

# Register your models here.

from .models import Weapon, Armor, OrksUnit, ElfUnit, Army, CustomUnitOrk, CustomUnitElf

admin.site.register(Weapon)
admin.site.register(Armor)
admin.site.register(OrksUnit)
admin.site.register(ElfUnit)
admin.site.register(Army)
admin.site.register(CustomUnitOrk)
admin.site.register(CustomUnitElf)



