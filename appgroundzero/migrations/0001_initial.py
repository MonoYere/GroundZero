# Generated by Django 4.2.2 on 2023-06-22 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id_artista', models.AutoField(db_column='idArtista', primary_key=True, serialize=False)),
                ('nmb_artista', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(db_column='idCategoria', primary_key=True, serialize=False)),
                ('nmb_categoria', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nmb_producto', models.CharField(max_length=120)),
                ('fch_creacion', models.DateField()),
                ('id_artista', models.ForeignKey(db_column='idArtista', on_delete=django.db.models.deletion.CASCADE, to='appgroundzero.artista')),
                ('id_categoria', models.ForeignKey(db_column='idCategoria', on_delete=django.db.models.deletion.CASCADE, to='appgroundzero.categoria')),
            ],
        ),
    ]
