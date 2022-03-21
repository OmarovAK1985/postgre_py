from main import connect_one


def album_selection():
    tuple_name = connect_one.connect().execute(
        f"SELECT album_name, year FROM album_list WHERE year = '2008'").fetchall()
    count = 1
    print('Название и год выходов альбомов, вышедших  в 2018 году')
    for i in tuple_name:
        print(f'\t{count}. Название альбома: {i[0]}. Год выпуска: {i[1]} год.')
        count = count + 1


def long_song_selection():
    tuple_name = connect_one.connect().execute(f"SELECT name_of_the_track, duration FROM tracks "
                                               f"WHERE duration = (SELECT MAX(duration) FROM tracks)").fetchall()
    for i in tuple_name:
        print('Самый длительный трек:')
        print(f'\tНазвание трека: {i[0]}, Длительность трека: {i[1]}')


def selection_of_short_songs():
    tuple_name = connect_one.connect().execute(f"SELECT name_of_the_track FROM tracks WHERE "
                                               f"duration < '00:03:30' ORDER BY duration DESC").fetchall()
    print('Список песен длительность менее 3,5 минут')
    count = 1
    for i in tuple_name:
        print(f'\t{count}. {i[0].strip()}')
        count = count + 1


def selection_of_collections():
    start_year = 2018
    end_year = 2020
    count = 1
    tuple_name = connect_one.connect().execute(
        f"SELECT name FROM compilation WHERE year <= {end_year} AND year >= {start_year} ").fetchall()
    if len(tuple_name) > 0:
        print(f'Название сборников вышедших в период с {start_year} года по {end_year} год:')
        for name_of_the_compilation in tuple_name:
            print(f'\t {count}. Название сборника - {name_of_the_compilation[0]}')
            count = count + 1
    else:
        print(f'Сборников вышедших в период с {start_year} года по {end_year} год в данной таблице не найдено.')


def selection_of_artists():
    tuple_names_singer = connect_one.connect().execute(f"SELECT singer_name FROM list_of_singers "
                                                       f"WHERE singer_name NOT LIKE '%% %%'").fetchall()
    print('Исполнители с одним именем: ')
    count = 1
    for i in tuple_names_singer:
        print(f"\t{count}. {i[0]}")
        count = count + 1


def song_selection():
    tuple_name_track = connect_one.connect().execute(
        f"SELECT name_of_the_track FROM tracks WHERE name_of_the_track LIKE '%%my%%' OR  name_of_the_track LIKE '%%мой%%' ").fetchall()
    count = 1
    print('Список песен с вхождением:')
    for name_track in tuple_name_track:
        print(f'\t{count}. {name_track[0]}')
        count = count + 1


def genre_count_singers():
    tuple_list = connect_one.connect().execute(f"SELECT genres, COUNT(singer_name) FROM list_of_singers "
                                               f"LEFT JOIN singers_genres ON list_of_singers.id = singers_genres.id_singer "
                                               f"LEFT JOIN list_of_genres ON list_of_genres.id = singers_genres.id_genres "
                                               f"GROUP BY genres;").fetchall()
    count = 1
    print('Количество исполнителей в разрезе жанров:')
    for i in tuple_list:
        print(f'\t {count}. Жанр: {i[0].title()}, Количество исполнителей: {i[1]}')
        count = count + 1


def count_tracks():
    tuple_list = connect_one.connect().execute(f"SELECT year, COUNT(name_of_the_track)  FROM tracks "
                                               f"LEFT JOIN album_list ON  tracks.album_id = album_list.id "
                                               f"WHERE year > 2018 and year < 2021 "
                                               f"GROUP BY year").fetchall()
    count = 1
    print("Количество альбомов в разрезе 2019 - 2020 г.г.")
    for i in tuple_list:
        print(f'\t{count}.Год выпуска альбома: {i[0]} год, Количество альбомов {i[1]}')
        count = count + 1


def average_duration_albums():
    tuple_list = connect_one.connect().execute(
        f"SELECT album_name, date_trunc('second', AVG(duration)) FROM album_list "
        f"LEFT JOIN tracks ON album_list.id = tracks.album_id "
        f"GROUP BY album_name  "
        f"ORDER BY AVG(duration)").fetchall()
    count = 1
    print('Средняя продолжительность альбомов: ')
    for i in tuple_list:
        print(f'\t{count}. Название альбома: {i[0].strip()}, Средняя продолжительность альбома: {i[1]}')
        count = count + 1


def select_singers_not_albums():
    tuple_list = connect_one.connect().execute(
        f"SELECT singer_name FROM album_list "
        f"LEFT JOIN singer_album ON album_list.id = singer_album.id_album "
        f"LEFT JOIN list_of_singers ON singer_album.id_singer = list_of_singers.id "
        f"WHERE year = 2020 ").fetchall()

    two_thousand_twenty_set = set()
    for i in tuple_list:
        two_thousand_twenty_set.add(i[0])

    tuple_list = connect_one.connect().execute(
        f"SELECT singer_name FROM album_list "
        f"LEFT JOIN singer_album ON album_list.id = singer_album.id_album "
        f"LEFT JOIN list_of_singers ON singer_album.id_singer = list_of_singers.id "
        f"WHERE year != 2020 ").fetchall()

    no_two_thousand_twenty_set = set()
    for i in tuple_list:
        no_two_thousand_twenty_set.add(i[0])

    new_set = no_two_thousand_twenty_set.difference(two_thousand_twenty_set)
    count = 1
    print('Список исполнителей не выпустивших альбомы в 2020 году:')
    for i in new_set:
        print(f"\t{count}. Исполнитель: {i}")
        count = count + 1


