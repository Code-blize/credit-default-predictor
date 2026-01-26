import os
from bs4 import BeautifulSoup
import re

def extract_text_from_filing(filepath):
    """
    Extract clean text from SEC filing HTML
    This function will evolve as you discover edge cases
    """
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Remove HTML tags
        soup = BeautifulSoup(content, 'html.parser')
        text = soup.get_text()
        
        # Clean up whitespace
        text = re.sub(r'\s+', ' ', text)
        
        return text[:5000]  # First 5000 chars for now
    
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return ""

# Process all downloaded filings
filings_dir = 'data/sec_filings'

if os.path.exists(filings_dir):
    for root, dirs, files in os.walk(filings_dir):
        for file in files:
            if file.endswith('.txt'):
                filepath = os.path.join(root, file)
                print(f"Processing {file}...")
                
                text = extract_text_from_filing(filepath)
                
                # Save extracted text
                output_file = filepath.replace('.txt', '_clean.txt')
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(text)
                
                print(f"✓ Saved to {output_file}")
                print(f"Preview: {text[:200]}...\n")
else:
    print("❌ No SEC filings found! Run 01_data_collection.py first")
