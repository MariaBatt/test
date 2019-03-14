from django.contrib import admin

# Register your models here.
from learning_foreign_languages.models import Language, Vocabulary

admin.site.register(Language)
admin.site.register(Vocabulary)
