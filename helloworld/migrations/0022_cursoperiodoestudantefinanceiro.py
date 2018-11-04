# Generated by Django 2.1.2 on 2018-11-04 18:21

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0021_estudante_profissao'),
    ]

    operations = [
        migrations.CreateModel(
            name='CursoPeriodoEstudanteFinanceiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagamentos', models.CharField(default=False, max_length=255)),
                ('cursoPeriodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helloworld.CursoPeriodo')),
                ('estudante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helloworld.Estudante')),
            ],
            managers=[
                ('objetos', django.db.models.manager.Manager()),
            ],
        ),
    ]