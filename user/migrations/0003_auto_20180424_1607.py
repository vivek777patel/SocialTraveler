# Generated by Django 2.0.2 on 2018-04-24 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180424_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfriends',
            name='updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='userfriends',
            name='are_friends_with',
            field=models.BooleanField(default=False),
        ),
    ]
