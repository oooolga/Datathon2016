__author__ = 'Ge Ya (Olga) Xu'

from variables import *
from os.path import isfile
import pandas as pd

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


			
def aggregate(process_path, stn_name='FRMT'):
	from glob import glob
	files = glob('{}/{}*.csv'.format(process_path, stn_name))
	with open('{}/{}_aggregate.csv'.format(process_path, stn_name), 'w') as f_temp:
		for f in files:
			try:
				demo_f = pd.read_csv(f, header=None)
				days = demo_f[0].unique()
				for day in days:
					temp_demo = demo_f[demo_f[0] == day]
					
					f_temp.write('{},{},{}\n'.format(day,f.split('_')[2], sum(temp_demo[2])))
			except:
				pass

		print 'Write to {}/{}_aggregate.csv'.format(process_path, stn_name)

if __name__ == '__main__':
	#main(ridership_csv_path, save_path)
	from glob import glob
	files = glob('{}/{}*.csv'.format(save_path, 'FRMT'))

	for f in files:
		t = f.split('_')[2]
		aggregate(save_path, t)