import json
import pandas as pd
import os

path_table = "c:/Users/utente/Desktop/Multimodal-Data-Integration-for-OVCA-Survival-Prediction/mRNA_table.tsv"
path = "c:/Users/utente/Desktop/Multimodal-Data-Integration-for-OVCA-Survival-Prediction/files_2023-12-14-mRNA.json"
with open(path, 'r') as f:
  met_json = json.load(f)

case_id_list = [] #lista case_id univoci

for dict in met_json:
  case_id_list.append(dict["cases"][0]["case_id"])

case_id_list=list(set(case_id_list))
mRNA_table = pd.DataFrame()

for case_id in case_id_list:
  for i in range(len(met_json)):
    if (met_json[i]["cases"][0]["case_id"] == case_id): 
      filename = met_json[i]["file_name"]
      if os.path.isfile("c:/Users/utente/Desktop/Multimodal-Data-Integration-for-OVCA-Survival-Prediction/mRNA_Data/" + filename):
        df = pd.read_csv("c:/Users/utente/Desktop/Multimodal-Data-Integration-for-OVCA-Survival-Prediction/mRNA_Data/" + filename, delimiter='\t', skiprows=[0, 2, 3, 4, 5])
        mRNA_table[case_id] = df['fpkm_uq_unstranded']
      else:
        continue

print(mRNA_table)
print(len(case_id_list))
mRNA_table.to_csv(path_table, sep='\t', index=False)