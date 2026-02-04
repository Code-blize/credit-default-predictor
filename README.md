credit_default_project/
│
├── 📓 notebooks/                    ← Your Jupyter notebooks go here
│   ├── 01_data_exploration.ipynb   ← Day 1: Explore data
│   ├── 02_data_cleaning.ipynb      ← Day 2: Clean data  
│   ├── 03_feature_engineering.ipynb ← Day 3-4: Create features
│   ├── 04_baseline_model.ipynb     ← Day 5: Simple model
│   └── 05_lstm_model.ipynb         ← Day 6-7: Deep learning
│
├── 📊 data/
│   ├── raw/                        ← Original downloaded data (DON'T EDIT)
│   ├── processed/                  ← Cleaned data (from notebook 02)
│   └── features/                   ← Feature files (from notebook 03)
│
├── 🐍 src/                          ← Python modules (reusable code)
│   ├── data_collection.py          ← Functions to download data
│   ├── feature_engineering.py      ← Functions to create features
│   └── models.py                   ← Model architectures
│
├── 📤 outputs/
│   ├── models/                     ← Saved trained models (.pkl, .pth)
│   ├── visualizations/             ← Plots and charts (.png)
│   └── reports/                    ← Text summaries
│
└── 📝 README.md                     ← Project documentation
