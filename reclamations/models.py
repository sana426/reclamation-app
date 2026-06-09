from django.db import models
from django.contrib.auth.models import User

class Reclamation(models.Model):
    # Types de statut
    STATUT_CHOICES = [
        ('en_attente', '⏳ En attente'),
        ('en_cours', '🔧 En cours'),
        ('resolue', '✅ Cloturée'),
    ]
    
    # Types d'urgence
    URGENCE_CHOICES = [
        ('faible', ' Faible'),
        ('moyen', ' Modéré'),
        ('urgent', ' Urgent'),
    ]
    
    # Types de problème
    TYPE_PROBLEME = [
        ('fuite', ' Fuite d\'eau'),
        ('pression', ' Basse pression'),
        ('coupure', ' Coupure d\'eau'),
        ('qualite', ' Qualité de l\'eau'),
        ('facturation', ' Facturation'),
        ('autre', ' Autre'),
    ]
    
    # Agences
    AGENCE_CHOICES = [
        ('Azilal', 'Azilal'),
        ('Afourer', 'Afourer'),
        ('Bzou', 'Bzou'),
        ('Demnate', 'Demnate'),
        ('Ait Attab', 'Ait Attab'),
        ('Tanante', 'Tanante'),
        ('Ouaouizeghth', 'Ouaouizeghth'),
    ]
    SERVICE_CHOICES = [
        ('eau', ' Eau'),
        ('electricite', ' Électricité'),
        ('assainissement', ' Assainissement'),
    ]
    
    # Champs
    id = models.CharField(max_length=20, primary_key=True)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=100, blank=True, null=True) 
    cin = models.CharField(max_length=10, blank=True, null=True)  # Optionnel
    telephone = models.CharField(max_length=15, blank=True, null=True)  # Optionnel
    email = models.EmailField(blank=True, null=True)
    agence = models.CharField(max_length=50, choices=AGENCE_CHOICES)
    type_probleme = models.CharField(max_length=50, choices=TYPE_PROBLEME)
    urgence = models.CharField(max_length=10, choices=URGENCE_CHOICES, default='faible')
    adresse = models.TextField(blank=True, null=True)
    description = models.TextField()
    date_creation = models.DateField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    date_cloture = models.DateField(blank=True, null=True)
    numero_contrat = models.CharField(max_length=50, blank=True, null=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default='eau')
    
    # Relation avec l'utilisateur
    cree_par = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.id} - {self.nom}"
    
    class Meta:
        ordering = ['-date_creation']