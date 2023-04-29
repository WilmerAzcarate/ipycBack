# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Carta(models.Model):
    menu = models.ForeignKey('Menu', models.DO_NOTHING)
    rstaurante = models.ForeignKey('Rstaurante', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'carta'
        unique_together = (('id', 'menu', 'rstaurante'),)


class Departamento(models.Model):
    nombre = models.CharField(max_length=120, db_comment='nombre del departamento')
    codigo = models.IntegerField(db_comment='codigo que identifica el departamento')
    pais = models.ForeignKey('Pais', models.DO_NOTHING, db_comment='id del pais al que pertenece el departamento')

    class Meta:
        managed = True
        db_table = 'departamento'
        unique_together = (('id', 'pais'),)
        db_table_comment = 'tabla de departamentos o estados\n'


class FacturaCabeza(models.Model):
    valor = models.FloatField(db_comment='este campo registra el dinero pagado en la transaccion')
    fecha = models.DateField(db_comment='este campo guarda el dia donde se lleva a cabo la transaccion')
    persona = models.ForeignKey('Persona', models.DO_NOTHING, db_comment='este campo sirve para saber que persona hizo la transaccion\n')

    class Meta:
        managed = True
        db_table = 'factura_cabeza'
        unique_together = (('id', 'persona'),)
        db_table_comment = 'esta tabla guarda las transacciones hechas por una persona'


class FacturaCuerpo(models.Model):
    cantidad = models.IntegerField(db_comment='cantidad del producto comprada')
    valor = models.FloatField(db_comment='cantidad pagada por esa cantidad del producto')
    suscripcion = models.ForeignKey('Suscripcion', models.DO_NOTHING, db_comment='identificacion del producto')
    factura_cabeza = models.ForeignKey(FacturaCabeza, models.DO_NOTHING, db_comment='datos de a que transaccion pertenece una compra')

    class Meta:
        managed = True
        db_table = 'factura_cuerpo'
        unique_together = (('id', 'suscripcion', 'factura_cabeza'),)
        db_table_comment = 'esta tabla se encarga de guardar en de talle que se compro y enque cantidad'


class Ingrediente(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True, null=True)
    calorias = models.FloatField(blank=True, null=True)
    grasas = models.FloatField(blank=True, null=True)
    proteinas = models.FloatField(blank=True, null=True)
    t_ingrediente = models.ForeignKey('TIngrediente', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'ingrediente'
        db_table_comment = 'aquello ingredientes que se usaran para preparar distintas recetas'


class Inventario(models.Model):
    cantidad = models.IntegerField()
    ingrediente = models.ForeignKey(Ingrediente, models.DO_NOTHING)
    tienda = models.ForeignKey('Tienda', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'inventario'
        unique_together = (('id', 'ingrediente', 'tienda'),)


class ListIngredientes(models.Model):
    ingrediente = models.ForeignKey(Ingrediente, models.DO_NOTHING)
    receta = models.ForeignKey('Receta', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'list_ingredientes'
        unique_together = (('id', 'ingrediente', 'receta'),)


class Menu(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'menu'
        db_table_comment = 'un conjunto de platos puestos en venta'


class Municipio(models.Model):
    nombre = models.CharField(max_length=120, db_comment='nombre del municiopio')
    codigo = models.IntegerField(db_comment='codigo que identifica el municiopio')
    departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_comment='id del departamento al que pertenece el municipio')

    class Meta:
        managed = True
        db_table = 'municipio'
        unique_together = (('id', 'departamento'),)
        db_table_comment = 'tabla de municipios o ciudades'


class OfIngrediente(models.Model):
    nombre = models.CharField(max_length=120)
    valor = models.FloatField()
    descricpion = models.TextField(blank=True, null=True)
    t_oferta = models.ForeignKey('TOferta', models.DO_NOTHING)
    inventario = models.ForeignKey(Inventario, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'of_ingrediente'
        unique_together = (('id', 't_oferta', 'inventario'),)
        db_table_comment = 'ofertas que afectan a los ingredientes'


class OfPlato(models.Model):
    nombre = models.CharField(max_length=120)
    valor = models.FloatField()
    descripcion = models.TextField(blank=True, null=True)
    t_oferta = models.ForeignKey('TOferta', models.DO_NOTHING)
    carta = models.ForeignKey(Carta, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'of_plato'
        unique_together = (('id', 't_oferta', 'carta'),)
        db_table_comment = 'ofertas de platos'


class Pais(models.Model):
    nombre = models.CharField(max_length=120, db_comment='nombre del pais')
    codigo = models.IntegerField(db_comment='codigo que identifica el pais')

    class Meta:
        managed = True
        db_table = 'pais'
        db_table_comment = 'tabla de paises'


class Persona(models.Model):
    p_nombre = models.CharField(max_length=120, db_comment='primer nombre del usuario - este campo es obligatorio')
    s_nombre = models.CharField(max_length=120, blank=True, null=True, db_comment='segundo nombre del usuario - este campo no es obligatorio')
    p_apellido = models.CharField(max_length=120, db_comment='primer apellido del usuario - este campo es obligatorio')
    s_apellido = models.CharField(max_length=120, blank=True, null=True, db_comment='segundo apellido del usuario - este campo no es obligatorio')
    fecha_nacimiento = models.DateField(db_comment='este campo guarda la fecha de nacimiento del usuario, usado para calcular la edad del usuario')
    n_identificacion = models.CharField(unique=True, max_length=20, db_comment='numero de identificacion, usado para diferenciar a una persona de otra')
    municipio = models.ForeignKey(Municipio, models.DO_NOTHING, db_comment='municipio al que pertenece el usuario')
    t_identificacion = models.ForeignKey('TIdentificacion', models.DO_NOTHING, db_comment='el tipo de identificacion del usuario')

    class Meta:
        managed = True
        db_table = 'persona'
        unique_together = (('id', 'municipio', 't_identificacion'),)
        db_table_comment = 'esta tabla guarda los datos de la persona'


class Plato(models.Model):
    nombre = models.CharField(max_length=45)
    precio = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)
    receta = models.ForeignKey('Receta', models.DO_NOTHING)
    menu = models.ForeignKey(Menu, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'plato'
        unique_together = (('id', 'receta'),)
        db_table_comment = 'el plato ya preparado, aveces esta vinculado a un menu'


class Preparacion(models.Model):
    id = models.IntegerField(primary_key=True)  # The composite primary key (id, receta_id) found, that is not supported. The first column is selected.
    codigo = models.IntegerField()
    descripcion = models.TextField()
    receta = models.ForeignKey('Receta', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'preparacion'
        unique_together = (('id', 'receta'),)
        db_table_comment = 'estos son los pasos a realizar para preparar la receta\n'


class Receta(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField(blank=True, null=True, db_comment='las recetas que publica la gente')
    t_receta = models.ForeignKey('TReceta', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'receta'


class Rstaurante(models.Model):
    nombre = models.CharField(max_length=120)
    direccion = models.CharField(max_length=120)
    telefono = models.IntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    latitud = models.FloatField()
    longitud = models.FloatField()

    class Meta:
        managed = True
        db_table = 'rstaurante'
        db_table_comment = 'negocio donde se consiguen platos de comida'


class Suscripcion(models.Model):
    nombre = models.CharField(max_length=120)
    valor = models.FloatField()
    fecha_inicio = models.DateField(db_comment='inicio de la suscripcion')
    fecha_fin = models.DateField(db_comment='fecha en la que termina la suscripcion')
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'suscripcion'
        db_table_comment = 'esta tabla guarda las distintas supcripciones que se pueden comprar\n'


class TIdentificacion(models.Model):
    nombre = models.CharField(max_length=120, db_comment='nombre del tipo de identificacion, nesesario para ser mostrado en los formularios')
    descripcion = models.TextField(blank=True, null=True, db_comment='descripcion , da informacion a los usuarios del para que se usa la identificacion')

    class Meta:
        managed = True
        db_table = 't_identificacion'
        db_table_comment = 'aqui se guardan los tipos de identificacion disponibles\n'


class TIngrediente(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_ingrediente'


class TOferta(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_oferta'
        db_table_comment = 'las ofertas pueden ser de varios tipos:\nporcentuales\nnxn\notro'


class TReceta(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_receta'
        db_table_comment = 'las recetas pueden venir de varios tipos , por ejemplo, almuerzo, comida o desayuno; y tambien celebracion , salud , vegetariana etc ...'


class Tienda(models.Model):
    nombre = models.CharField(max_length=120)
    direccion = models.CharField(max_length=120)
    telefono = models.CharField(max_length=120, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tienda'
