# Credit Default Prediction - Multi-Modal ML System

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-orange)](https://huggingface.co/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> Multi-modal credit default prediction combining financial time series (LSTM) with SEC filing sentiment analysis (FinBERT)

##  Project Overview

This system predicts credit default risk by:
- Analyzing SEC 10-K filings using FinBERT for sentiment extraction
- Processing financial time series data with LSTM networks
- Combining text embeddings + numerical features in ensemble model
- Deploying via FastAPI with real-time inference

**Status:**  Week 1 - Data Pipeline Development

---

##  Project Structure
```
credit-default-predictor/
├── src/
│   ├── data_pipeline/       # Data collection & processing
│   ├── models/              # ML model implementations
│   ├── features/            # Feature engineering
│   └── utils/               # Helper functions
├── api/                     # FastAPI backend
├── notebooks/               # Exploratory analysis
├── tests/                   # Unit tests
├── data/                    # Data storage (gitignored)
├── outputs/                 # Model outputs & visualizations
├── docs/                    # Documentation
├── requirements.txt         # Dependencies
└── .gitignore              # Ignore rules
```

---

##  Quick Start
```bash
# Clone repository
git clone https://github.com/Code-blize/credit-default-predictor.git
cd credit-default-predictor

# Install dependencies
pip install -r requirements.txt

# Run data pipeline
python src/data_pipeline/01_collect_data.py
python src/data_pipeline/02_extract_text.py
python src/data_pipeline/03_sentiment_analysis.py

# Train model (coming Week 2)
python src/models/train.py
```

---

##  Development Log

### Week 1: Data Pipeline
- [x] SEC EDGAR data collection
- [x] Text extraction from 10-K filings
- [x] FinBERT sentiment analysis
- [ ] Feature engineering pipeline
- [ ] Data validation & tests

### Week 2: Model Development
- [ ] LSTM time series model
- [ ] FinBERT embedding extraction
- [ ] Ensemble architecture
- [ ] Model evaluation metrics

### Week 3: Deployment
- [ ] FastAPI endpoint
- [ ] Model serving
- [ ] Monitoring dashboard
- [ ] Docker containerization

---

##  Tech Stack

**Data & ML:**
- Python 3.11
- PyTorch 2.0+
- HuggingFace Transformers
- Pandas, NumPy, Scikit-learn

**APIs & Deployment:**
- FastAPI
- Docker
- Prometheus (monitoring)

**Data Sources:**
- SEC EDGAR (10-K filings)
- Yahoo Finance (stock prices)

---

##  Results

_Coming soon - model performance metrics, visualizations_

---

##  Contributing

This is a learning project. Feedback welcome!

---

##  License

MIT License - see LICENSE file

---

**Built by:** [@Code-blize](https://github.com/Code-blize)  
**Started:** January 2025
