# Generated by Django 3.2.9 on 2021-12-11 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20211211_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp',
            name='Image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]