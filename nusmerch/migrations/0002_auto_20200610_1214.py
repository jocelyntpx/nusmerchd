# Generated by Django 3.0.6 on 2020-06-10 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nusmerch', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='last_name',
            field=models.CharField(default=1, max_length=200, verbose_name='Full Name'),
            preserve_default=False,
        ),
    ]
