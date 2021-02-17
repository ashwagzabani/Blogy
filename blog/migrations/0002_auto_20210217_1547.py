# Generated by Django 3.1.6 on 2021-02-17 12:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.CharField(max_length=255)),
                ('about_me', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='comment',
        ),
        migrations.AddField(
            model_name='post',
            name='isPublish',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
