# Generated by Django 3.2.13 on 2022-05-12 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_alter_empresa_web'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='web',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]