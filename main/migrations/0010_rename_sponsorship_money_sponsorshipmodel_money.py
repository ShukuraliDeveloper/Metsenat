# Generated by Django 4.0 on 2022-02-25 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_studentmodel_student_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsorshipmodel',
            old_name='sponsorship_money',
            new_name='money',
        ),
    ]
