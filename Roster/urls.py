from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="dashboard"),
    path('armies/', views.armies, name="armies"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    # path('calculate/', views.calculate),

    path('create_army/', views.create_army, name="create_army"),
    path('army_edit/<int:army_id>', views.create_ork_unit, name="army_edit"),
    path('delete_army/<int:army_id>', views.delete_army, name="delete_army"),
    path('delete_unit/<int:army_id>/<int:unit_id>/', views.delete_army_unit, name="delete_unit")
]
