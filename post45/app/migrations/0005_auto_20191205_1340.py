# Generated by Django 2.1.8 on 2019-12-05 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20191205_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
