# Generated by Django 2.2.7 on 2019-12-02 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledgebase', '0002_populate_lidwoorden'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='woord',
            name='lidwoord',
        ),
        migrations.AddField(
            model_name='woord',
            name='lidwoord',
            field=models.ManyToManyField(to='knowledgebase.Lidwoord'),
        ),
    ]