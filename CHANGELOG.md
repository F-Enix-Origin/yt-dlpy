# Changelog

## [1.5.0] - 2024-12-14
### Ajouté
- **Nouvelles Importations** :
  - `sys`
  - `argparse`
  - `urllib.request`
  - `urllib.error`
  - `mutagen`
  - `concurrent.futures`

- **Nouvelles Variables Globales** :
  - `YT_DLP_COMMAND` : Commande de base pour `yt-dlp`.
  - `SUPPORTED_SITES_URL` : URL du fichier `supportedsites.md`.
  - `URL_PATTERNS` : Expressions régulières pour vérifier les URLs.
  - `AUDIO_EXTENSIONS` : Extensions de fichiers audio supportées.
  - `MAX_BITRATE` et `MAX_SAMPLE_RATE` : Seuils de filtrage pour le bitrate et la fréquence d'échantillonnage.

- **Nouvelles Fonctions** :
  - `check_and_install_yt_dlp()` : Vérifie et installe `yt-dlp` si nécessaire.
  - `is_supported_url(url)` : Vérifie si une URL est supportée.
  - `create_download_directory(directory)` : Crée le répertoire de téléchargement.
  - `download_supportedsites_md()` : Télécharge le fichier `supportedsites.md`.
  - `extract_supported_sites()` : Extrait les sites supportés.
  - `check_site_in_url(supported_sites, url)` : Vérifie si un site supporté est dans l'URL.
  - `download_audio_thread(url, supported_sites)` : Télécharge un fichier audio en utilisant `yt-dlp`.
  - `scan_directory(directory)` : Scanne un répertoire pour trouver les fichiers audio.
  - `filter_audio_files(audio_files, max_bitrate, max_sample_rate)` : Filtre les fichiers audio.
  - `write_filtered_files_to_file(filtered_files, file_path)` : Écrit les fichiers audio filtrés dans un fichier.

### Modifié
- **Fonctions Existantes** :
  - `update_yt_dlp()` : Ajout de l'appel à `check_and_install_yt_dlp()`.
  - `download_audio(url)` : Utilisation de `YT_DLP_COMMAND`.
  - `url_request()` : Renommée en `get_url_from_user()` avec des fonctionnalités supplémentaires.
  - `download_mp3(line)` : Ajout de la gestion des scans de répertoires.
  - `batch_process(file_path)` : Ajout de la gestion des scans de répertoires et utilisation de `ThreadPoolExecutor`.
  - `main()` : Ajout de la gestion des arguments de ligne de commande, téléchargement et traitement des sites supportés, et gestion des scans de répertoires.

### Autres Changements
- Ajout de la gestion des arguments de ligne de commande avec `argparse`.
- Ajout de la vérification et de l'installation de `yt-dlp` si nécessaire.
- Ajout de la gestion des scans de répertoires pour trouver et filtrer les fichiers audio.
- Ajout de la gestion des sites supportés via le fichier `supportedsites.md`.
