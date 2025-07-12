# Predictive-Modeling-with-BELKA-Chemical-Libraries

The goal of this capstone project is to improve small molecule binding prediction by applying machine learning (ML) methods to navigate the immense chemical space and identify promising drug candidates. Traditional drug discovery relies on individually synthesizing and testing small molecules against protein targets — a slow process, especially given the estimated 10^60 drug-like compounds compared to only ~2,000 FDA-approved novel molecules. This project leverages the Big Encoded Library for Chemical Assessment (BELKA), which includes data on ~133 million small molecules screened against three protein targets using DNA-encoded chemical library (DEL) technology. We aim to build predictive models that estimate the binding affinity of unseen compounds to protein targets, using the provided training data and exploring additional modeling strategies beyond purely empirical binding data. By combining multiple approaches, we seek to enhance predicti

# 📄 What Does the Data Look Like?

- **id** — A unique identifier for each molecule–protein target pair.  
- **buildingblock1_smiles** — SMILES string representing the first chemical building block.  
- **buildingblock2_smiles** — SMILES string for the second building block.  
- **buildingblock3_smiles** — SMILES string for the third building block.  
- **molecule_smiles** — SMILES string of the complete molecule, combining the three building blocks and the triazine core.  
- **protein_name** — Name of the target protein (e.g., BRD4, HSA, sEH).  
- **binds** — The binary label indicating whether the molecule binds to the protein target.

![image](https://github.com/user-attachments/assets/fec46c08-3808-4b28-b66b-cea2a340c6d9)


Each SMILES molecule is represented three times to assess its binding interactions with three different protein targets: HSA, BRD4, and sEH.

The distribution of SMILES molecules that bind to each protein (BRD4, HSA, sEH) is as follows:
![train_viz](https://github.com/user-attachments/assets/d3b48540-2be1-4190-8e41-8ead33a2300e)

It offers insights into both the unique and shared positive binding interactions across the different protein targets.

The BELKA dataset (**Data Source**) is available here → [BELKA Dataset](https://www.kaggle.com/competitions/leash-BELKA/data?select=train.csv)

# Project Architecture

![workflow](https://github.com/user-attachments/assets/e69bb8e0-9461-415d-b8a8-d20720fd3ba2)

The workflow starts by loading raw Parquet files into Google Cloud Storage, followed by preprocessing steps such as deduplication, molecular encoding (using Morgan fingerprints, ECFP), and reshaping the data from long to wide format. Exploratory Data Analysis (EDA) is conducted to generate molecular descriptors, build a correlation matrix, and prepare the feature set for model training.

Various machine learning models—including Logistic Regression, Random Forest, CatBoost, and XGBoost—are trained, with the best-performing model saved to an artifact registry. This model is then deployed using FastAPI and integrated with Streamlit to enable user-friendly interaction.
