# Generated by Django 5.0.1 on 2024-02-05 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('apellido', models.CharField(max_length=64)),
                ('edad', models.IntegerField()),
                ('pago_primera_cuota', models.BooleanField()),
                ('turno', models.IntegerField()),
                ('fecha_ingreso', models.DateField()),
            ],
        ),
    ]