import scraper


chicago_zip_codes = [60007, 60018, 60068, 60106, 60131, 60176, 60601,
        60602, 60603, 60604, 60605, 60606, 60607, 60608, 60609, 60610,
        60611, 60612, 60613, 60614, 60615, 60616, 60617, 60618, 60619,
        60620, 60621, 60622, 60623, 60624, 60625, 60626, 60628, 60629,
        60630, 60631, 60632, 60633, 60634, 60636, 60637, 60638, 60639,
        60640, 60641, 60642, 60643, 60644, 60645, 60646, 60647, 60649,
        60651, 60652, 60653, 60654, 60655, 60656, 60657, 60659, 60660,
        60661, 60706, 60707, 60714, 60804, 60827]

chicago_area = 227.63


def main():
    scraper.unpickle_data('comcast.pkl')


def get_hotspots(data, chicago_zips):
    hotspots = []
    for dataset in data:
        for row in dataset:
            if int(row['zip']) in chicago_zip_codes:
                hotspots.append(row)
                break


def calculate_density(hotspots):
    density = len(hotspots) / chicago_area
    return density


if __name__ == '__main__':
    main()
