# Generated by Django 4.2.2 on 2024-06-21 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntlcargo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
