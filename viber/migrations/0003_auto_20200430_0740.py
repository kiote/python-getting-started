# Generated by Django 3.0.5 on 2020-04-30 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viber', '0002_auto_20200430_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created',
            field=models.IntegerField(default=0),
        ),
    ]
