# -*- coding: utf-8 -*-
import json


def load_data(filepath):
    f = open(filepath, 'rb')
    return json.loads(f.read())


def get_biggest_bar(data):
    item_max = max(data,key=lambda item:item['properties']['Attributes']['SeatsCount'])
    name_max = item_max['properties']['Attributes']['Name']
    seats_max = item_max['properties']['Attributes']['SeatsCount']
    return 'The biggest bar: ' + name_max + ', ' + str(seats_max) + ' seats'


def get_smallest_bar(data):
    data_0=filter(lambda item: item['properties']['Attributes']['SeatsCount']>0, data)
    item_min = min(data_0, key=lambda item: item['properties']['Attributes']['SeatsCount'])
    name_min = item_min['properties']['Attributes']['Name']
    seats_min = item_min['properties']['Attributes']['SeatsCount']
    return 'The smallest bar: ' + name_min + ', ' + str(seats_min) + ' seats'


def get_closest_bar(data, longitude, latitude):
    def x_f(item):
        long = item['geometry']['coordinates'][0]
        lat = item['geometry']['coordinates'][1]
        return ((long - longitude) ** 2 + (lat - latitude) ** 2) ** 0.5
    item_x = min(data,key=lambda item:x_f(item))
    item_x_name = item_x['properties']['Attributes']['Name']
    return 'The closest bar: ' + item_x_name


if __name__ == '__main__':
    data_r = load_data('bars.json')
    print(get_biggest_bar(data_r['features']))
    print(get_smallest_bar(data_r['features']))
    longitude = input('Your longitude:')
    latitude=input('Your latitude:')
    print(get_closest_bar(data_r['features'], float(longitude), float(latitude)))
