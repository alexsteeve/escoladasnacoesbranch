# Generated by Django 2.1 on 2018-10-03 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0019_auto_20180930_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursoperiodo',
            name='matriculasAbertas',
            field=models.BooleanField(default=False),
        ),
    ]