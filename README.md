# Predict-New-Medicines-using-DNA-Encoded-Libraries

The objective of this capstone project is to enhance small molecule binding prediction by utilizing machine learning (ML) techniques to explore a vast chemical space for potential drug candidates. Traditional drug discovery methods involve synthesizing small molecules individually and testing their interactions with specific protein targets. Given the estimated 10^60 potential drug-like compounds and the FDA's approval of only around 2,000 novel molecular entities, a more efficient approach is crucial. This project utilizes the Big Encoded Library for Chemical Assessment (BELKA), which contains data on approximately 133 million small molecules tested for binding to three protein targets using DNA-encoded chemical library (DEL) technology. In this project, we will develop predictive models to estimate the binding affinity of unknown chemical compounds to specified protein targets. Our approach will leverage the provided training data, while also exploring alternative methods for predicting small molecule binding without relying solely on empirical binding data. This will allow us to integrate various techniques to improve the accuracy and robustness of our predictions.

# How does the data look like?

- id - A unique example_id that we use to identify the molecule-binding target pair
- buildingblock1_smiles - The structure, in SMILES, of the first building block
- buildingblock2_smiles - The structure, in SMILES, of the second building block
- buildingblock3_smiles - The structure, in SMILES, of the third building block
- molecule_smiles - The structure of the fully assembled molecule, in SMILES. This includes the three building blocks and the triazine core
- protein_name - The protein target names includes (BRD4, HSA and sEH) 
- binds - The target column. A binary class label of whether the small  molecule binds to the protein.

![image](https://github.com/user-attachments/assets/fec46c08-3808-4b28-b66b-cea2a340c6d9)


Each SMILE molecule has been duplicated three times to evaluate its interactions with three distinct proteins: HSA, BRD4, and sEH.


The distribution of smiles that binds with different protein names (BRD4, HSA, sEH) are: 
![train_viz](https://github.com/user-attachments/assets/d3b48540-2be1-4190-8e41-8ead33a2300e)

It provides insights into the unique and overlapping positive interactions among the proteins.

The BELKA dataset i.e; **Data Source** can be found here -> [BELKA Dataset](https://www.kaggle.com/competitions/leash-BELKA/data?select=train.csv)

# Project Architecture

![workflow](https://github.com/user-attachments/assets/e69bb8e0-9461-415d-b8a8-d20720fd3ba2)

The workflow begins with loading raw Parquet files into Google Cloud Storage, followed by preprocessing tasks like deduplication, encoding (Morgan fingerprints, ECFP), and transforming data from long to wide formats. EDA is performed to generate molecular descriptors, compute a correlation matrix, and prepare features for model training.
Machine learning models (e.g., Logistic Regression, Random Forest, CatBoost, XGBoost) are trained, and the best-performing model is deployed via an artifact registry, served through FastAPI and Streamlit for user interaction.

