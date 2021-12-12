from django.test import TestCase
import pytest
from django.test import RequestFactory
from django.urls import reverse, resolve

from mixer.backend.django import mixer


def test_to_fail():
    assert True


def test_to_be_ok():
    assert 2 + 2 == 4


class TestUrls:

    def test_detail_url(self):
        path = reverse('dashboard')
        assert resolve(path).view_name == 'dashboard'

    def test_detail_url2(self):
        path = reverse('armies')
        assert resolve(path).view_name == 'armies'

    def test_detail_url3(self):
        path = reverse('register')
        assert resolve(path).view_name == 'register'

    def test_detail_url4(self):
        path = reverse('login')
        assert resolve(path).view_name == 'login'

    def test_detail_url5(self):
        path = reverse('logout')
        assert resolve(path).view_name == 'logout'

    def test_detail_url6(self):
        path = reverse('create_army')
        assert resolve(path).view_name == 'create_army'

    def test_detail_url7(self):
        path = reverse('army_edit', kwargs={'army_id': 1})
        assert resolve(path).view_name == 'army_edit'

    def test_detail_url8(self):
        path = reverse('delete_army', kwargs={'army_id': 1})
        assert resolve(path).view_name == 'delete_army'

    def test_detail_url9(self):
        path = reverse('delete_unit', kwargs={'army_id': 1, 'unit_id': 1})
        assert resolve(path).view_name == 'delete_unit'



# class TestViews:
#
#     def test_army_detail_authenticated(self):
#         path = reverse('armies')
#         request = RequestFactory().get(path)
#         request.user = mixer.blend('User')
#
#         response = armies(request, id)
#         assert response.Army.bojects(id)



# Create your tests here.
