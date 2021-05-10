# Generated by Django 3.2.2 on 2021-05-10 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='publish',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AddField(
            model_name='blog',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(help_text='Enter text'),
        ),
    ]
