# Generated by Django 5.2 on 2025-05-13 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_publication'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('data_scientist', 'Data Scientist'), ('data_analyst', 'Data Analyst'), ('python_developer', 'Python Developer'), ('other', 'Otro')], default='other', max_length=20, verbose_name='Categoría'),
        ),
    ]
