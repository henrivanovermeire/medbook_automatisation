import pandas as pd
from medbook_processor import MedbookProcessor
import os

source_path = './source/source_file.csv'

cases = pd.read_csv(source_path)

def extract_date_of_birth_from_patient_number(patient_nr):
    date_of_birth = patient_nr[4]+patient_nr[5]+'-'+patient_nr[2]+patient_nr[3]+'-'+patient_nr[0]+patient_nr[1]
    return date_of_birth

medbook = MedbookProcessor()
print('####################')
print(' MEDBOOK PROCESSOR')
print('\n')
print("author: HVO")
print('####################')

theatre = input('Theatre (CXZXX)?> ')
cases = cases[cases['OP-Zaal'] == theatre]


for index, row in cases.iterrows():
    os.system('clear')
    procedure = row['Orderomschrijving']
    date_of_birth = extract_date_of_birth_from_patient_number(row['Patiëntennr'])
    print(f"Now uploading case for user: {os.environ['USER']}") 
    print(f"{procedure} - {date_of_birth}")
    medbook.upload_case(procedure=procedure, specialty='13', date_of_birth=date_of_birth)
    
medbook.driver.close()
