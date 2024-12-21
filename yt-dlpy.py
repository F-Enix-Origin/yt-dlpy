# Small script to simplify the use of yt-dlp
# uses yt-dlp: ‘https://github.com/yt-dlp/yt-dlp’
# creator: F-Enix
# V1.5

import argparse
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from urllib.error import URLError, HTTPError
from urllib.request import urlopen


def check_and_install_mutagen():
    """
    Checks if mutagen is installed and installs it if not.
    """
    try:
        import mutagen
        print("mutagen is already installed.")
    except ImportError:
        print("mutagen is not installed. Installing now...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'mutagen'], check=True)
        print("mutagen has been installed successfully.")


check_and_install_mutagen()

from mutagen import File

# Configurable download path
DOWNLOAD_PATH = 'music_downloaded'
YT_DLP_COMMAND = ['yt-dlp', '-f', 'bestaudio', '-x', '--audio-format', 'mp3',
                  '--audio-quality', '320k', '--embed-thumbnail', '--add-metadata', '--output', '%(title)s.%(ext)s']

# URL of the supportedsites.md file
SUPPORTED_SITES_URL = "https://raw.githubusercontent.com/yt-dlp/yt-dlp/refs/heads/master/supportedsites.md"

# Regular expressions for different platforms
URL_PATTERNS = {
    'YouTube': re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/'),
    'SoundCloud': re.compile(r'(https?://)?(www\.)?soundcloud\.com/'),
    'Vimeo': re.compile(r'(https?://)?(www\.)?vimeo\.com/'),
    'Twitch': re.compile(r'(https?://)?(www\.)?twitch\.tv/'),
}

# Constants for audio file extensions and filtering thresholds
AUDIO_EXTENSIONS = ['.mp3', '.wav', '.flac', '.aac', '.ogg']
MAX_BITRATE = 320000
MAX_SAMPLE_RATE = 48000


def start():
    """
    Displays a startup message with simple visual effects.
    """
    print("Powered")
    time.sleep(1)
    print("by")
    time.sleep(1)
    for i in "..":
        print(i)
        time.sleep(1)
    print("@ F-Enix")
    time.sleep(1)
    print("___________   ___________ _______   .__            ")
    print("\\_   _____/    \\_   _____/ \\      \\  |__|___  ___    ")
    print(" |    __)______|    __)_  /   |   \\ |  |\\  \\/  /     ")
    print(" |     \\/_____/|        \\/    |    \\|  | >    <      ")
    print(" \\___  /      /_______  /\\____|__  /|__|/__/\\_ \\     ")
    print("     \\/               \\/         \\/           \\/      ")


def print_banner():
    banner = """
_____.___.                  __        ___.                ________                              .__
\\__  |   |  ____  __ __  _/  |_  __ __\\_ |_    ____       \\  ____ \\    ____   _  _  __ ____     |  |    ____ _____     ___||  ____   _______
 \\   |   | /  _ \\|  |  \\\\/   __|  |  \\| __ \\  / __ \\ _____|  |  |  \\  /  _ \\ / \\/ \\/ /|  \\  \\| ||  |   /  _ \\\\__  \\   / __ |_/ __ \\ /_   __  \\
  \\___   |(  <_> |  |  / |  |  |  |  /| \\_\\ \\ | ___//____/|  |  |`  \\(  <_> )\\      / |   \\  | ||  |__(  <_> )/ __ \\_/ /_/ | \\  ___/  |  |  \\/
 / ______| \\____/|____/  |__|  |____/ |___  / \\___ |      /_______  / \\____/  \\ /\\_/  |___|\\  / |____/ \\____/(____  /\\____ |  \\___  > |__|
 \\/                                       \\/      \\/              \\/                        \\/                    \\/      \\/      \\/
"""
    print(banner)


def check_and_install_yt_dlp():
    """
    Checks if yt-dlp is installed and installs it if not.
    """
    try:
        subprocess.run(['yt-dlp', '--version'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("yt-dlp is already installed.")
    except FileNotFoundError:
        print("yt-dlp is not installed. Installing now...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'yt-dlp'], check=True)
        print("yt-dlp has been installed successfully.")
    except subprocess.CalledProcessError:
        print("An error occurred while checking yt-dlp. Reinstalling now...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'yt-dlp'], check=True)
        print("yt-dlp has been reinstalled successfully.")


def update_yt_dlp():
    """
    Updates yt-dlp to the latest version available and checks the version.
    """
    check_and_install_yt_dlp()
    try:
        subprocess.run(['pip', 'install', '-U', 'yt-dlp[default]'], check=True)
        subprocess.run(['yt-dlp', '--version'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error updating yt-dlp: {e}")
    except FileNotFoundError:
        print("yt-dlp is not installed. Please install it before continuing.")


def download_audio(url):
    """
    Downloads an audio file from the provided URL using yt-dlp.
    """
    command = YT_DLP_COMMAND + [url]
    try:
        subprocess.run(command, check=True)
        print("File downloaded successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading the video: {e}")
    except FileNotFoundError:
        print("yt-dlp is not installed. Please install it before continuing.")


def is_supported_url(url):
    """
    Checks if the URL matches one of the supported platforms.
    """
    return any(pattern.match(url) for platform, pattern in URL_PATTERNS.items())


def get_url_from_user():
    """
    Prompts the user to enter the video URL and extracts the main URL.
    Checks if the URL matches one of the supported platforms.
    """
    url_local = input("Enter the video URL or 'batch' for batch processing or 'scan' to scan a directory: ")
    if url_local.lower() == 'batch':
        return 'batch'
    elif url_local.lower() == 'scan':
        return 'scan'
    elif is_supported_url(url_local):
        try:
            url_b = re.search("(.+?)&", url_local).group(1)
            return url_b
        except AttributeError:
            return url_local
    else:
        print("Warning: the URL may be defective or the platform is not supported")
        return url_local


def download_mp3(line, is_scan=False):
    """
    Downloads an MP3 file from the provided URL.
    """
    print(f"Downloading MP3 for: {line}")
    if is_scan:
        # Extract the title without extension
        title = os.path.splitext(os.path.basename(line))[0]
        search_query = f"ytsearch:{title}"
        command = YT_DLP_COMMAND + [search_query]
    else:
        command = YT_DLP_COMMAND + [line]

    try:
        subprocess.run(command, check=True)
        if not is_scan:
            print(f"File downloaded successfully for: {line}")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading the video: {e}")
    except FileNotFoundError:
        print("yt-dlp is not installed. Please install it before continuing.")


def batch_process(file_path, is_scan=False):
    """
    Processes a file containing URLs to download MP3 files in batch.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if not lines:
                print("The file is empty.")
            else:
                with ThreadPoolExecutor() as executor:
                    executor.map(lambda line: download_mp3(line.strip(), is_scan), lines)
    except FileNotFoundError:
        with open(file_path, 'w') as file:
            print(f"The file {file_path} was not found. A new empty file has been created.")
    except Exception as e:
        print(f"An error occurred: {e}")


def create_download_directory(directory):
    """
    Creates the download directory if it does not exist.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"The folder '{directory}' has been created.")


def download_supportedsites_md():
    """
    Downloads the supportedsites.md file from the provided URL using urllib.
    """
    try:
        with urlopen(SUPPORTED_SITES_URL) as response:
            content = response.read().decode('utf-8')
            with open('supportedsites.md', 'w', encoding='utf-8') as file:
                file.write(content)
            print("supportedsites.md file downloaded successfully.")
    except (URLError, HTTPError) as e:
        print(f"Error downloading the supportedsites.md file: {e}")


def extract_supported_sites():
    """
    Extracts lines in the form " - **site_name**" from the supportedsites.md file.
    """
    supported_sites = set()
    try:
        with open('supportedsites.md', 'r', encoding='utf-8') as file:
            for line in file:
                match = re.match(r" - \*\*(.+?)\*\*", line)
                if match:
                    supported_sites.add(match.group(1).lower())
        return supported_sites
    except FileNotFoundError:
        print("The supportedsites.md file was not found.")
        return supported_sites
    except Exception as e:
        print(f"An error occurred: {e}")
        return supported_sites


def check_site_in_url(supported_sites, url):
    """
    Checks if any of the supported sites are in the link.
    """
    for site in supported_sites:
        if site in url.lower():
            return site
    return None


def download_audio_thread(url, supported_sites):
    """
    Downloads an audio file from the provided URL using yt-dlp and checks if a supported site is in the URL.
    """
    command = YT_DLP_COMMAND + [url]
    try:
        subprocess.run(command, check=True)
        if not is_supported_url(url):
            print("File downloaded successfully")
            site = check_site_in_url(supported_sites, url)
            if site:
                print(f"The site '{site}' is in the supported sites file")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading the video: {e}")
    except FileNotFoundError:
        print("yt-dlp is not installed. Please install it before continuing.")


def scan_directory(directory):
    """
    Scans a directory and its subdirectories to find all audio files.

    Args:
        directory (str): The path of the directory to scan.

    Returns:
        list: A list of audio file paths.
    """
    audio_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in AUDIO_EXTENSIONS):
                audio_files.append(os.path.join(root, file))

    return audio_files


def filter_audio_files(audio_files, max_bitrate=MAX_BITRATE, max_sample_rate=MAX_SAMPLE_RATE):
    """
    Filters audio files based on bitrate and sample rate.

    Args:
        audio_files (list): A list of audio file paths.
        max_bitrate (int): The maximum bitrate (in bps).
        max_sample_rate (int): The maximum sample rate (in Hz).

    Returns:
        list: A list of tuples containing the file path, bitrate, and sample rate.
    """
    filtered_files = []

    for audio_file in audio_files:
        try:
            audio = File(audio_file)
            if audio is None:
                continue

            bitrate = audio.info.bitrate
            sample_rate = audio.info.sample_rate

            # Check that both conditions are met
            if bitrate < max_bitrate or sample_rate < max_sample_rate:
                filtered_files.append((audio_file, bitrate, sample_rate))
        except Exception as e:
            print(f"Error reading the file {audio_file}: {e}")

    return filtered_files


def write_filtered_files_to_file(filtered_files, file_path):
    """
    Writes the filtered audio files to a text file.

    Args:
        filtered_files (list): A list of tuples containing the file path, bitrate, and sample rate.
        file_path (str): The path of the text file.
    """
    with open(file_path, 'w') as file:
        for audio_file, bitrate, sample_rate in filtered_files:
            file.write(f"{audio_file}\n")


def main():
    """
    Main function that orchestrates the program flow.
    """
    parser = argparse.ArgumentParser(description="Downloads audio files from various platforms.")
    parser.add_argument('--download-path', type=str, default=DOWNLOAD_PATH, help="Download path")
    args = parser.parse_args()

    start()
    print_banner()
    time.sleep(1)

    update_yt_dlp()

    create_download_directory(args.download_path)

    try:
        os.chdir(args.download_path)
    except FileNotFoundError:
        print(
            f"The download directory '{args.download_path}' does not exist. Please create it or change the path in the script.")
        return

    download_supportedsites_md()
    supported_sites = extract_supported_sites()

    while True:
        url = get_url_from_user()
        if url == 'batch':
            file_path = 'links_list.txt'
            batch_process(file_path)
        elif url == 'scan':
            directory_to_scan = input("Enter the path of the directory to scan: ")
            audio_files = scan_directory(directory_to_scan)
            filtered_audio_files = filter_audio_files(audio_files)
            write_filtered_files_to_file(filtered_audio_files, 'filtered_audio_files.txt')
            batch_process('filtered_audio_files.txt', is_scan=True)
        else:
            print("Downloading MP3...")
            if is_supported_url(url):
                print(f"The URL matches a known pattern. Downloading...")
                download_audio_thread(url, supported_sites)
            else:
                print("The URL does not match any known pattern. Checking with the supportedsites.md file...")
                site = check_site_in_url(supported_sites, url)
                if site:
                    print(f"The site '{site}' is in the URL. Downloading...")
                    download_audio_thread(url, supported_sites)
                else:
                    print("No supported site found in the URL.")

        while True:
            end = input("Do you want to download another file? (Y/N): ").strip().lower()
            if end == 'y':
                break
            elif end == 'n':
                print("Exiting the download process...")
                print("Thank you for using our version of Youtube-Dl")
                time.sleep(5)
                return
            else:
                print("Invalid input. Please enter 'Y' for yes or 'N' for no.")


if __name__ == "__main__":
    main()
