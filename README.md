# Django Tabs


## Usage


Add **django\_vue\_tabs** to **INSTALLED\_APPS**

Add **TabsMixin** in your **ModelAdmin**

```python
from django_vue_tabs.admin import TabsMixin

class QuestionAdmin(TabsMixin, admin.ModelAdmin):
```

Define fieldsets classes

```python
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
```

Define Innline classes

```python
class ChoiceInline(admin.TabularInline):
    ...
    classes = ('inline-choices',)
```

Set tabs array in your ModelAdmin

```python
class QuestionAdmin(TabsMixin, admin.ModelAdmin):
    ...

    tabs = (
        ("Tab 1", ('fieldset-text',)),
        ('Tab 2', ('inline-choices',))
    )
```

Example image:

![](example.png?raw=true)

## Credits

- Alexandre Busquets Triola - MICRODISSENY GISCUBE SL

This package uses **Spatie bvba** [vue-tabs-component](https://github.com/spatie/vue-tabs-component).


## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.
