# Generated by Django 2.2.7 on 2019-12-04 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledgebase', '0003_auto_20191202_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='woord',
            name='accurate',
            field=models.BooleanField(default=True),
        ),
    ]
