# Generated by Django 4.1 on 2022-11-02 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0009_alter_userprofile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(default='media/person.png', upload_to='media'),
        ),
    ]
