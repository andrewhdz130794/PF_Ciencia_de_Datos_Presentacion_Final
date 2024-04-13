ddl = '''
create table categoria(
idcategoria int auto_increment primary key,
nombre varchar(50),
descripcion varchar(255),
estado bit
);

create table rol(
idrol int auto_increment primary key,
nombre varchar(30),
descripcion varchar(255),
estado bit
);

create table articulo(
idarticulo int auto_increment primary key,
idcategoria int,
codigo varchar(50),
nombre varchar(50),
precio_venta decimal(11,2),
stock int,
descripcion varchar(255),
imagen varchar(20),
estado bit,
constraint fk_categoria foreign key (idcategoria) references categoria(idcategoria)
	on delete set null
	on update cascade
);

create table persona(
idpersona int auto_increment primary key,
tipo_persona varchar(20),
nombre varchar(100),
tipo_documento varchar(20),
num_documento varchar(20) not null,
direccion varchar(70),
telefono varchar(20),
email varchar(50)
);

create table usuario(
idusuario int auto_increment primary key,
idrol int,
nombre varchar(100),
tipo_documento varchar(20),
num_documento varchar(20),
direccion varchar(70),
telefono varchar(20),
email varchar(50),
clave varbinary(255),
estado bit,
constraint fk_rol foreign key (idrol) references rol(idrol)
	on delete set null
	on update cascade,
);

create table venta(
idventa int auto_increment primary key,
idcliente int,
idusuario int,
tipo_comprobante varchar(20),
serie_comprobante varchar(7),
num_comprabante varchar(10),
fecha datetime,
impuesto decimal(4,2),
total decimal(11,2),
estado varchar(20),
constraint fk_idcliente foreign key (idcliente) references persona(idpersona)
	on delete set null
	on update cascade,
constraint fk_idusuario_vta foreign key (idusuario) references usuario(idusuario)
	on delete set null
	on update cascade
);

create table ingreso(
idingreso int auto_increment primary key,
idproveedor int,
idusuario int,
tipo_comprobante varchar(20),
serie_comprobante varchar(7),
num_comprobante varchar(10),
fecha datetime,
impuesto decimal(4,2),
total decimal(11,2),
estado varchar(20),
constraint fk_idproveedor foreign key (idproveedor) references persona(idpersona)
	on delete set null
	on update cascade,
constraint fk_idusuario_ing foreign key (idusuario) references usuario(idusuario)
	on delete set null
	on update cascade
);

/* Tablas detalle */
create table detalle_ingreso(
iddetalle_ingreso int auto_increment primary key,
idingreso int not null,
idarticulo int not null,
cantidad int not null,
precio decimal(11,2),
constraint fk_idingreso foreign key (idingreso) references ingreso(idingreso)
	on delete cascade
	on update cascade,
constraint fk_idarticulo_ing foreign key (idarticulo) references articulo(idarticulo)
	on delete cascade
	on update cascade
);

create table detalle_venta(
iddetalle_venta int auto_increment primary key,
idventa int not null,
idarticulo int not null,
cantidad int not null,
precio decimal(11,2),
descuento decimal(11,2),
constraint fk_idventa foreign key (idventa) references venta(idventa)
	on delete cascade
	on update cascade,
constraint fk_idarticulo_vta foreign key (idarticulo) references articulo(idarticulo)
	on delete cascade
	on update cascade
);
'''