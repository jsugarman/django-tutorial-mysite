from django.contrib import admin

# Register your models here.
from .models import Question
# from .models import Choice

# admin.site.register(Question)
# admin.site.register(Choice)

class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [
      (None,               {'fields': ['question_text']}),
      ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
  ]

admin.site.register(Question, QuestionAdmin)
