# Generated by Django 4.2.16 on 2024-10-17 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='directions',
            field=models.CharField(default='TBA', help_text='Enter the directions for your recipe', max_length=1500),
        ),
        migrations.AddField(
            model_name='recipe',
            name='pic',
            field=models.ImageField(default='no_picture.jpg', upload_to='recipes'),
        ),
    ]
