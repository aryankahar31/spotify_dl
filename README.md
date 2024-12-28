# spotify_dl
# Spotify to MP3 Converter

This project is a Python script that allows you to convert Spotify tracks to MP3 format by searching for the song on YouTube and downloading its audio. It uses the [Spotipy](https://spotipy.readthedocs.io/) library for Spotify API integration and [yt-dlp](https://github.com/yt-dlp/yt-dlp) for downloading and extracting audio from YouTube.

## Features

- Fetches metadata for Spotify tracks, including the track name, artist, and album.
- Searches for the track on YouTube using its title and artist.
- Downloads the audio from YouTube in MP3 format.
- Supports automatic handling of errors and invalid inputs.

## Requirements

To run this project, you need to install the following Python libraries:

- `spotipy` for interacting with the Spotify API.
- `yt-dlp` for downloading audio from YouTube.
- `pytube` for YouTube search functionality.
  
You can install the necessary libraries using `pip`:

```bash
pip install spotipy yt-dlp pytube
