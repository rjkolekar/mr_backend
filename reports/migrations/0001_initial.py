# Generated by Django 5.0.3 on 2024-03-21 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('industry', models.CharField(max_length=100)),
                ('table_of_contents', models.TextField()),
                ('highlights', models.TextField()),
                ('methodology', models.TextField()),
                ('price', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
