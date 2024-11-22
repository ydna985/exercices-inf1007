"""
Chapitre 11.4

Classes pour représenter une bibliothèque musicale.
"""
import json

class Song:
    """
    Une chanson dans la bibliothèque.

    :param title:       Le titre de la chanson
    :param artist:      L'artiste de la chanson
    :param duration:    La durée de la chanson en secondes
    :param genre:       Le genre musical
    """

    # TODO: __init__
    # Ajouter un constructeur qui initialise le titre, l'artiste, la durée et le genre d'une chanson.
    def __init__(self, title, artist, time, genre):
        self.__title=title
        self.__artist=artist
        self.time=time
        self.genre=genre
    # TODO: Propriétés
    # Ajouter les propriétés en lecture seule pour `title` et `artist`.
    @property
    def title(self):
        return self.__title
    
    @property
    def artist(self):
        return self.__artist
    # TODO: __str__
    # Implémenter la méthode spéciale pour afficher une chanson au format :
    # "{title} by {artist} - {minutes}:{seconds} ({genre})"
    def __str__(self):
        mins, secs = divmod(self.time, 60)
        return f"{self.__title} by {self.__artist} - {mins}:{secs} ({self.genre})"
    # TODO: to_dict
    # Ajouter une méthode qui convertit les attributs de la chanson en dictionnaire.
    def to_dic(self):
        my_dic={"titre":self.title, "artist":self.artist, "time":self.time, "genre":self.genre}



class Playlist:
    """
    Une playlist contenant plusieurs chansons.

    :param name:  Le nom de la playlist
    """

    # TODO: __init__
    # Ajouter un constructeur qui initialise le nom de la playlist et une liste vide pour les chansons.
    def __init__(self, name):
        self.__name=name
        self.songs=[]
    # TODO: Propriété pour `name`
    # Ajouter une propriété en lecture seule pour le nom de la playlist.
    @property
    def name(self):return self.__name

    # TODO: add_song
    # Ajouter une méthode qui ajoute une chanson à la liste des chansons.
    # Si l'objet ajouté n'est pas une instance de `Song`, lever une erreur `TypeError`.
    def add_song(self,song):
        if not isinstance(song, Song):
            raise TypeError("Seulement des objets de type song peut etre ajouter")
        
        self.songs.append(song)
    # TODO: sort_songs
    # Ajouter une méthode qui trie les chansons selon une clé donnée (`title`, `artist`, `duration`, ou `genre`).
    # Lever une erreur si la clé n'est pas valide.
    def sort_songs(self,key):
        valid_keys=[attr for attr in dir(Song) if not callable(getattr(Song,attr)) and attr.startswith("__")]
        if key not in valid_keys:
            raise ValueError(f"Clé est invalide. Choisir parmi {valid_keys}")
        self.songs.sort(key=lambda song:getattr(song, key))
        #self.songs.sort(key=lambda song:song.to_dict()[key])
    # TODO: total_duration
    # Ajouter une méthode qui calcule et retourne la durée totale de toutes les chansons de la playlist.
    def total_duration(self):
        return sum(song.time for song in self.songs)
    # TODO: display
    # Ajouter une méthode qui affiche les chansons dans la playlist avec leur durée totale.
    def display(self):
        print(f"Playlist: {self.__name}")
        for i,song in enumerate(self.songs,1):
            print(f"{i}. {song}")
        mins, secs = divmod(self.total_duration(), 60)
    # TODO: export_to_json
    # Ajouter une méthode qui exporte la playlist triée au format JSON dans un fichier.
    def export_to_json(self, path):
        playlist_dict=[song.to_dict() for song in self.songs]
        with open(path,'w',encoding="utf-8") as file:
            json.dump(playlist_dict,file)
        print(f"Playlist sauvegarder dans: {path}")
    
