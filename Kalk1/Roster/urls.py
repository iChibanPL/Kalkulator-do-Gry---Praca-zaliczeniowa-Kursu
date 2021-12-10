from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="dashboard"),
    path('armies/', views.armies, name="armies"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('calculate/', views.calculate),

    path('create_army/', views.createArmy, name="create_army"),
    path('army_edit/<int:army_id>', views.createOrkUnit, name="army_edit"),
    path('delete_army/<int:army_id>', views.deleteArmy, name="delete_army"),
    path('delete_unit/<int:army_id>', views.deleteArmyUnit, name="delete_unit")

]