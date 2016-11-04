__author__ = 'Ge Ya (Olga) Xu'

from variables import *
from os.path import isfile


def main(file_path, save_path, num_lines=48763195):

	with open(file_path) as f:

		line = f.readline()
		counter = 1

		while True:
			line = f.readline().split(',')

			if not line:
				break

			if counter % 10000 == 0:
				print 'finished processing: {}/{}'.format(counter, num_lines)

			counter += 1

			stn_file = '{}/{}_{}_ridership.csv'.format(save_path, line[2], line[3])

			with open(stn_file, 'ab') as stn_f:
				stn_f.write('{},{},{},{}'.format(line[0], line[1], line[4], line[6]))


			


if __name__ == '__main__':
	main(ridership_csv_path, save_path)