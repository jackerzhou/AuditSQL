# Generated by Django 2.0.2 on 2018-02-02 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='avatar_file',
            field=models.ImageField(default='img/default/avatar1.png', upload_to='imgs/%Y/%m/%d/', verbose_name='用户头像'),
        ),
    ]
