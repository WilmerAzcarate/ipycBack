# Generated by Django 4.2 on 2023-04-29 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_comment='nombre del departamento', max_length=120)),
                ('codigo', models.IntegerField(db_comment='codigo que identifica el departamento')),
            ],
            options={
                'db_table': 'departamento',
                'db_table_comment': 'tabla de departamentos o estados\n',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('calorias', models.FloatField(blank=True, null=True)),
                ('grasas', models.FloatField(blank=True, null=True)),
                ('proteinas', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ingrediente',
                'db_table_comment': 'aquello ingredientes que se usaran para preparar distintas recetas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'menu',
                'db_table_comment': 'un conjunto de platos puestos en venta',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_comment='nombre del municiopio', max_length=120)),
                ('codigo', models.IntegerField(db_comment='codigo que identifica el municiopio')),
                ('departamento', models.ForeignKey(db_comment='id del departamento al que pertenece el municipio', on_delete=django.db.models.deletion.DO_NOTHING, to='principal.departamento')),
            ],
            options={
                'db_table': 'municipio',
                'db_table_comment': 'tabla de municipios o ciudades',
                'managed': True,
                'unique_together': {('id', 'departamento')},
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_comment='nombre del pais', max_length=120)),
                ('codigo', models.IntegerField(db_comment='codigo que identifica el pais')),
            ],
            options={
                'db_table': 'pais',
                'db_table_comment': 'tabla de paises',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Rstaurante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('direccion', models.CharField(max_length=120)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
            ],
            options={
                'db_table': 'rstaurante',
                'db_table_comment': 'negocio donde se consiguen platos de comida',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Suscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('valor', models.FloatField()),
                ('fecha_inicio', models.DateField(db_comment='inicio de la suscripcion')),
                ('fecha_fin', models.DateField(db_comment='fecha en la que termina la suscripcion')),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'suscripcion',
                'db_table_comment': 'esta tabla guarda las distintas supcripciones que se pueden comprar\n',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TIdentificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_comment='nombre del tipo de identificacion, nesesario para ser mostrado en los formularios', max_length=120)),
                ('descripcion', models.TextField(blank=True, db_comment='descripcion , da informacion a los usuarios del para que se usa la identificacion', null=True)),
            ],
            options={
                'db_table': 't_identificacion',
                'db_table_comment': 'aqui se guardan los tipos de identificacion disponibles\n',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('direccion', models.CharField(max_length=120)),
                ('telefono', models.CharField(blank=True, max_length=120, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('latitud', models.FloatField(blank=True, null=True)),
                ('longitud', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tienda',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TIngrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_ingrediente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TOferta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_oferta',
                'db_table_comment': 'las ofertas pueden ser de varios tipos:\nporcentuales\nnxn\notro',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TReceta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_receta',
                'db_table_comment': 'las recetas pueden venir de varios tipos , por ejemplo, almuerzo, comida o desayuno; y tambien celebracion , salud , vegetariana etc ...',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.TextField(blank=True, db_comment='las recetas que publica la gente', null=True)),
                ('t_receta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.treceta')),
            ],
            options={
                'db_table': 'receta',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_nombre', models.CharField(db_comment='primer nombre del usuario - este campo es obligatorio', max_length=120)),
                ('s_nombre', models.CharField(blank=True, db_comment='segundo nombre del usuario - este campo no es obligatorio', max_length=120, null=True)),
                ('p_apellido', models.CharField(db_comment='primer apellido del usuario - este campo es obligatorio', max_length=120)),
                ('s_apellido', models.CharField(blank=True, db_comment='segundo apellido del usuario - este campo no es obligatorio', max_length=120, null=True)),
                ('fecha_nacimiento', models.DateField(db_comment='este campo guarda la fecha de nacimiento del usuario, usado para calcular la edad del usuario')),
                ('n_identificacion', models.CharField(db_comment='numero de identificacion, usado para diferenciar a una persona de otra', max_length=20, unique=True)),
                ('municipio', models.ForeignKey(db_comment='municipio al que pertenece el usuario', on_delete=django.db.models.deletion.DO_NOTHING, to='principal.municipio')),
                ('t_identificacion', models.ForeignKey(db_comment='el tipo de identificacion del usuario', on_delete=django.db.models.deletion.DO_NOTHING, to='principal.tidentificacion')),
            ],
            options={
                'db_table': 'persona',
                'db_table_comment': 'esta tabla guarda los datos de la persona',
                'managed': True,
                'unique_together': {('id', 'municipio', 't_identificacion')},
            },
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('ingrediente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.ingrediente')),
                ('tienda', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.tienda')),
            ],
            options={
                'db_table': 'inventario',
                'managed': True,
                'unique_together': {('id', 'ingrediente', 'tienda')},
            },
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='t_ingrediente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.tingrediente'),
        ),
        migrations.CreateModel(
            name='FacturaCabeza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField(db_comment='este campo registra el dinero pagado en la transaccion')),
                ('fecha', models.DateField(db_comment='este campo guarda el dia donde se lleva a cabo la transaccion')),
                ('persona', models.ForeignKey(db_comment='este campo sirve para saber que persona hizo la transaccion\n', on_delete=django.db.models.deletion.DO_NOTHING, to='principal.persona')),
            ],
            options={
                'db_table': 'factura_cabeza',
                'db_table_comment': 'esta tabla guarda las transacciones hechas por una persona',
                'managed': True,
                'unique_together': {('id', 'persona')},
            },
        ),
        migrations.AddField(
            model_name='departamento',
            name='pais',
            field=models.ForeignKey(db_comment='id del pais al que pertenece el departamento', on_delete=django.db.models.deletion.DO_NOTHING, to='principal.pais'),
        ),
        migrations.CreateModel(
            name='Carta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.menu')),
                ('rstaurante', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.rstaurante')),
            ],
            options={
                'db_table': 'carta',
                'managed': True,
                'unique_together': {('id', 'menu', 'rstaurante')},
            },
        ),
        migrations.CreateModel(
            name='Preparacion',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('codigo', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('receta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.receta')),
            ],
            options={
                'db_table': 'preparacion',
                'db_table_comment': 'estos son los pasos a realizar para preparar la receta\n',
                'managed': True,
                'unique_together': {('id', 'receta')},
            },
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.menu')),
                ('receta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.receta')),
            ],
            options={
                'db_table': 'plato',
                'db_table_comment': 'el plato ya preparado, aveces esta vinculado a un menu',
                'managed': True,
                'unique_together': {('id', 'receta')},
            },
        ),
        migrations.CreateModel(
            name='OfPlato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('valor', models.FloatField()),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('carta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.carta')),
                ('t_oferta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.toferta')),
            ],
            options={
                'db_table': 'of_plato',
                'db_table_comment': 'ofertas de platos',
                'managed': True,
                'unique_together': {('id', 't_oferta', 'carta')},
            },
        ),
        migrations.CreateModel(
            name='OfIngrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('valor', models.FloatField()),
                ('descricpion', models.TextField(blank=True, null=True)),
                ('inventario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.inventario')),
                ('t_oferta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.toferta')),
            ],
            options={
                'db_table': 'of_ingrediente',
                'db_table_comment': 'ofertas que afectan a los ingredientes',
                'managed': True,
                'unique_together': {('id', 't_oferta', 'inventario')},
            },
        ),
        migrations.CreateModel(
            name='ListIngredientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingrediente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.ingrediente')),
                ('receta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.receta')),
            ],
            options={
                'db_table': 'list_ingredientes',
                'managed': True,
                'unique_together': {('id', 'ingrediente', 'receta')},
            },
        ),
        migrations.CreateModel(
            name='FacturaCuerpo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(db_comment='cantidad del producto comprada')),
                ('valor', models.FloatField(db_comment='cantidad pagada por esa cantidad del producto')),
                ('factura_cabeza', models.ForeignKey(db_comment='datos de a que transaccion pertenece una compra', on_delete=django.db.models.deletion.DO_NOTHING, to='principal.facturacabeza')),
                ('suscripcion', models.ForeignKey(db_comment='identificacion del producto', on_delete=django.db.models.deletion.DO_NOTHING, to='principal.suscripcion')),
            ],
            options={
                'db_table': 'factura_cuerpo',
                'db_table_comment': 'esta tabla se encarga de guardar en de talle que se compro y enque cantidad',
                'managed': True,
                'unique_together': {('id', 'suscripcion', 'factura_cabeza')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('id', 'pais')},
        ),
    ]