from main import connect_one

connect_one.connect().execute(
    'create table if not exists list_of_genres (id serial primary key, genres varchar(40) unique);'
    'create table if not exists list_of_singers (id serial primary key, singer_name varchar(40) unique);'
    'create table if not exists singers_genres (id_singer integer references list_of_singers(id), id_genres integer references list_of_genres(id), constraint pk primary key (id_singer, id_genres));'
    'create table if not exists album_list (id serial primary key, album_name varchar (40) unique, year numeric check (year >1000));'
    'create table if not exists singer_album (id serial primary key, id_singer integer references list_of_singers (id), id_album integer references album_list(id));'
    'create table if not exists tracks (id serial primary key, name_of_the_track varchar(40) unique, duration interval MINUTE TO SECOND, track_link text unique, album_id integer references album_list(id));'
    'create table if not exists compilation (id serial primary key, name varchar(40) unique, year numeric check (year >1000));'
    'create table if not exists compilation_track (id_track integer references tracks(id), id_compilation integer references compilation(id), constraint pk_compilaion_track primary key(id_track, id_compilation));'
    )
