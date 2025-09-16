import requests
import os
from urllib.parse import urlparse
import datetime

def download_image():
    """
    A practical tool that prompts for a URL, downloads an image,
    and saves it to a local directory, handling errors gracefully.
    """
    
    # Principle: Community - Connecting to the wider web to fetch resources.
    print("--- 🌍 Python Image Downloader ---")
    image_url = input("Please enter the URL of the image you want to download: ")

    # A simple validation for the URL
    if not image_url.lower().startswith(('http://', 'https://')):
        print("❌ Error: Invalid URL. Please provide a full URL starting with 'http://' or 'https://'.")
        return

    # --- Directory Creation ---
    # Principle: Sharing - Organizing fetched images in a dedicated folder.
    # We define a directory to store our downloaded images.
    download_dir = "Fetched_Images"
    try:
        # os.makedirs creates the directory.
        # exist_ok=True prevents an error if the directory already exists.
        os.makedirs(download_dir, exist_ok=True)
        print(f"✅ Directory '{download_dir}' is ready.")
    except OSError as e:
        # Principle: Respect - Handling potential file system errors gracefully.
        print(f"❌ Error: Could not create directory '{download_dir}'. Reason: {e}")
        return

    # --- Image Fetching and Saving ---
    try:
        print(f"🔗 Connecting to {image_url}...")
        
        # Use requests to get the image data. stream=True is crucial for large files.
        # timeout=10 prevents the script from hanging indefinitely.
        response = requests.get(image_url, stream=True, timeout=10)
        
        # Principle: Respect - Checking for HTTP errors without crashing.
        # raise_for_status() will raise an HTTPError for bad responses (4xx or 5xx).
        response.raise_for_status()

        # --- Determine the Filename ---
        # 1. Try to get the filename from the URL path.
        parsed_url = urlparse(image_url)
        filename = os.path.basename(parsed_url.path)
        
        # 2. If the URL path doesn't give a good filename, generate one.
        if not filename or '.' not in filename:
            # Use a timestamp for a unique name.
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            # Try to get the file extension from the 'Content-Type' header.
            content_type = response.headers.get('content-type')
            if content_type and 'image' in content_type:
                # e.g., 'image/jpeg' -> 'jpeg'
                extension = '.' + content_type.split('/')[-1]
            else:
                extension = '.jpg' # Default to .jpg if we can't determine it.
            filename = f"downloaded_image_{timestamp}{extension}"

        # Construct the full path to save the file.
        save_path = os.path.join(download_dir, filename)

        # --- Save the Image in Binary Mode ---
        print(f"📥 Downloading '{filename}'...")
        with open(save_path, 'wb') as file:
            # Write the content in chunks to handle large images efficiently.
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print(f"🎉 Success! Image saved to: {save_path}")

    # --- Comprehensive Error Handling ---
    # Principle: Respect - Catching specific errors and giving clear feedback.
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: Could not download the image. Server responded with: {e.response.status_code} {e.response.reason}")
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Could not connect to the URL. Please check your internet connection or the domain name.")
    except requests.exceptions.Timeout:
        print("❌ Timeout Error: The request took too long to respond.")
    except requests.exceptions.RequestException as e:
        print(f"❌ An unexpected error occurred with the request: {e}")
    except IOError as e:
        print(f"❌ File Error: Could not save the image to disk. Reason: {e}")

# --- Main Execution Block ---
# Principle: Practicality - Making the script directly runnable.
if __name__ == "__main__":
    download_image()