"""
Setup script: Creates folder structure and checks dependencies
Run this FIRST before any other script
"""

import os
import sys

def create_folders():
    """Create necessary folder structure"""
    folders = [
        'data',
        'data/sec_filings',
        'data/processed',
        'data/models',
        'logs'
    ]
    
    print("Creating folder structure...")
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"  ✓ {folder}")
    
    print("\n Folder structure ready!")

def check_dependencies():
    """Check if required packages are installed"""
    required = [
        'pandas',
        'numpy',
        'sec_edgar_downloader',
        'yfinance',
        'bs4',  # beautifulsoup4
        'transformers',
        'torch',
        'sklearn'
    ]
    
    print("\nChecking dependencies...")
    missing = []
    
    for package in required:
        try:
            __import__(package)
            print(f"  {package}")
        except ImportError:
            print(f"  {package} - MISSING")
            missing.append(package)
    
    if missing:
        print(f"\n Missing packages: {', '.join(missing)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("\n All dependencies installed!")
    return True

if __name__ == "__main__":
    create_folders()
    check_dependencies()
