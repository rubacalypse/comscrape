import sqlite3
import cPickle as pickle
import pprint
from sys import argv


def main():
    cursors = map(connect_dataset, argv[1:])
    results = map(query_dataset, cursors)
    pretty_dictionary = map(make_dict, results)
    pickle_file = 'comcast.pkl'
    pkl_file = pickle_data(pickle_file, pretty_dictionary)


def connect_dataset(name):
    conn = sqlite3.connect(name)
    c = conn.cursor()
    return c


def query_dataset(cursor):
    cursor.execute('select latitude, longitude, town, county, postcode from sites')
    result = cursor.fetchall()
    return result


def make_dict(result):
    new_dict = [{'lat': lat, 'lon': lon, 'city': city, 'state': state,
        'zip': zip} for (lat, lon, city, state, zip) in result]
    return new_dict


def pickle_data(pfile, data):
    pickle_file = pfile
    output = open(pickle_file, 'wb')
    pickle.dump(data, output)
    output.close()
    return pickle_file


def unpickle_data(file):
    pickle_file = open(file, 'rb')
    data = pickle.load(pickle_file)
    pickle_file.close()
    return data


if __name__ == '__main__':
    main()
