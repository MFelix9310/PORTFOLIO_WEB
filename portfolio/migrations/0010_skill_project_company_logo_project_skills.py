# Generated by Django 5.2 on 2025-05-13 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_certification_credential_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('name_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre (English)')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('order', models.IntegerField(default=0, verbose_name='Orden')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades',
                'ordering': ['order', 'name'],
            },
        ),
        migrations.AddField(
            model_name='project',
            name='company_logo',
            field=models.ImageField(blank=True, null=True, upload_to='companies/', verbose_name='Logo de la empresa'),
        ),
        migrations.AddField(
            model_name='project',
            name='skills',
            field=models.ManyToManyField(blank=True, related_name='projects', to='portfolio.skill', verbose_name='Habilidades'),
        ),
    ]
