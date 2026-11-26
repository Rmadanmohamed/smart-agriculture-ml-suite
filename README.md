# Smart Agriculture ML Suite

## Overview and problem statement

A graduation-project suite of agricultural modeling notebooks for crop selection, production/yield estimation, soil analysis, explainability, weather time-series forecasting and plant image classification. Intended as a set of research experiments, not an operational farm advisory service.

## Technology stack and prerequisites

Python 3 and a notebook runtime are required (exact version unspecified). [requirements.txt](requirements.txt) declares keras, lightgbm, matplotlib, numpy, opencv-python, pandas, plotly, scikit-learn, seaborn, tensorflow, torch, torchvision, xgboost; all versions are unpinned. Additional notebook dependencies not listed directly: scipy, statsmodels, pmdarima, tqdm, pillow, kagglehub, skimpy, shap, lime, lazypredict. Local Jupyter must be installed separately. No exact dependency lock is available.

## Project structure

- [agriculture-modeling-pipeline.ipynb](notebooks/agriculture-modeling-pipeline.ipynb) — experiment source.
- [agriculture-visualizations.ipynb](notebooks/agriculture-visualizations.ipynb) — experiment source.
- [crop-recommendation-testing-final.ipynb](notebooks/crop-recommendation-testing-final.ipynb) — experiment source.
- [crop-yield-prediction-model.ipynb](notebooks/crop-yield-prediction-model.ipynb) — experiment source.
- [crop-yield-time-series-prediction.ipynb](notebooks/crop-yield-time-series-prediction.ipynb) — experiment source.
- [plant-disease-classification-pytorch-vgg.ipynb](notebooks/plant-disease-classification-pytorch-vgg.ipynb) — experiment source.
- [plant-disease-cnn-vgg-resnet-comparison.ipynb](notebooks/plant-disease-cnn-vgg-resnet-comparison.ipynb) — experiment source.
- [soil-nutrient-xai-classification.ipynb](notebooks/soil-nutrient-xai-classification.ipynb) — experiment source.
- [soil-nutrients-crop-yield-prediction.ipynb](notebooks/soil-nutrients-crop-yield-prediction.ipynb) — experiment source.
- [sustainable-agriculture-random-forest-analysis.ipynb](notebooks/sustainable-agriculture-random-forest-analysis.ipynb) — experiment source.
- [requirements.txt](requirements.txt) — dependencies.
- [LICENSE](LICENSE) — repository license, separate from dataset rights.

## Dataset and preprocessing

External CSVs include `Crop_recommendation.csv`, `crop_production.csv`, `Soil Nutrients.csv`, `Agri_model_cleaned.csv`, `Agri_yield_prediction_30k_realistic.csv`, `prcp.csv`, and Kaggle farmer/market datasets. Other notebooks use image folders and notebook-specific file paths. Data is not bundled; confirm exact schemas, data source, and licensing in the original data environment. Crop recommendation inputs include N, P, K, temperature, humidity, pH, rainfall and target `Crop`. Yield workflows use `Yield`, `Production` or `Crop_Yield_ton` depending on the notebook.

## Models and workflow

Crop recommendation uses one-hot targets with multi-output classifiers (75/25 split, seed 0); production regression uses linear regression, random forest, SVR and decision tree (75/25, seed 5). Time series includes SARIMAX, auto-ARIMA and Keras LSTM. Plant disease notebooks use PyTorch VGG16 and TensorFlow CNN/transfer learning (including VGG16 and ResNet50); the TensorFlow notebook uses 224x224 image loading and ImageNet weights in its VGG section. Soil notebooks use PCA, LazyClassifier, gradient boosting, random forest and XGBoost, with SHAP/LIME explainability. The sustainable agriculture notebook fits random forest regression (30 trees, depth 7, 80/20 split, seed 42).

## Installation and execution

```bash
git clone https://github.com/Rmadanmohamed/smart-agriculture-ml-suite.git
cd smart-agriculture-ml-suite
python -m venv .venv
```

Activate with `source .venv/bin/activate` (Linux/macOS) or `.venv\Scripts\Activate.ps1` (Windows PowerShell).

```bash
python -m pip install -r requirements.txt
python -m pip install jupyter scipy statsmodels pmdarima tqdm pillow kagglehub skimpy shap lime lazypredict
jupyter notebook notebooks/crop-recommendation-testing-final.ipynb
```

Alternatively, use Google Colab or Kaggle where applicable. For local execution, adjust environment-specific file paths in a local working copy. Install optional notebook-specific packages only for experiments that use them. Exact compatible versions and end-to-end execution have not been verified.

## Environment variables

No application environment-variable configuration was identified in the reviewed notebook sections. Dataset paths and model settings are configured in cells. If downloading data from a restricted source, use that provider's authorized access method rather than embedding credentials.

## Usage, evaluation and limitations

Choose a notebook by task, supply its external data and run its relevant cells. The notebooks contain classification reports, accuracy, confusion matrices, R², MAE/MSE/RMSE and feature-importance plots depending on the experiment. No saved numeric outputs were found in the reviewed cells; the previous README's >97% statement is not a verified held-out result. Notebook-specific dependencies, legacy APIs and paths can prevent a clean run. Use a GPU optionally for image training and ensure compatible TensorFlow/PyTorch builds. Verify dataset provenance, independent evaluation and regional applicability before farm decisions.

## Testing and validation

No automated test suite is included. Execute the relevant notebook with its required data and inspect generated results. Training and tests were not executed during this documentation audit.

## Screenshots and demo

No standalone screenshots or verified live demo were found. Generate charts and circuit/model visualizations by executing relevant notebooks.

## Author

**Ramadan Mohamed Hassan** — AI Engineer | AI Researcher | AI Automation | LLM & RAG Systems | Machine Learning

[Portfolio](https://ramadan-ai-portfolio.vercel.app/) · [LinkedIn](https://www.linkedin.com/in/ramadan-mohamed-89085a366/) · [GitHub](https://github.com/Rmadanmohamed) · [Email](mailto:ramadanmohameddd3@gmail.com)

## Remediation validation

Corrects undefined scaler and eliminates fitting on test data in the crop-yield notebook. Other agricultural experiments need their original datasets and further leakage review.

Run the scoped synthetic check with `python tests/regression.py` after installing its CI dependencies. Prior notebook outputs were cleared because they predate the correction.
