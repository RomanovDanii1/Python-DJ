# Generated by Django 4.1.4 on 2023-03-04 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
