
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from yt_dlp import YoutubeDL
from pytube import Search
import os

# Step 1: Spotify API Credentials
SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here

# This is only Example API
# SPOTIFY_CLIENT_ID = '62324b5fb19c45e3934345545fa14'
# SPOTIFY_CLIENT_SECRET = '30c37932775842324521294d9'

# Authenticate with Spotify API
spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))

def get_spotify_metadata(spotify_url):
    """Fetch metadata of a Spotify track."""
    try:
        track = spotify.track(spotify_url)
        return {
            "title": track['name'],
            "artist": track['artists'][0]['name'],
            "album": track['album']['name']
        }
    except Exception as e:
        print(f"Error fetching metadata: {e}")
        return None

def search_and_download_youtube(song_title, artist):
    """Search for the song on YouTube and download the audio without FFmpeg."""
    try:
        search_query = f"{song_title} {artist} lyrics"
        search_results = Search(search_query).results
        
        if not search_results:
            print("No YouTube results found.")
            return None
        
        # Select the first result
        video_url = search_results[0].watch_url
        print(f"Found YouTube video: {video_url}")

        output_path = "downloads"
        os.makedirs(output_path, exist_ok=True)

        # Download audio using yt-dlp without FFmpeg (no post-processing)
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'noplaylist': True,  # Avoid downloading playlists
            'postprocessors': [],  # Remove FFmpeg postprocessors
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        print(f"Downloaded: {song_title}")
        return f"{output_path}/{song_title}.webm"  # Save in .webm format (you can change it if needed)
    except Exception as e:
        print(f"Error downloading YouTube audio: {e}")
        return None

def main():
    """Main function to handle Spotify to MP3 conversion."""
    try:
        # Step 2: Input Spotify Track URL
        spotify_url = input("Enter Spotify track URL: ")
        metadata = get_spotify_metadata(spotify_url)
        if not metadata:
            print("Failed to fetch metadata. Exiting.")
            return

        print(f"Downloading: {metadata['title']} by {metadata['artist']}")

        # Step 4: Search and Download from YouTube
        file_path = search_and_download_youtube(metadata['title'], metadata['artist'])
        if file_path:
            print(f"Downloaded and saved as {file_path}")
        else:
            print("Failed to download audio.")
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
