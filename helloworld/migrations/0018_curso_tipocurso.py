# Generated by Django 2.1 on 2018-09-13 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0017_tipocurso'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='tipoCurso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='helloworld.TipoCurso'),
            preserve_default=False,
        ),
    ]
