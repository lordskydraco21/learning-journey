import os
import shutil
from pathlib import Path
from datetime import datetime

def move_files_to_folder(source_dir, new_folder_name):
    """
    Move all files from source directory to a new folder,
    except requirements.txt and README.md
    """
    # Convert to Path object
    source_path = Path(source_dir)
    
    # Create timestamp for folder name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_folder_name = f"{new_folder_name}_{timestamp}"
    
    # Create new folder
    new_folder_path = source_path / new_folder_name
    new_folder_path.mkdir(exist_ok=True)
    
    print(f"Created folder: {new_folder_name}")
    
    # Files to exclude
    excluded_files = {
        'requirements.txt',
        'README.md',
        'readme.md',
        'move_files.py'  # Exclude this script itself
    }
    
    # Move files
    moved_count = 0
    for item in source_path.iterdir():
        # Skip if it's a directory or an excluded file
        if item.is_dir() or item.name.lower() in excluded_files:
            continue
            
        try:
            # Handle name conflicts
            target_path = new_folder_path / item.name
            if target_path.exists():
                base = target_path.stem
                suffix = target_path.suffix
                counter = 1
                while target_path.exists():
                    new_name = f"{base}_{counter}{suffix}"
                    target_path = new_folder_path / new_name
                    counter += 1
            
            # Move the file
            shutil.move(str(item), str(target_path))
            print(f"Moved: {item.name} -> {target_path.name}")
            moved_count += 1
            
        except Exception as e:
            print(f"Error moving {item.name}: {str(e)}")
    
    print(f"\nOperation complete!")
    print(f"Files moved: {moved_count}")
    print(f"Destination folder: {new_folder_path}")

def main():
    # Get current directory
    current_dir = os.getcwd()
    
    print("File Moving Utility")
    print("==================")
    print(f"Working directory: {current_dir}")
    
    # Move files to a new folder named 'project_files'
    move_files_to_folder(current_dir, "project_files")

if __name__ == "__main__":
    main()
