# Generated by Django 4.2.7 on 2023-12-10 15:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppEncuesta', '0003_alter_opinion_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2023, 12, 10, 15, 11, 20, 262204)),
        ),
        migrations.CreateModel(
            name='RespuestaAlternativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_alternativa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppEncuesta.alternativa')),
                ('id_pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppEncuesta.pregunta')),
            ],
        ),
    ]
