# Generated by Django 3.1.6 on 2021-02-18 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorys',
            name='image',
            field=models.ImageField(blank=True, default='test.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(blank=True, default='test.png', upload_to=''),
        ),
    ]
