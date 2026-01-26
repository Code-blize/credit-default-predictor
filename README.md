## Progress Log

### Day 1 (Jan 26, 2025) 
**Goal:** Download SEC filings and extract text

**What I Built:**
- Data collection script for SEC 10-K filings
- Text extraction pipeline
- Folder structure for project

**What Broke:**
- `pyrate-limiter` dependency conflict with `sec-edgar-downloader`
- Had to pin specific versions: `pyrate-limiter<3.0.0`
- Learned about dependency hell in Python packages

**What I Learned:**
- Real-world data is messy
- SEC EDGAR has HTML parsing challenges
- Dependency management is crucial
- Force kernel restart needed after uninstalling packages

**What Works:**
- Downloaded 10-K filings for 5 companies
- Text extraction running without errors
- Project structure organized

**Next Steps (Day 2):**
- [ ] FinBERT sentiment analysis
- [ ] Create sentiment scores dataset
- [ ] Visualize sentiment distribution
