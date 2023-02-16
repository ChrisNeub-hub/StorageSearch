import os
import shutil

# Define the file extensions you want to search for
file_extensions = ['.txt', '.doc', '.docx', '.pdf']

# Define the root folder where you want to start the search
root_folder = 'F:\\'

# Define the folder where you want to move the documents to
destination_folder = 'F:\\Documents'

# A function that searches for documents in a folder and its sub-folders and moves them to a destination folder
def move_documents(folder):
    for subdir, dirs, files in os.walk(folder):
        for file in files:
            filepath = os.path.join(subdir, file)
            
            if any(filepath.endswith(ext) for ext in file_extensions):
                try:
                    shutil.move(filepath, os.path.join(destination_folder, file))
                    print("Document found: ", file)
                
                except Exception:
                    print(Exception)
# Call the function to start the search and move
move_documents(root_folder)