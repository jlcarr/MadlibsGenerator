# Generated by Django 4.1.2 on 2022-10-29 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='substitution',
            name='tag',
        ),
        migrations.AddField(
            model_name='substitution',
            name='lemma',
            field=models.CharField(default='test', max_length=20),
            preserve_default=False,
        ),
    ]