# Generated by Django 5.0.4 on 2024-06-15 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='name',
            field=models.CharField(default='Unknown', max_length=100),
            preserve_default=False,
        ),
    ]