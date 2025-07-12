# Data Processing Workflow

This document outlines the steps taken to process and prepare the dataset for machine learning modeling.

## Steps:

1. **Download Data from Google Cloud Storage (GCS):**
   - The dataset was downloaded from GCS to the local environment for processing.

2. **Dataset Undersampling:**
   - The dataset was undersampled to maintain a 2:1 ratio of binding values (`0s` to `1s`).

3. **Long to Wide Format Conversion:**
   - Each SMILES molecule is repeated twice to understand interactions with three proteins: HSA, BRD4, and sEH.
   - The dataset was converted from long format to wide format to save space:
     - Long format: **1.4 GB**
     - Wide format: **460 MB**
   - This process helped us save memory by 45%

4. **Preprocessing in Wide Format:**
   - To save computation time, Morgan fingerprinting analysis was applied to each SMILES molecule only once in the wide format (instead of three times in the long format).

5. **Reconversion to Long Format:**
   - The processed dataset was converted back to long format for machine learning modeling.
   - One-hot encoding was applied to the protein names.

6. **Dataset Splitting:**
   - The dataset was split into the following subsets:
     - `X_train`
     - `X_val`
     - `y_train`
     - `y_val`
   - The split utilized EFCP features, encoded protein names, and binding values.

7. **Saving Processed Data:**
   - The processed subsets were saved as pickle files in the GCS artifacts folder for downstream tasks.

