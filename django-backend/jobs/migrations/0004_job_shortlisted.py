# Generated by Django 5.0.1 on 2024-12-30 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_remove_job_similarity_rating_job_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='shortlisted',
            field=models.BooleanField(default=False),
        ),
    ]
