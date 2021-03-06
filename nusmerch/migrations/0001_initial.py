# Generated by Django 3.0.6 on 2020-06-10 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Full Name')),
                ('number', models.IntegerField()),
                ('matric', models.CharField(help_text='AXXXXXXXB', max_length=10, verbose_name='Matric Number')),
                ('email', models.EmailField(max_length=200)),
                ('faculty', models.CharField(choices=[('FASS', 'Arts and Social Sciences'), ('BIZ', 'Business'), ('COM', 'Computing'), ('DEN', 'Dentistry'), ('SDE', 'Design and Environment'), ('ENG', 'Engineering'), ('LAW', 'Law'), ('MED', 'Medicine'), ('SCI', 'Science')], default='FASS', max_length=50)),
                ('campus_residential_type', models.CharField(choices=[('TH', 'Temasek Hall'), ('EH', 'Eusoff Hall'), ('SH', 'Sheares Hall'), ('RH', 'Raffles Hall'), ('KR', 'Kent Ridge Hall'), ('TEM', 'Tembusu'), ('RVRC', 'Ridge View Residences'), ('CAPT', 'College of Alice and Peter Tan'), ('USP', 'University Scholars Programme'), ('RC4', 'Residential COllege 4'), ('NIL', 'Do Not Stay On Campus')], default='NIL', max_length=100, verbose_name='Campus Residential Type')),
                ('password1', models.CharField(max_length=50)),
                ('password2', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='profile_image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
