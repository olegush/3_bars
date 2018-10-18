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
    except NameError:
        print(NameError)


def calc_distance(bar, user_coordinates):
    bar_longitude = bar['geometry']['coordinates'][0]
    bar_latitude = bar['geometry']['coordinates'][1]
    return ((bar_longitude - user_coordinates[0]) ** 2 +
            (bar_latitude - user_coordinates[1]) ** 2) ** 0.5


def get_bar(bars_list, index):
    return bars_list[index]['properties']['Attributes']['Name']


if __name__ == '__main__':
    try:
        bars_list = load_data(sys.argv[1])['features']
        biggest_bar_index = bars_list.index(
            max(bars_list,
                key=lambda bar:
                bar['properties']['Attributes']['SeatsCount'])
        )
        print(u'The biggest bar: {}'.format(
            get_bar(bars_list, biggest_bar_index))
        )
        smallest_bar_index = bars_list.index(
            min(bars_list,
                key=lambda bar:
                bar['properties']['Attributes']['SeatsCount'])
        )
        print(u'The smallest bar: {} '.format(
            get_bar(bars_list, smallest_bar_index))
        )
        user_coordinates = check_coordinates("Your longitude:",
                                             "Your latitude:")
        if user_coordinates:
            closest_bar_item = min(bars_list,
                                   key=lambda bar:
                                   calc_distance(bar, user_coordinates))
            closest_bar_index = bars_list.index(closest_bar_item)
            print(u'The closest bar: {} '
                  .format(get_bar(bars_list, closest_bar_index)))
    except IndexError:
        print('No script parameter (path to json file)')
    except IOError:
        print('No such file or directory')
