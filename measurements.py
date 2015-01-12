from speedtest import speedtest_cli
import cPickle as pickle
from scraper import pickle_data
import pprint
from sys import argv
import datetime


def main():
    output = speedtest_cli.speedtest()
    dlspeed = output['download']
    ulspeed = output['upload']
    output['upload'] = speed_in_Mbits(ulspeed)
    output['download'] = speed_in_Mbits(dlspeed) 
    #pprint.pprint(output)
    time = datetime.datetime.now()
    pfile = output['ip'] + "_hour_" + str(time.hour) + "_min_" + str(time.minute)
    pickle = pickle_data(pfile, output)


def speed_in_Mbits(speed):
    speed = round((speed / 1000 / 1000) * 8, 2)
    return speed


if __name__ == '__main__':
    main()
