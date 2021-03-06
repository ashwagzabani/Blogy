# Generated by Django 3.1.6 on 2021-02-18 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210218_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorys',
            name='descreption',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='categorys',
            name='image',
            field=models.ImageField(blank=True, default='category_img/category.png', upload_to='category_img/'),
        ),
        migrations.AlterField(
            model_name='likes',
            name='likes_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='about_me',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='position',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
