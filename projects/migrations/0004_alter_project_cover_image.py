# Generated by Django 3.2.5 on 2021-07-17 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='cover_image',
            field=models.ImageField(blank=True, default='cover_images/default.jpeg', null=True, upload_to='cover_images/'),
        ),
    ]
