# Generated by Django 4.2.3 on 2023-08-02 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0004_technology_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='technology',
            options={'ordering': ['name'], 'verbose_name_plural': 'Technologies'},
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]