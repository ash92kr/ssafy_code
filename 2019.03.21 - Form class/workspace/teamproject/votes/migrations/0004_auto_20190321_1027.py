# Generated by Django 2.1.7 on 2019-03-21 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0003_auto_20190321_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='image',
        ),
        migrations.AddField(
            model_name='question',
            name='image_a',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='question',
            name='image_b',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
