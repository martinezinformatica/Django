from django.contrib import admin
from aulas.models import Musician, Person, Album
# Register your models here.

admin.site.register(Person)
admin.site.register(Album)
admin.site.register(Musician)
