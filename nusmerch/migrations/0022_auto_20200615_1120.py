# Generated by Django 3.0.6 on 2020-06-15 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nusmerch', '0021_product_filter'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='filter_campus',
            field=models.CharField(choices=[('TH', 'Temasek Hall'), ('EH', 'Eusoff Hall'), ('SH', 'Sheares Hall'), ('RH', 'Raffles Hall'), ('KR', 'Kent Ridge Hall'), ('TEM', 'Tembusu'), ('RVRC', 'Ridge View Residences'), ('CAPT', 'College of Alice and Peter Tan'), ('USP', 'University Scholars Programme'), ('RC4', 'Residential College 4'), ('NIL', 'Do Not Stay On Campus')], max_length=200, null=True, verbose_name='Filter(Faculty)'),
        ),
        migrations.AddField(
            model_name='product',
            name='filter_email',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='filter_faculty',
            field=models.CharField(choices=[('FASS', 'Arts and Social Sciences'), ('BIZ', 'Business'), ('COM', 'Computing'), ('DEN', 'Dentistry'), ('SDE', 'Design and Environment'), ('ENG', 'Engineering'), ('LAW', 'Law'), ('MED', 'Medicine'), ('SCI', 'Science')], max_length=200, null=True, verbose_name='Filter(Faculty)'),
        ),
        migrations.AddField(
            model_name='product',
            name='filter_matric',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='filter',
            field=models.CharField(choices=[('NIL', 'NIL'), ('Faculty', 'Faculty'), ('Matric', 'Matric'), ('Email', 'Email'), ('Campus Residential', 'Campus Residential')], default='NIL', max_length=200, null=True, verbose_name='Filter Type'),
        ),
    ]
