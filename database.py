import json
from datetime import datetime as dt

current_date_format = '%d-%m-%Y %H:%M:%S'

# crear archivo
# leer archivo
# actualizar archivo


def get_current_date():
    current_date = dt.now()
    formatted_current_date = current_date.strftime(current_date_format)

    return formatted_current_date


def set_filename():
    current_date = dt.now()
    filename = current_date.strftime('%d%m%Y%H%M%S')

    return filename


current_filename = set_filename()
file_path = f'./database/{current_filename}.json'


def create_file():
    with open(file_path, 'w') as db:
        db.write('{}')


def read_file():
    with open(file_path, 'r', encoding='utf-8') as db:
        data = json.load(db)

    return data


def update_file(new_db):
    with open(file_path, 'w', encoding='utf-8') as db:
        json.dump(new_db, db)


def letter_json_format(letter, position):
    current_date = get_current_date()

    letter_dict = {letter: {
        "fechahora_apertura": current_date,
        "posicion_apertura": {"f": position[0], "c": position[1]},
        "intentos": {}
    }}

    return letter_dict


def attempt_json_format(attempts_count, position, pair_found):
    current_date = get_current_date()

    attempt_dict = {f"{attempts_count}": {
        "posicion": {"f": position[0], "c": position[1]},
        "fechahora_jugada": current_date
    }}

    if pair_found:
        attempt_dict['encontro'] = pair_found

    return attempt_dict


def add_attempt(db, letter, attempt):
    db[letter]['intentos'].update(attempt)


def add_letter(db, letter_dict):
    db.update(letter_dict)


def update_history(rows, columns):
    db = read_file()

    db_keys = list(db.keys())

    start_datetime = db[db_keys[0]]['fechahora_apertura']

    db_last_letter_attempts = db[db_keys[-1]]['intentos']
    last_letter_attempts_keys = list(db_last_letter_attempts.keys())

    end_datetime = db_last_letter_attempts[last_letter_attempts_keys[-2]]['fechahora_jugada']

    attempts_count = 0
    for values in db.values():
        attempts_count += len(values['intentos'])

    game_duration = subtract_dates(start_datetime, end_datetime)

    boxes = rows * columns
    points = calc_points(boxes, game_duration)

    with open('./database/historico.csv', 'a') as history_file:
        data = f'{end_datetime},{rows},{columns},{attempts_count},{game_duration},{points}\n'
        history_file.write(data)


def time_to_seconds(str_datetime):
    datetime = dt.strptime(str_datetime, current_date_format)

    seconds = (60 * ((datetime.hour * 60) + datetime.minute)) + datetime.second

    return seconds


def subtract_dates(start_datetime, end_datetime):
    start_datetime_seconds = time_to_seconds(start_datetime)
    end_datetime_seconds = time_to_seconds(end_datetime)

    dates_subtract = end_datetime_seconds - start_datetime_seconds

    return dates_subtract


def calc_points(boxes, game_duration):
    points = boxes * game_duration

    return points
