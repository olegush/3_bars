import json
import os.path
import sys


def load_data(filepath, error_file, error_json):
    if os.path.exists(filepath):
        with open(filepath, 'rb') as file:
            try:
                data_json = json.loads(file.read())
            except ValueError:
                return error_json
            else:
                return data_json
    else:
        return error_file


def check_coordinates(longitude, latitude):
    try:
        user_longitude = float(input(longitude))
        user_latitude = float(input(latitude))
        return user_longitude, user_latitude
    except NameError:
        print(NameError)


def calc_distance(bar, user_longitude, user_latitude):
    bar_longitude = bar['geometry']['coordinates'][0]
    bar_latitude = bar['geometry']['coordinates'][1]
    return ((bar_longitude - user_longitude) ** 2 +
            (bar_latitude - user_latitude) ** 2) ** 0.5


def get_bar(bars_list, mode, coordinates):
    if mode == 'biggest':
        return max(bars_list, key=lambda bar:
                   bar['properties']['Attributes']['SeatsCount'])
    if mode == 'smallest':
        return min(bars_list, key=lambda bar:
                   bar['properties']['Attributes']['SeatsCount'])
    if mode == 'closest':
        return min(bars_list, key=lambda bar:
                   calc_distance(bar, coordinates[0], coordinates[1]))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        user_filepath = sys.argv[1]
        if os.path.exists(user_filepath):
            bars_dict = load_data('bars.json', "file does not exists",
                                  "json data does not exists or incorrect")
            bars_list = bars_dict['features']
            biggest_bar = get_bar(bars_list, 'biggest', None)
            print('The biggest bar: {} '
                  .format(biggest_bar['properties']['Attributes']['Name']
                          .encode("UTF-8")))
            smallest_bar = get_bar(bars_list, 'smallest', None)
            print('The smallest bar: {} '
                  .format(smallest_bar['properties']['Attributes']['Name']
                          .encode("UTF-8")))
            user_coordinates = check_coordinates("Your longitude:",
                                                 "Your latitude:")
            if user_coordinates:
                closest_bar = get_bar(bars_list, 'closest', user_coordinates)
                print('The closest bar: {} '
                      .format(closest_bar['properties']['Attributes']['Name']
                              .encode("UTF-8")))
        else:
            print('need correct file path')
    else:
        print('need filename')
