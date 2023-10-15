# PP00015_MLOps_End-to-End-ML-Application-Project_MLflow
This project is an application of MLops principles 

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py


## How to run the project

### STEPS:

Clone the repository

```bash
https://github.com/soyinkas1/PP00015_MLOps_End-to-End-ML-Application-Project_MLflow
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.9 -y
```

```bash
conda activate mlproj
```

### STEP 02 - install the requirements

```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

```bash
open up your local host and port 
```

## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)

##### cmd
- mlflow ui

## dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI = https://dagshub.com/soyinkas1/PP00015_MLOps_End-to-End-ML-Application-Project_MLflow.mlflow \
MLFLOW_TRACKING_USERNAME = soyinkas1 \
MLFLOW_TRACKING_PASSWORD = 064e0bf4875a7186f622763f3cff47a14ab0f2a6 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URL=https://dagshub.com/soyinkas1/PP00015_MLOps_End-to-End-ML-Application-Project_MLflow.mlflow
export MLFLOW_TRACKING_USERNAME=soyinkas1
export MLFLOW_TRACKING_PASSWORD=064e0bf4875a7186f622763f3cff47a14ab0f2a6
```

