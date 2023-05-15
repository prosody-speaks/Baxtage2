# Generated by Django 4.2.1 on 2023-05-14 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineup', '0005_alter_performance_tech_spec'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acttechrider',
            name='setup_name',
        ),
        migrations.AddField(
            model_name='acttechrider',
            name='name',
            field=models.CharField(default='hgf', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='acttechrider',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]