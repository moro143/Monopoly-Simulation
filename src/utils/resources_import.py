import csv
import os.path


def board_tiles(filename='/src/resources/board_tiles.csv'):
    """_summary_

    :param filename: _description_, defaults to '/src/resources/board_tiles.csv'
    :type filename: str, optional
    :return: _description_
    :rtype: _type_
    """
    result = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        keys = csv_reader.__next__()

        for row in csv_reader:
            tile = {}
            for i, key in enumerate(keys):
                tile[key] = row[i]
            result.append(tile)
    return result
