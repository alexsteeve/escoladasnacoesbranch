# Generated by Django 2.1 on 2018-09-30 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0018_curso_tipocurso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursoperiodoestudante',
            name='aprovacao',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cursoperiodoestudante',
            name='financeiro',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cursoperiodoestudante',
            name='presencas',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cursoperiodoestudante',
            name='provas',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cursoperiodoestudante',
            name='trabalhos',
            field=models.BooleanField(default=False),
        ),
    ]
