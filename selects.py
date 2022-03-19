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

album_selection()
long_song_selection()
selection_of_short_songs()
selection_of_collections()
selection_of_artists()
song_selection()

