import os
import shutil

# Source folder where the videos are currently located
source_folder = 'F:\\'

# Destination folder where the videos will be moved to
destination_folder = 'F:\\Videos'

# Loop through all files and move videos to the destination folder
for root, dirs, files in os.walk(source_folder):
    # Loop through all files in the current folder
    for file in files:
        # Check if the file is a video file
        if file.endswith('.mp4') or file.endswith('.avi') or file.endswith('.mov'):
            try:
                # Create the full file path for the source file
                source_file = os.path.join(root, file)
                print("Video found: ", source_file)

                # Create the full file path for the destination file
                destination_file = os.path.join(destination_folder, file)

                # Move the file to the destination folder
                shutil.move(source_file, destination_file)
            except Exception:
                print(Exception)
                print("Error at: ", root, file)

print("All video files moved to ", destination_folder)
