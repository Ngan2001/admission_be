# Generated by Django 4.1.6 on 2023-05-06 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0010_alter_frequentlyquestions_question_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livestreamscomment',
            name='livestreams_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admissions.livestreamsnotification'),
        ),
    ]
