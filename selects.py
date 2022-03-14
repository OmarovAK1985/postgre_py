from main import connect_one
from datetime import timedelta


def album_selection():
    tuple_name = connect_one.connect().execute(
        f"SELECT album_name, year FROM album_list WHERE year = '2008'").fetchall()
    count = 1
    print('Название и год выходов альбомов, вышедших  в 2018 году')
    for i in tuple_name:
        print(f'\t{count}. Название альбома: {i[0]}. Год выпуска: {i[1]} год.')
        count = count + 1


def long_song_selection():
    tuple_name = connect_one.connect().execute(f"SELECT duration FROM tracks").fetchall()
    list_duration = []
    for i in tuple_name:
        for val in i:
            list_duration.append(val)
    count = timedelta()
    for i in list_duration:
        if i > count:
            count = i

    tuple_name = connect_one.connect().execute(
        f"SELECT name_of_the_track, duration FROM tracks WHERE duration = '{count}'").fetchall()
    print('Самая длительная песня:')
    for i in tuple_name:
        duration = str(i[1])
        duration = duration[2:].replace(':', ' минут ') + ' секунд'
        print(f'\tНазвание песни: {i[0]}, длительность которой {duration}.')


def selection_of_short_songs():
    tuple_name = connect_one.connect().execute(f"SELECT duration FROM tracks").fetchall()
    list_duration = []
    for i in tuple_name:
        for val in i:
            list_duration.append(val)
    count = timedelta()
    for i in list_duration:
        if i > count:
            count = i
    count = timedelta(minutes=3, seconds=30)
    m = 1
    print(f'Название песен с длительностью до {count}')
    for i in list_duration:
        if i < count:
            tuple_name = connect_one.connect().execute(
                f"SELECT name_of_the_track FROM tracks WHERE duration = '{i}'").fetchall()
            for name in tuple_name:
                print(f'\t{m}. Название песни: {name[0].strip()}')
                m = m + 1


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
    tuple_names_singer = connect_one.connect().execute(f"SELECT singer_name FROM list_of_singers").fetchall()
    list_name_singer = []
    for i in tuple_names_singer:
        if i[0].count(' ') == 0:
            list_name_singer.append(i[0])
    print(f'Имена артистов с одним словом:')
    count = 1
    for i in list_name_singer:
        print(f"\t {count}. {i}")
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