# ML Training Pipeline

This repository contains the code and instructions for a machine learning (ML) training pipeline designed to train multiple models, evaluate their performance, and deploy the best model based on the **Weighted Mean Average Precision (mAP)** metric to Google Artifact Registry for future predictions.

---

## Features

- Trains multiple ML models including:
  - Logistic Regression
  - Random Forest
  - Decision Tree
  - LightGBM
  - XGBoost
  - CatBoost
- Evaluates models using:
  - **Accuracy**
  - **ROC AUC**
  - **Weighted mAP**
  - **Classification Report**
- Automatically identifies and logs the best-performing model.
- Uploads trained models to Google Cloud Storage (GCS).
- Deploys the best model to Google Artifact Registry for serving and prediction.

---

## Prerequisites

### Tools and Libraries
- Python 3.7+
- Required Python packages:
  ```bash
  pip install -r requirements.txt
  ```
- Google Cloud CLI configured with:
  - **Vertex AI API** enabled
  - **Artifact Registry** enabled

### Google Cloud Setup
1. Authenticate with Google Cloud:
   ```bash
   gcloud auth login
   ```
2. Set your project and region:
   ```bash
   gcloud config set project <YOUR_PROJECT_ID>
   gcloud config set compute/region <YOUR_REGION>
   ```
3. Create a GCS bucket for storing models:
   ```bash
   gcloud storage buckets create gs://<YOUR_BUCKET_NAME>
   ```
4. Create an Artifact Registry repository:
   ```bash
   gcloud artifacts repositories create <YOUR_REPO_NAME> --repository-format=docker --location=us-central1
   ```

---

## Pipeline Overview


  **Model Training**:
   - Trains each model using the training set.
   - Calculates evaluation metrics using the validation set.

---

## Usage

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Configure Environment Variables
Set the following environment variables:
```bash
export PROJECT_ID=<YOUR_PROJECT_ID>
export REGION=<YOUR_REGION>
export BUCKET_NAME=<YOUR_BUCKET_NAME>
export ARTIFACT_REGISTRY=<YOUR_ARTIFACT_REGISTRY>
```


---

## Key Files

### `train_pipeline.py`
- Main script to train models, evaluate performance, and deploy the best model.

  
### `requirements.txt`
- List of required Python libraries.

---

## Results

- The best-performing model is uploaded to Google Artifact Registry and deployed to a Vertex AI Endpoint.
- Model metrics and artifacts are logged in GCS.
- Endpoint details are printed in the console for future predictions.

---

## Future Enhancements

- Add hyperparameter tuning using Vertex AI Hyperparameter Tuning.
- Enable support for additional ML frameworks (e.g., TensorFlow, PyTorch).
- Automate monitoring and retraining workflows using Vertex AI Pipelines.
