# 🎵 YouTube Audio and Video Downloader 🎥

This repository contains Python scripts to download audio and video content from YouTube using the `yt_dlp` library.

## Prerequisites

Before running the scripts, make sure you have the following installed:

- ✔️ `yt_dlp` library
- ✔️ `ffmpeg`

## Installation

1. Clone the repository:
  ```console
  git clone https://github.com/AshotZaqoyan/YouTube-Audio-Video-Downloader.git
  cd YouTube-Audio-Video-Downloader
  ```

3. Install the `yt_dlp` library:📗
```console
pip install yt-dlp
```

4. Download 📲 and install `ffmpeg`:

**Windows:**

a. Visit the official FFmpeg website: https://ffmpeg.org/download.html

b. Under the "Get packages & executable files" section, find 🔍 Windows builds. Choose the "Windows Builds by BtbN" link.

c. Download 📲 the appropriate version for your system (32-bit or 64-bit).

d. Extract the downloaded ZIP file 📂 to a directory (e.g., C:\ffmpeg).

e. Add the path (e.g., C:\ffmpeg\bin) to your system's PATH variable. [Instructions](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/)

**macOS:**

a. Install Homebrew (if not installed):
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

b. Install FFmpeg:
brew install ffmpeg

**Linux (Ubuntu/Debian):**

a. Update package 📦 info:
sudo apt update

b. Install FFmpeg:
sudo apt install ffmpeg

## Usage

### Audio Downloader (`audio_downloader.py`)

1. Edit the `video_urls` list in the script 📜 to include the YouTube URLs you want to download.

2. Modify the `output_path` 📂 to specify the directory for the downloaded audio files.

3. If you have installed FFmpeg in a custom location (not in the system PATH), you'll need to adjust the `ffmpeg_location` in the `ydl_opts` dictionary in the `audio_downloader.py` script 📜. Replace `'path/to/your/ffmpeg'` with the actual path to your FFmpeg executable (if you have FFmpeg in your system PATH you will be able to run the script without needing to specify the `ffmpeg_location`):
```python
   'ffmpeg_location': 'path/to/your/ffmpeg'
```
4. Run the script:

### Video Downloader (`video_downloader.py`)

1. Edit the `video_urls` list in the script 📜 to include the YouTube URLs you want to download.

2. Modify the `output_path` 📂 to specify the directory for the downloaded video files.

3. Run the script:
