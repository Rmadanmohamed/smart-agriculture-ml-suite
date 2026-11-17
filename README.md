# Smart Agriculture ML Suite

## Overview

A notebook-based machine-learning suite covering crop recommendation, crop-yield prediction, soil-nutrient analysis, explainability, and plant-disease classification experiments.

## Problem Statement

Agricultural decision support combines information about crops, soil conditions, disease indicators, and yield. This repository collects exploratory and modeling workflows for several of those tasks.

## Implemented Workflows

- Crop recommendation modeling
- Crop-yield prediction
- Soil-nutrient analysis and explainability experiments
- Plant-disease classification experiments using CNN/VGG/ResNet-family approaches
- Agriculture-focused visualization notebooks

This is a collection of notebook workflows rather than a single packaged end-to-end production pipeline.

## Technology

- Python, Pandas
- Scikit-learn
- TensorFlow / Keras
- PyTorch
- XGBoost, LightGBM
- Plotly

The presence of a library in the dependency stack does not imply that every model in the repository uses it.

## Data

The repository references Crop_recommendation.csv, crop_production.csv, Soil Nutrients.csv, and plant-disease image datasets referenced from Kaggle/Colab notebooks. Review each notebook for its specific source, preprocessing, and split. The repository does not yet provide a unified dataset card covering provenance, licensing, and exact versions for all experiments.

## Models and Evaluation

The notebooks include experiments with Random Forest, Decision Tree, KNN, SVM, XGBoost, LightGBM, CNN, VGG, ResNet, MobileNet, and LSTM methods.

Evaluation code includes accuracy, R², confusion matrices, and feature-importance visualizations. A plant-disease notebook contains a reported accuracy above 97%, but this result has not been independently reproduced as part of this repository audit. It is therefore not presented as a verified benchmark here.

## Project Structure

- notebooks/agriculture-modeling-pipeline.ipynb
- notebooks/agriculture-visualizations.ipynb
- notebooks/crop-recommendation-testing-final.ipynb
- notebooks/crop-yield-prediction-model.ipynb
- notebooks/crop-yield-time-series-prediction.ipynb
- notebooks/plant-disease-classification-pytorch-vgg.ipynb
- notebooks/plant-disease-cnn-vgg-resnet-comparison.ipynb
- notebooks/soil-nutrient-xai-classification.ipynb
- notebooks/soil-nutrients-crop-yield-prediction.ipynb
- notebooks/sustainable-agriculture-random-forest-analysis.ipynb

## Run

    pip install -r requirements.txt
    jupyter notebook notebooks/crop-recommendation-testing-final.ipynb

For reproducibility, run the notebook from a clean environment, record dataset versions, and preserve the original train/validation/test separation. Do not compare metrics across notebooks unless their datasets and evaluation protocols are comparable.

## Related Research

The broader AgriNova research project is described in this co-authored publication:

**Attiya, I., Badr, M., Bedeir, A., Mohamed, R., Mohamed, N., Saad, M., Tharwat, M., & Abdelgawad, N. (2026).** *An edge-cloud AI-robotics framework with blockchain-based validation for crop yield prediction and plant health monitoring.* **Internet of Things, 39**, Article 102025.  
[DOI](https://doi.org/10.1016/j.iot.2026.102025) · [Elsevier publisher page](https://www.sciencedirect.com/science/article/pii/S2542660526001551)

The publisher's contribution statement credits Ramadan Mohamed with **Writing – original draft, Visualization, Validation, and Data curation**. The paper is a co-authored research output. Its system-level claims should not be read as proof that every component is integrated into this notebook repository.

## Limitations and Next Steps

- Add dataset cards with source, license, version, and preprocessing details.
- Make train/validation/test splits explicit and check for leakage.
- Add clean, scriptable training and evaluation entry points.
- Re-run reported metrics from pinned dependencies and documented splits.
- Consolidate reusable workflows only where this does not obscure the original experiments.

## Author

Ramadan Mohamed Hassan  
GitHub: https://github.com/Rmadanmohamed
