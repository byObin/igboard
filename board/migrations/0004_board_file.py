# Generated by Django 4.1 on 2022-08-08 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_alter_board_board_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='Files'),
        ),
    ]