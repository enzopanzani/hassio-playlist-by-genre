import os
from mutagen import File
from collections import defaultdict

music_dir = "/media/music"
playlist_dir = "/media/playlists"

genres = defaultdict(list)

for root, dirs, files in os.walk(music_dir):
    for file in files:
        if file.lower().endswith(('.mp3', '.flac', '.ogg', '.m4a')):
            full_path = os.path.join(root, file)
            try:
                audio = File(full_path, easy=True)
                if audio is None:
                    continue
                genre = audio.get('genre', ['Unknown'])[0]
                relative_path = os.path.relpath(full_path, "/media")
                genres[genre].append(f"/media/{relative_path}".replace("\\", "/"))
            except Exception as e:
                print(f"Erreur avec le fichier {full_path} : {e}")

os.makedirs(playlist_dir, exist_ok=True)
for genre, tracks in genres.items():
    filename = os.path.join(playlist_dir, f"{genre}.m3u")
    with open(filename, 'w', encoding='utf-8') as f:
        for track in tracks:
            f.write(track + "\n")

print("✅ Playlists générées.")
