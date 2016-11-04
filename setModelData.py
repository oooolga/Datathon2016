from variables import *
import pandas as pd
import numpy as np
import pdb

def main(data_dir, station_file, demographic_file, real_estate_file, save_path):
	station_f = pd.read_csv('{}/{}'.format(data_dir, station_file))
	station_by_zipcode = {}

	zipcodes = station_f.zipcode.unique()

	for zipcode in zipcodes:
		station_by_zipcode[zipcode] = [row.abbr \
					for _,row in station_f[station_f.zipcode == zipcode].iterrows()]

	demo_f = pd.read_csv('{}/{}'.format(data_dir, demographic_file))
	real_f = pd.read_csv('{}/{}'.format(data_dir, real_estate_file))

	years = demo_f.year.unique()

	row_list = []
	for year in years:
		for month in range(1,13):
			for zipcode in zipcodes:
				time = '{}-{:02}'.format(year, month)

				for abbr in station_by_zipcode[zipcode]:
					demo_temp = demo_f[demo_f.zipcode == zipcode]
					demo_temp = demo_temp[demo_temp.year == year]
					if len(demo_temp):
						household = demo_temp.median_household_income.values[0]
						hs = demo_temp.some_hs.values[0]
						college = demo_temp.some_college.values[0]
						bach = demo_temp.bach_degree.values[0]
						grad = demo_temp.grad_degree.values[0]
						popu = demo_temp.totalpop.values[0]

					else:
						continue

					real_temp = real_f[real_f.zipcode == zipcode]
					if len(real_temp):
						home = real_temp[time].values[0]
					else:
						home = np.NaN

					row_list.append({'year': year, 'month': month, 'abbr': abbr, 
										 'household income': household, 'hs': hs,
										 'college': college, 'bach': bach, 'grad': grad,
										 'demography': popu, 'home value': home
										 })
	
		df = pd.DataFrame(row_list)
		df.to_csv('{}/data.csv'.format(save_path))
	return

if __name__ == '__main__':
	main(data_dir, station_file, demographic_file, real_estate_file, save_path)