# Smart Agriculture ML Suite

## Overview
A graduation-project notebook suite for crop recommendation, crop yield prediction, soil nutrient analysis, XAI, and plant disease classification.

## Problem Statement
Sustainable farming decisions depend on crop, soil, disease, market, and yield signals that require both classical ML and deep learning workflows.

## Features
- Crop recommendation modeling
- Crop yield prediction
- Soil nutrient analysis with explainability
- Plant disease CNN/VGG/ResNet experiments
- Agriculture visualization notebooks

## Tech Stack
- Python
- Pandas
- Scikit-learn
- TensorFlow
- Keras
- PyTorch
- XGBoost
- LightGBM
- Plotly

## Dataset
- Crop_recommendation.csv
- crop_production.csv
- Soil Nutrients.csv
- Plant disease image datasets referenced from Kaggle/Colab

## Models / Algorithms
- Random Forest
- Decision Tree
- KNN
- SVM
- XGBoost
- LightGBM
- CNN
- VGG
- ResNet
- MobileNet
- LSTM

## Results
The notebooks include accuracy, R2, confusion-matrix, and feature-importance evaluation code. One plant-disease notebook reports over 97% accuracy in its markdown, but results should be rerun for verification.

## Project Structure
- notebooks/
  - agriculture-modeling-pipeline.ipynb
  - agriculture-visualizations.ipynb
  - crop-recommendation-testing-final.ipynb
  - crop-yield-prediction-model.ipynb
  - crop-yield-time-series-prediction.ipynb
  - plant-disease-classification-pytorch-vgg.ipynb
  - plant-disease-cnn-vgg-resnet-comparison.ipynb
  - soil-nutrient-xai-classification.ipynb
  - soil-nutrients-crop-yield-prediction.ipynb
  - sustainable-agriculture-random-forest-analysis.ipynb

## How to Run
- `pip install -r requirements.txt`
- `jupyter notebook notebooks/crop-recommendation-testing-final.ipynb`

## Screenshots / Demo
Screenshots or demo media can be added after deployment.

## Future Improvements
- Unify all agriculture notebooks into a single pipeline
- Add dataset cards and provenance links
- Connect trained models to AgriNova dashboard

## Author
Ramadan Mohamed Hassan
