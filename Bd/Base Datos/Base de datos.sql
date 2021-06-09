--Creacion de BD
create database school;

--crear tablas

--tabla usuario
create table usuario(
id_usuario int primary key,
usuario varchar(15),
contraseña varchar(300),
rol int
)
--add foranea
alter table usuario add foreign key(rol) references rol(id_rol) on delete cascade on update cascade

--tabla rol
create table rol(
    id_rol int,
    nombre varchar(30),
    primary key(id_rol)
)
--tabla profesor
create table profesor(
    id_profesor int primary key,
    nombre varchar(30),
    apellido varchar(30),
    cedula bigint,
    correo varchar(60),
    telefono varchar(15),
    usuario int
    )
--add foreana
alter table profesor add foreign key(usuario) references usuario(id_usuario) on delete cascade on update cascade
-- table estudiante
create table estudiante(
    id_estudiante int primary key,
    nombre varchar(30),
    apellido varchar(30),
    tipo_documento varchar(30),
    documento bigint,
    correo varchar(60),
    telefono varchar(15),
    acudiente varchar(80),
    usuario int
)
--add foranea
alter table estudiante add foreign key(usuario) references usuario(id_usuario) on delete cascade on update cascade

--tabla profesor-actividad
create table profesor_actividad(
    profesor int,
    actividad int
)
--add foranea
alter table profesor_actividad add foreign key(actividad) references actividad(id_actividad) on delete cascade on update cascade
alter table profesor_actividad add foreign key(profesor)references profesor(id_profesor) on delete cascade on update cascade
--tabla actividad
create table actividad(
    id_actividad int primary key,
    nombre varchar(60),
    fecha_entrega date
)
--tabla actividad-materia
create table actividad_materia(
    actividad int,
    materia int
)
--add foranea
alter table actividad_materia add foreign key(actividad) references actividad(id_actividad) on delete cascade on update cascade
alter table actividad_materia add foreign key(materia) references materia(id_materia) on delete cascade on update cascade

--tabla estudiante-calificacion
create table estudiante_calificacion(
    estudiante int,
    calificacion int
)
--add foranea
alter table estudiante_calificacion add foreign key(calificacion) references calificacion(id_calificacion) on delete cascade on update cascade
alter table estudiante_calificacion add foreign key (estudiante) references estudiante(id_estudiante) on delete cascade on update cascade
--tabla estudiante-grado
create table estudiante_grado(
    estudiante int,
    grado int
)
--add foranea
alter table estudiante_grado add foreign key(estudiante) references estudiante(id_estudiante) on delete cascade on update cascade
alter table estudiante_grado add foreign key(grado) references grado(id_grado) on delete cascade on update cascade

-- table grado
create table grado(
    id_grado int primary key,
    nombre varchar(60),
    cantidad int,
    aula int

)
--add foranea
alter table grado add foreign key (aula) references aula(id_aula) on delete cascade on update cascade
--tabla aula
create table aula(
    id_aula int primary key,
    numero int,
    capacidad int,
    grado int
)
--add foranea
alter table aula add foreign key (grado) references grado(id_grado) on delete cascade on update cascade

--tabla materia
create table materia(
    id_materia int primary key,
    nombre varchar(60),
    horario varchar(20)
)
--tabla materia-calificacion
create table materia_calificacion(
    materia int,
    calificacion int
)
--add tabla
alter table materia_calificacion add foreign key(materia) references materia(id_materia) on delete cascade on update cascade
alter table materia_calificacion add foreign key(calificacion) references calificacion(id_calificacion) on delete cascade on update cascade

-- tabla calificacion
create table calificacion(
    id_calificacion int primary key,
    nombre varchar(60),
    numero bigint,
    periodo int
)
--add foranea
alter table calificacion add foreign key(periodo) references periodo(id_periodo) on delete cascade on update cascade
-- tabla periodo
create table periodo(
    id_periodo int primary key,
    fecha date,
    numero int 

)

insert into usuario values(1,'admin','admin',1)
insert into rol values(1,'administrador') 