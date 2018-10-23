import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.loads(file.read())


def check_coordinates(longitude, latitude):
    err = 'coordinate must be a float number'
    try:
        user_longitude = float(input(longitude))
        user_latitude = float(input(latitude))
        return user_longitude, user_latitude
    except ValueError:
        print(err)


def calc_distance(bar, user_coordinates):
    bar_longitude = bar['geometry']['coordinates'][0]
    bar_latitude = bar['geometry']['coordinates'][1]
    return ((bar_longitude - user_coordinates[0]) ** 2 +
            (bar_latitude - user_coordinates[1]) ** 2) ** 0.5


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


def get_bar_info_dict(bar_item, bar_info):
    for key, value in bar_item.items():
        if not isinstance(value, dict):
            bar_info[key] = value
        else:
            get_bar_info_dict(value, bar_info)
    return bar_info


if __name__ == '__main__':
    try:
        bars_data = load_data(sys.argv[1])
    except IndexError:
        exit('No script parameter (path to json file)')
    except IOError:
        exit('No such file or directory')
    except ValueError:
        exit('Not json data')
    bars_list = bars_data['features']
    biggest_bar = get_bar_info_dict(get_biggest_bar(bars_list), {})
    print('The biggest bar: {}'.format(biggest_bar['Name']))
    smallest_bar = get_bar_info_dict(get_smallest_bar(bars_list), {})
    print('The smallest bar: {}'.format(smallest_bar['Name']))
    user_coordinates = check_coordinates('Your longitude:', 'Your latitude:')
    closest_bar = get_bar_info_dict(
        get_closest_bar(bars_list, user_coordinates), {}
    )
    print('The closest bar: {}'.format(closest_bar['Name']))
