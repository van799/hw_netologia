# Generated by Django 4.1.1 on 2022-09-09 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_rename_teachers_student_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teacher',
            new_name='teachers',
        ),
    ]
