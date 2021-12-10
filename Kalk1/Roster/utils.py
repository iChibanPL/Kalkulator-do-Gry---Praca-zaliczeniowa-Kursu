from .forms import OrkUnitForm, ElfUnitForm


def get_unit_form_for_army(army, request_post=None):
    if army.army_type == 'Ork':
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
