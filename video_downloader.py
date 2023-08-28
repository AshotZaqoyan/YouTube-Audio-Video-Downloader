import yt_dlp

# List of YouTube video URLs you want to download
video_urls = [
    'https://youtu.be/VC66iWDAvrc',
    'https://youtu.be/X-N9MEWYN8w'
]

# Replace with your desired output directory
output_path = 'C:/Users/zaqoy/Desktop/m/'

# Options for yt_dlp (YouTube Downloader)
ydl_opts = {
    'format': 'best',  # Select the best available format
    'outtmpl': output_path + '%(title)s.%(ext)s',  # Output file template
    'quiet': True,  # Suppress output messages
}

# Lists to store successful and failed download URLs
failed_downloads = []
successful_downloads = []

# Initialize YouTube Downloader with the provided options
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for url in video_urls:
        try:
            ydl.download([url])  # Download the video
            print("Downloaded:", url)
            successful_downloads.append(url)
        except Exception as e:
            print(f"Failed to download {url}: {e}")
            failed_downloads.append(url)
            
# Print results
print("\n" * 4)
print("Failed downloads:", failed_downloads)
print("Successful downloads:", successful_downloads)
