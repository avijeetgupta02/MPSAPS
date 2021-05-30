#!/usr/bin/env python

import sys
import csv
import json
from pprint import pprint

state_list = ['AN', 'AP', 'AR', 'AS', 'BR', 'CH', 'CT',
              'DD', 'DL', 'DN', 'GA', 'GJ', 'HP', 'HR',
              'JH', 'JK', 'KA', 'KL', 'LD', 'MH', 'ML',
              'MN', 'MP', 'MZ', 'NL', 'OR', 'PB', 'PY',
              'RJ', 'SK', 'TN', 'TR', 'UP', 'UT', 'WB']


state_code_dict = {'Andaman & Nicobar': 'AN', 'Andhra Pradesh': 'AP',
                   'Arunachal Pradesh': 'AR', 'Assam': 'AS',
                   'Bihar': 'BR', 'Chandigarh': 'CH',
                   'Chhatisgarh': 'CT', 'Daman & Diu': 'DD',
                   'Dadra & Nagar Haveli': 'DN', 'Goa': 'GA', 'Gujarat': 'GJ',
                   'Himachal Pradesh': 'HP', 'Haryana': 'HR', 'Jharkhand': 'JH',
                   'Jammu & Kashmir': 'JK', 'Karnataka': 'KA', 'Kerala': 'KL',
                   'Lakshwadeep': 'LD', 'Maharashtra': 'MH', 'Meghalaya': 'ML',
                   'Manipur': 'MN', 'Madhya Pradesh': 'MP', 'Mizoram': 'MZ',
                   'Nagaland': 'NL', 'Odisha': 'OR', 'Punjab': 'PB',
                   'Puducherry': 'PY', 'Rajasthan': 'RJ', 'Sikkim': 'SK',
                   'Tamil Nadu': 'TN', 'Tripura': 'TR', 'Uttar Pradesh': 'UP',
                   'Uttarakhand': 'UT', 'West Bengal': 'WB'}


district_dir = '/home/sachin/Documents/GMU/Spring2015/Proposal/MyWork/Data/IndiaDistricts/'
state_code_dict_json = district_dir + 'state_code_dict.json'
state_dist_list_json = district_dir + 'state_dist_list_withcode.json'

state_dict = {}
state_dist_list = {}

lus_csv_data = []

for state_c in state_list:
    if state_c not in state_dist_list:
        state_dist_list[state_c] = []
        state_file = district_dir + state_c + '.csv'
        # print(state_file)
        with open(state_file, 'r') as fp_state:
            state_reader = csv.DictReader(fp_state)
            for state_row in state_reader:
                mydist_d = {'census_sc': state_row['StateCode']}
                mydist_d['census_dc'] = state_row['DistCode']
                mydist_d['state'] = state_row['State']
                mydist_d['district'] = ' '.join(state_row['District'].split())

                state_dist_list[state_c].append(mydist_d)
# pprint(state_dist_list)

with open(state_dist_list_json, 'w') as json_fp:
    json.dump(state_dist_list, json_fp, sort_keys=True, indent=4,
              separators=(',', ': '))

with open(state_code_dict_json, 'w') as json_fp:
    json.dump(state_code_dict, json_fp, sort_keys=True, indent=4,
              separators=(',', ': '))

sys.exit(0)
