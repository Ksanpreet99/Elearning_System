# Generated by Django 3.2.8 on 2021-11-25 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_quesmodel_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='quesmodel',
            name='Quiz_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
