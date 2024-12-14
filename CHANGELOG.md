# Changelog

## [1.0.0] - 2024-12-14
### Ajouté
- **Importations** :
  - Ajout des modules `os`, `re`, `subprocess`, et `time`.

- **Variables Globales** :
  - `DOWNLOAD_PATH` : Chemin de téléchargement configurable.

- **Fonctions** :
  - `start()` : Affiche un message de démarrage avec des effets visuels.
  - `print_banner()` : Affiche une bannière ASCII.
  - `update_yt_dlp()` : Met à jour `yt-dlp` à la dernière version.
  - `download_audio(url)` : Télécharge un fichier audio à partir de l'URL fournie.
  - `url_request()` : Demande à l'utilisateur de saisir l'URL de la vidéo.
  - `download_mp3(line)` : Télécharge un fichier MP3 à partir de l'URL fournie.
  - `batch_process(file_path)` : Traite un fichier contenant des URLs pour télécharger les fichiers MP3 en batch.
  - `main()` : Fonction principale qui orchestre le flux du programme.

- **Flux Principal** :
  - Appelle `start()` et `print_banner()`.
  - Met à jour `yt-dlp`.
  - Change le répertoire de travail à `DOWNLOAD_PATH`.
  - Boucle pour demander des URLs et télécharger des fichiers MP3.
  - Gère les téléchargements en batch si l'utilisateur entre 'batch'.
