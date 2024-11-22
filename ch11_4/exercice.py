
from music_library import *
import os
def manage_playlist(sort_key: str, file_name: str):
	#sauvegarde
	output_dir="libraries"
	if not os.path.exists(output_dir):
		os.makedirs(output_dir)
		print("répertoire créer")
	
	
	songs = [
        Song("Blinding Lights", "The Weeknd", 200, "Pop"),
        Song("Shape of You", "Ed Sheeran", 240, "Pop"),
        Song("Bohemian Rhapsody", "Queen", 360, "Rock"),
        Song("Hotel California", "Eagles", 390, "Rock"),
        Song("Take Five", "Dave Brubeck", 324, "Jazz"),
    ]

	playlist = Playlist("My Favorites")
	for song in songs:
		playlist.add_song(song)
    
	print("Playlist avant tri :")
	playlist.display()
	playlist.sort_songs(sort_key)
	print(f"Playlist triée par {sort_key} :")
    
	playlist.display()

	# playlist.export_to_json(file_path)
	# print(f"Playlist exportée dans le fichier : {file_path}")
	file_path=os.path.join(output_dir, file_name)
	playlist.export_to_json(file_path)

def main():
	manage_playlist("time", file_name="sorted_playlist.json")

if __name__ == "__main__":
	main()
