# Generated by Django 3.1 on 2020-09-02 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('notification', '0001_initial'),
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweet.tweet'),
        ),
    ]
