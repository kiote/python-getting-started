# Generated by Django 3.0.5 on 2020-04-27 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_message_raw_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='chat_id',
            field=models.CharField(default='', max_length=80, verbose_name='chat_id'),
        ),
    ]
