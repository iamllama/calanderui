# Generated by Django 3.0.6 on 2020-05-12 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendarui', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dqdatafile',
            old_name='dq_datafile_id_pk',
            new_name='dq_datafile_id',
        ),
    ]