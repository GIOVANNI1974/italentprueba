# Generated by Django 3.2.13 on 2022-05-03 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectovacantes', '0003_auto_20220503_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivovacante',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proyectovacantes.categoria'),
        ),
        migrations.AlterField(
            model_name='archivovacante',
            name='vacante',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
