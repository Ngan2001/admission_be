# Generated by Django 4.1.6 on 2023-04-09 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0003_remove_department_introduction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='livestreamsnotification',
            name='title',
            field=models.TextField(null=True),
        ),
    ]
