# Generated by Django 4.1 on 2022-08-19 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_alter_board_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='image',
            field=models.ImageField(blank=True, default='Images/favicon.png', null=True, upload_to='Images/', verbose_name='썸네일 이미지'),
        ),
    ]
