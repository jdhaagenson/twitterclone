# Generated by Django 3.1 on 2020-09-02 20:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitteruser',
            name='following',
            field=models.ManyToManyField(default='self', to=settings.AUTH_USER_MODEL),
        ),
    ]
