# Generated by Django 3.2.24 on 2024-02-17 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('like', '0001_initial'),
        ('publication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='publication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publication.publication'),
        ),
    ]