import os
import shutil

# Locate the default Hugging Face cache directory
cache_dir = os.path.expanduser("~/.cache/huggingface")

# Check if the directory exists
if os.path.exists(cache_dir):
    shutil.rmtree(cache_dir)
    print(f"Deleted cache directory: {cache_dir}")
else:
    print("No cache directory found!")
