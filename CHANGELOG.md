# Changelog

## [1.5.0] - 2024-12-14
### Added
- **New Imports** :
  - `sys`
  - `argparse`
  - `urllib.request`
  - `urllib.error`
  - `mutagen`
  - `concurrent.futures`

- **New Global Variables** :
  - `YT_DLP_COMMAND` : Base command for `yt-dlp`.
  - `SUPPORTED_SITES_URL` : URL of the `supportedsites.md` file.
  - `URL_PATTERNS` : Regular expressions to check URLs.
  - `AUDIO_EXTENSIONS` : Supported audio file extensions.
  - `MAX_BITRATE` and `MAX_SAMPLE_RATE` : Filtering thresholds for bitrate and sample rate.

- **New Functions** :
  - `check_and_install_yt_dlp()` : Checks and installs `yt-dlp` if necessary.
  - `is_supported_url(url)` : Checks if a URL is supported.
  - `create_download_directory(directory)` : Creates the download directory.
  - `download_supportedsites_md()` : Downloads the `supportedsites.md` file.
  - `extract_supported_sites()` : Extracts supported sites.
  - `check_site_in_url(supported_sites, url)` : Checks if a supported site is in the URL.
  - `download_audio_thread(url, supported_sites)` : Downloads an audio file using `yt-dlp`.
  - `scan_directory(directory)` : Scans a directory to find audio files.
  - `filter_audio_files(audio_files, max_bitrate, max_sample_rate)` : Filters audio files.
  - `write_filtered_files_to_file(filtered_files, file_path)` : Writes filtered audio files to a file.

### Modified
- **Existing Functions** :
  - `update_yt_dlp()` : Added call to `check_and_install_yt_dlp()`.
  - `download_audio(url)` : Uses `YT_DLP_COMMAND`.
  - `url_request()` : Renamed to `get_url_from_user()` with additional features.
  - `download_mp3(line)` : Added handling for directory scans.
  - `batch_process(file_path)` : Added handling for directory scans and use of `ThreadPoolExecutor`.
  - `main()` : Added handling for command-line arguments, downloading and processing supported sites, and handling directory scans.

### Other Changes
- Added handling for command-line arguments with `argparse`.
- Added verification and installation of `yt-dlp` if necessary.
- Added handling for directory scans to find and filter audio files.
- Added handling for supported sites via the `supportedsites.md` file.
