# Generated by Django 3.2.12 on 2022-10-27 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campos', '0003_campos_cidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campos',
            name='preco',
            field=models.IntegerField(),
        ),
    ]
