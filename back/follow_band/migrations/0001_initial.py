# Generated by Django 3.2.24 on 2024-02-17 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('band', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow_band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='band.band')),
            ],
        ),
    ]