def singer_compilation(name='Red Hot Chili Peppers'):
    tuple_list = connect_one.connect().execute(f"SELECT name FROM compilation "
                                               f"LEFT JOIN compilation_track ON compilation.id = compilation_track.id_compilation "
                                               f"LEFT JOIN tracks ON compilation_track.id_track = tracks.id  "
                                               f"LEFT JOIN album_list on tracks.album_id = album_list.id "
                                               f"LEFT JOIN singer_album ON album_list.id = singer_album.id_album "
                                               f"LEFT JOIN list_of_singers ON  singer_album.id_singer = list_of_singers.id "
                                               f"WHERE singer_name = '{name}'").fetchall()
    count = 0

    if len(tuple_list) > 0:
        print(f'Список сборников, в которых есть {name}:')
        for i in tuple_list:
            count = count + 1
            print(f'\t{count}. Название сборника, в котором присутствует {name.upper()}: {i[0]}')
    else:
        print(f"У исполнителя {name.upper()} нет сборников")


def name_of_albums_more_one_genres():
    tuple_list = connect_one.connect().execute(f"SELECT album_name, count(id_genres) FROM singers_genres "
                                               f"LEFT JOIN list_of_singers ON singers_genres.id_singer = list_of_singers.id "
                                               f"LEFT JOIN singer_album ON list_of_singers.id = singer_album.id_singer "
                                               f"LEFT JOIN album_list ON singer_album.id_album = album_list.id "
                                               f"GROUP BY album_name "
                                               f"HAVING COUNT (id_genres) > 1").fetchall()

    print('Название альбомов, в которых присутствуют исполнители более 1 жанра: ')
    count = 0
    for i in tuple_list:
        count = count + 1
        print(f'\t{count}. Название альбома: {i[0]}')


def tracks_not_in_compilation():
    tuple_list = connect_one.connect().execute(f"SELECT name_of_the_track FROM tracks "
                                               f"LEFT JOIN compilation_track ON tracks.id = compilation_track.id_track "
                                               f"LEFT JOIN compilation ON compilation_track.id_compilation = compilation.id "
                                               f" WHERE compilation.id IS NULL "
                                               f"").fetchall()

    print('Название песен не вошедших в сборники: ')
    count = 0
    for i in tuple_list:
        count = count + 1
        print(f'\t{count}. {i[0].strip()}')


def short_album():
    connect_one.connect().execute(f"INSERT INTO album_list (album_name, year) VALUES ('short_album', '2022')"
                                  f"ON CONFLICT DO NOTHING;")

    id_album = connect_one.connect().execute(f"SELECT id FROM album_list WHERE album_name = 'short_album'").fetchone()
    for i in id_album:
        connect_one.connect().execute(f"INSERT INTO tracks (name_of_the_track, album_id) VALUES ('Тест', '{i}')"
                                      f"ON CONFLICT DO NOTHING;")

    tuple_list = connect_one.connect().execute(f"SELECT album_name, COUNT(*) FROM album_list "
                                               f"LEFT JOIN tracks ON album_list.id = tracks.album_id "
                                               f"GROUP BY album_name "
                                               f"HAVING COUNT(*) = (SELECT COUNT(*) FROM album_list  "
                                                                    f"LEFT JOIN tracks ON album_list.id = tracks.album_id "
                                                                    f"GROUP BY album_name ORDER BY COUNT (*) ASC LIMIT 1) "
                                               ).fetchall()

    print('Название альбомов с меньшим количеством песен: ')
    count = 0
    for i in tuple_list:
        count = count + 1
        print(f'\t{count}. {i[0]}')


def short_track():
    tuple_list = connect_one.connect().execute(f"SELECT singer_name, duration FROM list_of_singers "
                                               f"LEFT JOIN singer_album ON list_of_singers.id = singer_album.id_singer "
                                               f"LEFT JOIN album_list ON singer_album.id_album = album_list.id "
                                               f"LEFT JOIN tracks ON album_list.id = tracks.album_id "
                                               f"WHERE duration = (SELECT MIN(duration) FROM tracks)"
                                               ).fetchall()

    print('Список исполнителей с самым коротким треком')
    count = 0
    for i in tuple_list:
        count = count + 1
        print(f"\t{count}. Исполнитель: {i[0]}")


album_selection()
long_song_selection()
selection_of_short_songs()
selection_of_collections()
selection_of_artists()
song_selection()
genre_count_singers()
count_tracks()
average_duration_albums()
select_singers_not_albums()
singer_compilation()
name_of_albums_more_one_genres()
tracks_not_in_compilation()
short_track()
short_album()

