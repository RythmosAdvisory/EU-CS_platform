# Generated by Django 2.2.10 on 2020-03-27 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0030_auto_20200324_0512'),
    ]

    operations = [
        migrations.CreateModel(
            name='OriginDatabase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('originDatabase', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='originUID',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='originURL',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='originDatabase',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.OriginDatabase'),
        ),
    ]
