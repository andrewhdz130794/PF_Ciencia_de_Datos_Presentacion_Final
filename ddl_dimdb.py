ddl = '''
create table dim_articulo(
idarticulo int primary key,
codigo varchar(50),
articulo_nombre varchar(100),
precio_venta decimal(11,2),
stock int,
articulo_descrip varchar(255),
articulo_estado bit,
categoria_nombre varchar(50),
categoria_descrip varchar(255)
);

create table dim_usuario(
idusuario int primary key,
nombre_u varchar(100),
direccion_u varchar(70),
telefono_u varchar(20),
email_u varchar(50),
estado_u bit,
rol_nombre varchar(30),
rol_descrip varchar(255)
);

create table dim_persona(
idpersona int primary key,
tipo_persona varchar(20),
nombre_p varchar(100),
direccion_p varchar(70),
telefono_p varchar(20),
email_p varchar(50)
);

create table dim_calendar(
fecha date primary key,
mes int,
año int,
dia_mes int,
dia_semana int,
semana_año int
);

/* Fact Tables */
create table fact_venta(
idventa int,
idcliente int,
idusuario int,
fecha date,
idarticulo int,
venta_u int,
venta_d decimal(11,2),
descuento_d decimal(11,2),
impuesto_v decimal(11,2)
);

create table fact_ingreso(
idingreso int,
idproveedor int,
idusuario int,
fecha date,
idarticulo int,
compra_u int,
compra_d decimal(11,2),
impuesto_i decimal(11,2)
);

/* Foreign keys */
alter table fact_venta
	add constraint fk_idcliente foreign key (idcliente) references dim_persona(idpersona);
alter table fact_venta
	add constraint fk_idusuario foreign key (idusuario) references dim_usuario(idusuario);
alter table fact_venta
	add constraint fk_idarticulo foreign key (idarticulo) references dim_articulo(idarticulo);
alter table fact_venta
	add constraint fk_fecha foreign key (fecha) references dim_Calendar(fecha);


alter table fact_ingreso
	add constraint fk_idproveedor foreign key (idproveedor) references dim_persona(idpersona);
alter table fact_ingreso
	add constraint fk_idusuario foreign key (idusuario) references dim_usuario(idusuario);
alter table fact_ingreso
	add constraint fk_idarticulo foreign key (idarticulo) references dim_articulo(idarticulo);
alter table fact_ingreso
	add constraint fk_fecha foreign key (fecha) references dim_Calendar(fecha);

'''