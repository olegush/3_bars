import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.loads(file.read())


def check_coordinates(longitude, latitude):
    try:
        user_longitude = float(input(longitude))
        user_latitude = float(input(latitude))
        return user_longitude, user_latitude
    except Exception as e:
        print("type error: " + str(e))


def calc_distance(bar, user_coordinates):
    bar_longitude = bar['geometry']['coordinates'][0]
    bar_latitude = bar['geometry']['coordinates'][1]
    return ((bar_longitude - user_coordinates[0]) ** 2 +
            (bar_latitude - user_coordinates[1]) ** 2) ** 0.5


def get_bar(bar_item):
    return bar_item['properties']['Attributes']['Name']


def get_biggest_bar(bars_list):
    return max(bars_list,
               key=lambda bar: bar['properties']['Attributes']['SeatsCount']
               )


def get_smallest_bar(bars_list):
    return min(bars_list,
               key=lambda bar: bar['properties']['Attributes']['SeatsCount']
               )


def get_closest_bar(bars_list, user_coordinates):
    return min(bars_list, key=lambda bar: calc_distance(bar, user_coordinates))


if __name__ == '__main__':
    try:
        bars_list = load_data(sys.argv[1])['features']
    except IndexError:
        print('No script parameter (path to json file)')
    except IOError:
        print('No such file or directory')
    else:
        print('The biggest bar:')
        print(get_bar(get_biggest_bar(bars_list)))
        print('The smallest bar:')
        print(get_bar(get_smallest_bar(bars_list)))
        user_coordinates = check_coordinates("Your longitude:",
                                             "Your latitude:")
        if user_coordinates:
            closest_bar = get_closest_bar(bars_list, user_coordinates)
            print('The closest bar:')
            print(get_bar(closest_bar))
