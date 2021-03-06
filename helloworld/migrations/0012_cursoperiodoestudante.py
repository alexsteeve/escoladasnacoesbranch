# Generated by Django 2.1 on 2018-09-02 17:31

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0011_cursoperiodo_diasemana'),
    ]

    operations = [
        migrations.CreateModel(
            name='CursoPeriodoEstudante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aprovacao', models.BooleanField()),
                ('presencas', models.BooleanField()),
                ('financeiro', models.BooleanField()),
                ('provas', models.BooleanField()),
                ('trabalhos', models.BooleanField()),
                ('cursoPeriodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helloworld.CursoPeriodo')),
                ('estudante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helloworld.Estudante')),
            ],
            managers=[
                ('objetos', django.db.models.manager.Manager()),
            ],
        ),
    ]
