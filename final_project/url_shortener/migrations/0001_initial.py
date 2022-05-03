# Generated by Django 4.0.3 on 2022-05-03 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashed_url', models.CharField(max_length=10)),
                ('full_url', models.URLField()),
                ('number_of_uses', models.PositiveIntegerField()),
            ],
        ),
    ]