# Generated by Django 3.0.8 on 2020-09-10 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendrequest',
            name='from_user',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='friendrequest',
            name='to_user',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='friends',
            name='user1',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='friends',
            name='user2',
            field=models.CharField(max_length=150),
        ),
    ]