import json


def load_data(filepath):
    openfile = open(filepath, 'rb')
    return json.loads(openfile.read())


def get_biggest_bar(data_bars):
    biggest_bar = max(data_bars, key=lambda bar:
                      bar['properties']['Attributes']['SeatsCount'])
    biggest_bar_name = biggest_bar['properties']['Attributes']['Name']
    biggest_bar_name_seats = \
        biggest_bar['properties']['Attributes']['SeatsCount']
    return 'The biggest bar: ' \
           + biggest_bar_name + ', ' \
           + str(biggest_bar_name_seats) + ' seats'


def get_smallest_bar(data_bars):
    smallest_bar_without_zero = \
        filter(lambda bar: bar['properties']['Attributes']['SeatsCount'] > 0,
               data_bars)
    smallest_bar = min(smallest_bar_without_zero, key=lambda bar:
                       bar['properties']['Attributes']['SeatsCount'])
    smallest_bar_name_min = smallest_bar['properties']['Attributes']['Name']
    smallest_bar_seats = smallest_bar['properties']['Attributes']['SeatsCount']
    return 'The smallest bar: ' + \
           smallest_bar_name_min + ', ' + str(smallest_bar_seats) + ' seats'


def get_closest_bar(data_bars, user_longitude, user_latitude):
    def calc_distance(bar):
        bar_longitude = bar['geometry']['coordinates'][0]
        bar_latitude = bar['geometry']['coordinates'][1]
        return ((bar_longitude - user_longitude) ** 2 +
                (bar_latitude - user_latitude) ** 2) ** 0.5
    closest_bar = min(data_bars, key=lambda bar: calc_distance(bar))
    closest_bar_name = closest_bar['properties']['Attributes']['Name']
    return 'The closest bar: ' + closest_bar_name


if __name__ == '__main__':
    bars_dict = load_data('bars.json')
    bars_list = bars_dict['features']
    print(get_biggest_bar(bars_list))
    print(get_smallest_bar(bars_list))
    user_longitude = input('Your longitude:')
    user_latitude = input('Your latitude:')
    print(get_closest_bar(bars_list,
                          float(user_longitude), float(user_latitude)))
