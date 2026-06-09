from django.urls import path
from . import views

app_name = 'reclamations'

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('rechercher/', views.rechercher_reclamations, name='rechercher'),
    path('liste/', views.liste_reclamations, name='liste_reclamations'),
    path('nouvelle/', views.nouvelle_reclamation, name='nouvelle_reclamation'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/stats/', views.dashboard_stats, name='dashboard_stats'),
    path('changer-statut/', views.changer_statut, name='changer_statut'),
    path('supprimer/<str:reclamation_id>/', views.supprimer_reclamation, name='supprimer_reclamation'),
    path('detail/<str:reclamation_id>/', views.detail_reclamation, name='detail_reclamation'),
    path('export/excel/', views.export_excel, name='export_excel'),
    path('export/pdf/', views.export_pdf, name='export_pdf'),
    path('modifier/<str:reclamation_id>/', views.modifier_reclamation, name='modifier_reclamation'),
]