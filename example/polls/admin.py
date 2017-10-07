from django.contrib import admin
from django_vue_tabs.admin import TabsMixin

from .models import (
    Choice, Question, Comment
)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    classes = ('inline-choices',)


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1
    classes = ('inline-comments',)


class QuestionAdmin(TabsMixin, admin.ModelAdmin):

    # change_form_template = 'django_vue_tabs/change_form.html'
    change_form_template = 'admin/polls/question/change_form.html'

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

    inlines = (ChoiceInline, CommentInline,)
    list_display = ('question_text', 'pub_date',)
    tabs = (
        ("Tab 1", ('fieldset-text',)),
        ('Tab 2', ('inline-choices',)),
        ('Tab 3', ('inline-comments',)),
    )


admin.site.register(Question, QuestionAdmin)
