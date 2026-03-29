# Airbnb Price Prediction

Predict Airbnb listing prices using public listings data.  
This project includes 
**data cleaning**, 
**feature engineering**, 
**model training**, and a
**Streamlit interactive app**.

---

## Project Structure


airbnb-price-prediction/
├─ app/
│ └─ app.py # Streamlit frontend
├─ src/
│ ├─ data_cleaning.py # Data cleaning
│ ├─ feature_engineering.py
│ └─ train.py # Model training
├─ data/
│ ├─ raw/
│ │ └─ listings.csv # Raw Airbnb dataset
│ └─ processed/
│ └─ cleaned.csv # Cleaned data (generated)
├─ models/
│ └─ model.pkl # Trained model (generated)
├─ requirements.txt # Python dependencies
└─ run_all.py # Run everything with one command


---

## Prerequisites
- Python 3.10+  
- pip (Python package manager)  

Optional but recommended:

```bash
python3 -m venv venv
source venv/bin/activate
```

## Dataset
Download the Detailed Listings CSV for your city from Inside Airbnb.
Place it in:
```bash
data/raw/listings.csv
```
If the file is .csv.gz, unzip it first:
```bash
gunzip data/raw/listings.csv.gz
```
## Install Dependencies
```bash
pip3 install -r requirements.txt
```
Includes pandas, scikit-learn, Streamlit, joblib, etc.

## Run Everything (Recommended)
From the project root, run:
```bash
python3 run_all.py
```
This will:

1. Clean the data → data/processed/cleaned.csv
2. Train the model → models/model.pkl
3. Launch the Streamlit app locally
   >> Open the Local URL (e.g., http://localhost:8501) in your browser.

## Manual Steps (Optional)

If you prefer to run steps individually:

1. Clean data
```bash
python3 -m src.data_cleaning
```
3. Train the model
```bash
python3 -m src.train
```
4. Launch Streamlit
```bash
streamlit run app/app.py --server.headless true --browser.gatherUsageStats false
```
Press Ctrl + C in Terminal to stop Streamlit.

## Notes
run_all.py automatically creates models/ and data/processed/ if missing.
Streamlit runs fully locally — no login or email required.
Update dependencies later:
pip install -r requirements.txt --upgrade
## References
Inside Airbnb
 — public dataset
Python libraries: pandas, scikit-learn, Streamlit
