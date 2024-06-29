from django.contrib import admin
from .models import Post, Document, Ressource

# Enregistrer chaque modèle dans le site d'administration
admin.site.register(Post)
admin.site.register(Document)
admin.site.register(Ressource)