# Generated by Django 4.0.3 on 2022-09-29 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Numero_telefonico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='numeros',
            field=models.ManyToManyField(to='Registro.numero_telefonico'),
        ),
    ]
