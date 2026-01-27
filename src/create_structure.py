"""
Creates the full project structure with .gitkeep files
This makes folders visible on GitHub
"""

import os

# Full project structure (the impressive one)
structure = {
    'data': ['sec_filings', 'processed', 'raw', 'models'],
    'src': ['data_pipeline', 'models', 'utils'],
    'api': [],
    'monitoring': ['dashboards'],
    'tests': [],
    'docs': ['architecture', 'experiments'],
    'notebooks': ['exploration'],
    '.github': ['workflows'],
    'logs': []
}

def create_structure():
    for main_folder, subfolders in structure.items():
        # Create main folder
        os.makedirs(main_folder, exist_ok=True)
        
        # Add .gitkeep to main folder
        gitkeep_path = os.path.join(main_folder, '.gitkeep')
        with open(gitkeep_path, 'w') as f:
            f.write('')  # Empty file
        print(f"✓ Created {main_folder}/")
        
        # Create subfolders
        for subfolder in subfolders:
            full_path = os.path.join(main_folder, subfolder)
            os.makedirs(full_path, exist_ok=True)
            
            # Add .gitkeep to subfolder
            gitkeep_path = os.path.join(full_path, '.gitkeep')
            with open(gitkeep_path, 'w') as f:
                f.write('')
            print(f"  ✓ {main_folder}/{subfolder}/")

if __name__ == "__main__":
    print("Creating production-ready folder structure...\n")
    create_structure()
    print("\n✅ Structure complete! All folders will now appear on GitHub")
