import pandas as pd
import numpy as np
from rdkit.Chem import AllChem
from rdkit import Chem
from joblib import Parallel, delayed
import pandas as pd
from tqdm import tqdm
from sklearn.preprocessing import OneHotEncoder
import requests
import json

# Define the function for parallel processing
def smiles_to_mol(smiles):
    return Chem.MolFromSmiles(smiles)

def generate_ecfp(molecule, radius=2, bits=1024):
    if molecule is None:
        return None
    return list(AllChem.GetMorganFingerprintAsBitVect(molecule, radius=radius, nBits=bits))

def predictbind(df):
   df['molecule'] = Parallel(n_jobs=-1)(delayed(smiles_to_mol)(smiles) for smiles in df['molecule_smiles'])
   df['ecfp'] = Parallel(n_jobs=-1)(delayed(generate_ecfp)(mol) for mol in tqdm(df['molecule']))   
   onehot_encoder = OneHotEncoder(sparse_output=False) 
   protein_onehot  = onehot_encoder.fit_transform(df['protein_names'].values.reshape(-1, 1))
   protein_onehot_list = protein_onehot.tolist()
   df['protein_onehot'] = protein_onehot_list
   api_url = "http://127.0.0.1:8000/predict"
   api_responses = []
   for index, row in df.iterrows():
        ecfp = row['ecfp']  
        protein_onehot = row['protein_onehot'] 
        
        data = {
            'encoded_smiles': ecfp,  
            'encoded_protein': protein_onehot  
        }
        response = requests.post(api_url, json=data)
        if response.status_code == 200:
            print(f"Request for index {index} was successful.")
            api_responses.append(response.json())  
        else:
            print(f"Request for index {index} failed. Status code: {response.status_code}")
            api_responses.append(None) 
   df["prediction"] = [response['prediction'] for response in api_responses]
   df["label"] = df["prediction"].apply(lambda x: "Does not bind" if x == 0 else "Binds")
   res_df = df.drop(["ecfp", "molecule", "protein_onehot"], axis=1)
   return res_df


# data = pd.read_csv("sampled_data.csv")
# res = predictbind(data)
# print(res[["binds","prediction"]])


