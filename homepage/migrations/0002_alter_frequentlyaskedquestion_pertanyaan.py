# Generated by Django 4.1 on 2022-10-26 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequentlyaskedquestion',
            name='pertanyaan',
            field=models.TextField(blank=True, null=True),
        ),
    ]