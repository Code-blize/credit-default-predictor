"""
DAY 1: Environment Setup & Data Collection
============================================

LEARNING OBJECTIVES:
- Understand proper Python project setup
- Learn data validation techniques
- Practice exploratory data analysis
- Build foundation for ML pipeline

WHAT I'LL DO:
1. Validate Python environment
2. Download the UCI credit card dataset
3. Perform initial data exploration
4. Create data quality report

TIME ESTIMATE: 2-3 hours
"""

import sys
import subprocess
import os
from pathlib import Path

def check_python_version():
    """
    Validate Python version is 3.8+
    
    WHY THIS MATTERS:
    - Modern ML libraries require Python 3.8+
    - Version compatibility prevents hard-to-debug errors
    - Professional projects always validate dependencies
    """
    required_version = (3, 8)
    current_version = sys.version_info[:2]
    
    if current_version >= required_version:
        print(f" Python {current_version[0]}.{current_version[1]} detected - Good to go!")
        return True
    else:
        print(f" Python {current_version[0]}.{current_version[1]} detected")
        print(f"   Required: Python {required_version[0]}.{required_version[1]}+")
        return False


def install_requirements():
    """
    Install required packages
    
    LEARNING NOTE:
    - requirements.txt is standard for Python projects
    - Version pinning ensures reproducibility
    - Virtual environments prevent conflicts
    """
    requirements = [
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "scikit-learn>=1.3.0",
        "torch>=2.0.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "jupyter>=1.0.0",
        "pytest>=7.4.0",
        "requests>=2.31.0"
    ]
    
    print("\n Installing required packages...")
    print("   This may take a few minutes...\n")
    
    for package in requirements:
        print(f"   Installing {package}...")
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", 
                package, "--break-system-packages", "-q"
            ])
            print(f"    {package} installed")
        except subprocess.CalledProcessError as e:
            print(f"    Failed to install {package}: {e}")
            return False
    
    print("\n All packages installed successfully!")
    return True


def download_uci_dataset():
    """
    Download UCI Credit Card Default dataset
    
    DATASET INFO:
    - 30,000 credit card clients from Taiwan
    - Features: payment history, demographics, credit data
    - Target: default payment (1=default, 0=no default)
    - Perfect for learning classification
    
    SOURCE: UCI Machine Learning Repository
    """
    import requests
    
    data_dir = Path("data/raw")
    data_dir.mkdir(parents=True, exist_ok=True)
    
    dataset_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00350/default%20of%20credit%20card%20clients.xls"
    output_file = data_dir / "credit_default.xls"
    
    if output_file.exists():
        print(f"\n Dataset already exists at {output_file}")
        return True
    
    print(f"\n Downloading UCI Credit Card Default dataset...")
    print(f"   URL: {dataset_url}")
    print(f"   Destination: {output_file}")
    
    try:
        response = requests.get(dataset_url, timeout=30)
        response.raise_for_status()
        
        with open(output_file, 'wb') as f:
            f.write(response.content)
        
        print(f"    Dataset downloaded ({len(response.content) / 1024:.1f} KB)")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"    Download failed: {e}")
        print("\n   FALLBACK: You can manually download from:")
        print("   https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients")
        return False


def validate_dataset():
    """
    Validate downloaded dataset
    
    DATA SCIENCE PRINCIPLE:
    - ALWAYS validate data after loading
    - Check for expected columns, shapes, types
    - Catch data quality issues early
    """
    import pandas as pd
    
    data_path = Path("data/raw/credit_default.xls")
    
    if not data_path.exists():
        print("\n Dataset not found. Run download first.")
        return False
    
    print("\n🔍 Validating dataset...")
    
    try:
        # Load the dataset (skip first row which is header info)
        df = pd.read_excel(data_path, header=1)
        
        print(f"    Dataset loaded successfully")
        print(f"    Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
        print(f"    Memory: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        
        # Check for target variable
        if 'default payment next month' in df.columns:
            default_rate = df['default payment next month'].mean()
            print(f"    Default rate: {default_rate:.2%}")
            print(f"      - {(df['default payment next month']==1).sum():,} defaults")
            print(f"      - {(df['default payment next month']==0).sum():,} non-defaults")
        
        # Check for missing values
        missing = df.isnull().sum().sum()
        if missing == 0:
            print(f"    No missing values detected")
        else:
            print(f"     {missing} missing values found")
        
        # Save basic info
        info_path = Path("data/raw/dataset_info.txt")
        with open(info_path, 'w') as f:
            f.write("UCI CREDIT CARD DEFAULT DATASET\n")
            f.write("="*50 + "\n\n")
            f.write(f"Shape: {df.shape}\n")
            f.write(f"Columns: {list(df.columns)}\n")
            f.write(f"Default rate: {default_rate:.2%}\n")
        
        print(f"    Dataset info saved to {info_path}")
        
        return True
        
    except Exception as e:
        print(f"    Validation failed: {e}")
        return False


def create_project_structure():
    """
    Create organized project folders
    
    PROFESSIONAL PRACTICE:
    - Consistent folder structure
    - Separation of concerns
    - Easy navigation and scaling
    """
    folders = [
        "data/raw",
        "data/processed", 
        "data/features",
        "src/data_collection",
        "src/feature_engineering",
        "src/models",
        "src/evaluation",
        "src/utils",
        "notebooks",
        "outputs/models",
        "outputs/visualizations",
        "outputs/reports",
        "tests"
    ]
    
    print("\n Creating project structure...")
    
    for folder in folders:
        Path(folder).mkdir(parents=True, exist_ok=True)
        print(f"    {folder}/")
    
    # Create .gitignore
    gitignore_content = """
# Data files
data/raw/*
data/processed/*
data/features/*
!data/.gitkeep

# Model outputs
outputs/models/*
!outputs/models/.gitkeep

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/

# Jupyter
.ipynb_checkpoints

# IDE
.vscode/
.idea/

# OS
.DS_Store
"""
    
    with open('.gitignore', 'w') as f:
        f.write(gitignore_content)
    
    print("    .gitignore created")
    
    return True


def main():
    """
    Main setup workflow
    
    PROFESSIONAL TIP:
    - Break complex tasks into functions
    - Each function has single responsibility
    - Easy to test and debug
    """
    print("="*60)
    print("🎓 CREDIT DEFAULT PREDICTION - DAY 1 SETUP")
    print("="*60)
    
    # Step 1: Check Python
    if not check_python_version():
        print("\n Setup failed: Python version too old")
        return
    
    # Step 2: Create structure
    if not create_project_structure():
        print("\n Setup failed: Could not create folders")
        return
    
    # Step 3: Install packages
    if not install_requirements():
        print("\n Setup failed: Package installation error")
        return
    
    # Step 4: Download data
    if not download_uci_dataset():
        print("\n  Setup incomplete: Dataset download failed")
        print("   Continue manually or try again")
    
    # Step 5: Validate data
    if not validate_dataset():
        print("\n  Setup incomplete: Dataset validation failed")
    
    print("\n" + "="*60)
    print(" DAY 1 SETUP COMPLETE!")
    print("="*60)
    print("\n NEXT STEPS:")
    print("   1. Review the downloaded dataset in data/raw/")
    print("   2. Open notebooks/01_data_exploration.ipynb")
    print("   3. Complete Day 1 learning exercises")
    print("   4. Ask mentor (me) any questions!")
    print("\n Great start! Let's keep building!\n")


if __name__ == "__main__":
    main()
