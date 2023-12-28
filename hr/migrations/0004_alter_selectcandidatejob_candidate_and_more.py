# Generated by Django 4.2.4 on 2023-08-09 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0003_alter_selectcandidatejob_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectcandidatejob',
            name='candidate',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hr.candidateapplications'),
        ),
        migrations.AlterField(
            model_name='selectcandidatejob',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.jobpost'),
        ),
    ]
