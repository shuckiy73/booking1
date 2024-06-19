# Generated by Django 5.0.6 on 2024-06-19 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('checkin', models.DateField()),
                ('checkout', models.DateField()),
                ('guests', models.IntegerField()),
                ('result_data', models.JSONField()),
            ],
        ),
    ]