# Generated by Django 4.1 on 2022-08-14 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rword', '0003_alter_rboard_s_contents_alter_rboard_sentence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rboard',
            name='word_tag',
        ),
        migrations.AddField(
            model_name='rboard',
            name='s_keyword',
            field=models.ManyToManyField(related_name='s_word', to='rword.wordlist'),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]