# Generated by Django 2.2.10 on 2020-03-04 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0014_resource_datepublished'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='about',
        ),
        migrations.AlterField(
            model_name='resource',
            name='abstract',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='resource',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
