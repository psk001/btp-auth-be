# Generated by Django 4.1.7 on 2023-02-18 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.IntegerField()),
                ('mobile', models.TextField(max_length=13)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
