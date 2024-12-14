# Yt-dlpy

Yt-dlpy is a Python script designed to simplify the process of downloading high-quality audio files (MP3, 320kbps, 48kHz) from various platforms supported by `yt-dlp`. This tool supports single-link downloads, batch processing, and scanning directories to download better audio versions from YouTube.

## Features

- **Single Link Download**: Download audio files from a single URL.
- **Batch Processing**: Process a file containing multiple URLs to download audio files in batch.
- **Directory Scanning**: Scan a directory for audio files and download better versions from YouTube.
- **Supported Platforms**: YouTube, SoundCloud, Vimeo, Twitch, and more.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/F-Enix-Origin/yt-dlpy.git
   ```
2. Navigate to the project directory:
   ```sh
   cd yt-dlpy
   ```
3. Run the script:
   ```sh
   python yt-dlpy.py
   ```
4. Follow the on-screen instructions to download your audio files.

## Usage

### Single Link Download

1. Run the script.
2. Enter the video URL when prompted.
3. The script will download the audio file to the specified download directory.

### Batch Processing

1. Create a text file (e.g., `links_list.txt`) containing the URLs, each on a new line.
2. Run the script.
3. Enter `batch` when prompted.
4. The script will process the file and download the audio files in batch.

### Directory Scanning

1. Run the script.
2. Enter `scan` when prompted.
3. Provide the path of the directory to scan.
4. The script will scan the directory, filter the audio files, and download better versions from YouTube.

## License

This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## Acknowledgments

- This script uses `yt-dlp`: [yt-dlp GitHub](https://github.com/yt-dlp/yt-dlp)
- Created by F-Enix

## Contact

For any questions or support, please contact [in progress].
