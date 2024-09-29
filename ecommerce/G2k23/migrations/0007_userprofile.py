# Generated by Django 4.2.5 on 2023-12-12 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('G2k23', '0006_rename_is_solid_item_is_sold'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('mobile_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
