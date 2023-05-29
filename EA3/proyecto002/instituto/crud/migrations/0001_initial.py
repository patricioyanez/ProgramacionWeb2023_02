# Generated by Django 4.2.1 on 2023-05-26 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('idMarca', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, null=True, unique=True)),
                ('activo', models.BooleanField()),
            ],
        ),
    ]