# Generated by Django 4.2.1 on 2023-05-14 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lineup', '0006_remove_acttechrider_setup_name_acttechrider_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acttechrider',
            name='name',
        ),
    ]
