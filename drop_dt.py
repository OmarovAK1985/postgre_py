from main import connect_one


connect_one.connect().execute('DROP TABLE if exists album_list, compilation, compilation_track, list_of_genres, list_of_singers,'
                              'singer_album, singers_genres, tracks cascade;')
