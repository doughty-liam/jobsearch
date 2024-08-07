# Generated by Django 5.0 on 2024-07-24 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=10000)),
                ('date_added', models.DateField()),
                ('applied', models.BooleanField()),
                ('similarity_rating', models.FloatField()),
            ],
        ),
    ]
