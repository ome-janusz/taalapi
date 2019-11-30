# Generated by Django 2.2.7 on 2019-11-30 19:13

from django.db import migrations, models
import django.db.models.deletion
import lidwoorden.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lidwoord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=3, unique=True, validators=[lidwoorden.validators.validate_lidwoord])),
            ],
            options={
                'verbose_name_plural': 'lidwoorden',
            },
        ),
        migrations.CreateModel(
            name='Woord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=256)),
                ('lidwoord', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lidwoorden.Lidwoord')),
            ],
            options={
                'verbose_name_plural': 'woorden',
            },
        ),
    ]