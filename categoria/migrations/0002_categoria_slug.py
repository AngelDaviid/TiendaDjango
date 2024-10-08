# Generated by Django 5.1.1 on 2024-09-15 20:52

from django.db import migrations, models
from django.db import migrations
from django.utils.text import slugify

def populate_slug(apps, schema_editor):
    Categoria = apps.get_model('categoria', 'Categoria')
    for categoria in Categoria.objects.all():
        categoria.slug = slugify(f'{categoria.nombre}-{categoria.id}')
        categoria.save()

class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='slug',
            field=models.SlugField(unique=True, blank=True),
        ),
        migrations.RunPython(populate_slug),
    ]
