#!/usr/bin/env python3

import zipfile
import glob
import os
'''
1. Read list of Zip files under ./SOAP directory
2. Extract store number from each filename and creates directory based on store_number
3. Unzip the SOAP cert from zip file to directory created in Step 2
'''

# TODO : read all zipfiles under SOAP directory
zip_files = glob.glob('./certs/802/*.zip')
print(zip_files)

for file in zip_files:
    base_name = os.path.basename(file)
    sliced_file_name = base_name.split('.')
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall('./certs/802/{}'.format(sliced_file_name[0]))

# To extract zipfile into a directory
# for store in stores_list:
#     #TODO Check if folder exists already
#     print('./SOAP/_.{}.lowes.com.zip'.format(store))
#     with zipfile.ZipFile('./SOAP/_.{}.lowes.com.zip'.format(store), 'r') as zip_ref:
#         zip_ref.extractall('./SOAP/{}'.format(store))


