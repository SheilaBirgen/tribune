# Generated by Django 3.0.3 on 2020-02-26 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_article'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Editor',
        ),
        migrations.DeleteModel(
            name='tags',
        ),
    ]
