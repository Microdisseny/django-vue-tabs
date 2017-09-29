from django.contrib import admin
from django_vue_tabs.admin import TabsMixin


from .models import (
    Choice, Question
)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    classes = ('inline-choices',)


class QuestionAdmin(TabsMixin, admin.ModelAdmin):
    fieldsets = [
        ('Text', {
            'fields': ['question_text'],
            'classes': ('fieldset-text',),
        }),
        ('Date information', {
            'fields': ['pub_date'],
            'classes': ('fieldset-text',),
        }),
    ]

    inlines = (ChoiceInline,)
    list_display = ('question_text', 'pub_date',)
    tabs = (
        ("Tab 1", ('fieldset-text',)),
        ('Tab 2', ('inline-choices',))
    )


admin.site.register(Question, QuestionAdmin)
