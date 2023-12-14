import json
import pandas as pd
import os

#tabella metilazione: CASE_ID
#1
...
#27.000

path_table = "c:/Users/utente/Desktop/BIO_Project/met_table.tsv"
path = "c:/Users/utente/Desktop/BIO_Project/files_2023-12-14-met.json"
with open(path, 'r') as f:
  met_json = json.load(f)

case_id_list = [] #lista case_id univoci

for dict in met_json:
  case_id_list.append(dict["cases"][0]["case_id"])

case_id_list=list(set(case_id_list))
met_table = pd.DataFrame()


for case_id in case_id_list:
  for i in range(len(met_json)):
    if (met_json[i]["cases"][0]["case_id"] == case_id): 
      filename = met_json[i]["file_name"]
      if os.path.isfile("c:/Users/utente/Desktop/BIO_Project/mRNA_Data/" + filename):
        df = pd.read_csv("c:/Users/utente/Desktop/BIO_Project/Met_Data/" + filename, header=None, delimiter='\t')
        met_table[case_id] = df.iloc[:,1]

print(met_table)
met_table.to_csv(path_table, sep='\t', index=False)

