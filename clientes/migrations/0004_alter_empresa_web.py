# Generated by Django 3.2.13 on 2022-05-12 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_empresa_web'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='web',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
