import json
import os.path


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'rb') as file:
            try:
                data_json = json.loads(file.read())
            except ValueError:
                return "json data does not exists or incorrect"
            else:
                return data_json
    else:
        return "file does not exists"


def get_biggest_bar(data_bars):
    biggest_bar = max(data_bars, key=lambda bar:
                      bar['properties']['Attributes']['SeatsCount'])
    biggest_bar_name = biggest_bar['properties']['Attributes']['Name']
    return biggest_bar_name


def get_smallest_bar(data_bars):
    smallest_bar = min(data_bars, key=lambda bar:
                       bar['properties']['Attributes']['SeatsCount'])
    smallest_bar_name_min = smallest_bar['properties']['Attributes']['Name']
    return smallest_bar_name_min


def calc_distance(bar):
    bar_longitude = bar['geometry']['coordinates'][0]
    bar_latitude = bar['geometry']['coordinates'][1]
    return ((bar_longitude - user_longitude) ** 2 +
            (bar_latitude - user_latitude) ** 2) ** 0.5


def get_closest_bar(data_bars, user_longitude, user_latitude):
    closest_bar = min(data_bars, key=lambda bar: calc_distance(bar))
    closest_bar_name = closest_bar['properties']['Attributes']['Name']
    return closest_bar_name


if __name__ == '__main__':
    bars_dict = load_data('bars.json')
    bars_list = bars_dict['features']
    print('The biggest bar: ' + get_biggest_bar(bars_list))
    print('The smallest bar: ' + get_smallest_bar(bars_list))
    while True:
        try:
            user_longitude = float(input("Your longitude: "))
            user_latitude = float(input('Your latitude:'))
            print('The closest bar: '
                  + get_closest_bar(bars_list, user_longitude, user_latitude))
            break
        except NameError:
            print('Incorrect coordinates!')
        except ValueError:
            print('Incorrect coordinates!')
        except TypeError:
            print('Incorrect coordinates!')
