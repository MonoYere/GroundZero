from django.db import models

class Artista(models.Model):
    id_artista = models.AutoField(db_column='idArtista', primary_key=True)
    nmb_artista = models.CharField(max_length=120)

    def __str__(self):
        return str(self.nmb_artista)


class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='idCategoria', primary_key=True)
    nmb_categoria = models.CharField(max_length=120)

    def __str__(self):
        return str(self.nmb_categoria)


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nmb_producto = models.CharField(max_length=120)
    fch_creacion = models.DateField(blank=False, null=False)
    id_categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, db_column='idCategoria')
    id_artista = models.ForeignKey('Artista', on_delete=models.CASCADE, db_column='idArtista')

    def __str__(self):
        return str(self.nmb_producto)
