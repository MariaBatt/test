from django.contrib import admin

# Register your models here.
from maria_bs.models import Language, Vocabulary

admin.site.register(Language)
admin.site.register(Vocabulary)
