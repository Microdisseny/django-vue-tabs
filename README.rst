Django Tabs
===========


Usage
-----

Add ''django_tabs'' to INSTALLED_APPS


Add TabsMixin in your ModelAdmin

.. code::

    class QuestionAdmin(TabsMixin, admin.ModelAdmin):


Define fieldsets classes

.. code::

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

Define Innline classes

.. code::

    class ChoiceInline(admin.TabularInline):
        ...
        classes = ('inline-choices',)


Set tabs array in your ModelAdmin

.. code::

    class QuestionAdmin(TabsMixin, admin.ModelAdmin):
        ...

        tabs = (
            ("Tab 1", ('fieldset-text',)),
            ('Tab 2', ('inline-choices',))
        )


Example image:

.. figure:: example.png?raw=true
   :alt: Example image
