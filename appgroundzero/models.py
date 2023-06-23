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
    id_producto = models.AutoField(primary_key=True, verbose_name='Id')
    nmb_producto = models.CharField(max_length=120, verbose_name='Nombre')
    imagen = models.ImageField(upload_to='imagenes/',verbose_name='Imagen', null=True, blank=True)
    fch_creacion = models.DateField(blank=False, null=False, verbose_name='Fecha de creación')
    id_categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, db_column='idCategoria', verbose_name='Id de la categoria')
    id_artista = models.ForeignKey('Artista', on_delete=models.CASCADE, db_column='idArtista', verbose_name='Id del artista')

    def __str__(self):
        return str(self.nmb_producto)
    