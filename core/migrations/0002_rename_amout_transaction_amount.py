# Generated by Django 4.2.6 on 2023-10-21 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='amout',
            new_name='amount',
        ),
    ]