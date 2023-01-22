# Generated by Django 4.1.5 on 2023-01-21 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='genero',
            field=models.CharField(choices=[('M', 'Másculino'), ('F', 'Femenino'), ('O', 'Otros')], max_length=1),
        ),
    ]
