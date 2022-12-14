# Generated by Django 3.2.13 on 2022-05-03 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectovacantes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArchivoVacante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('archivo', models.FileField(upload_to='documents/')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proyectovacantes.categoria')),
                ('vacante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='proyectovacantes.vacante')),
            ],
        ),
    ]
