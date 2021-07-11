#clear
print('Example clear')
playlist = {
    "artist": "Jorja Smith",
    "song": "Be Honest",
    "duration": "3:27"
}
playlist.clear()
print(playlist)
print()

#copy
print('Example copy')
playlist = {
    "artist": "Jorja Smith",
    "song": "Be Honest",
    "duration": "3:27"
}
playlist.copy()
print(playlist)
print()

#fromkeys
print('Example fromkeys')
playlist = ("artist","song","duration")
details = 0
playlist_dict = dict.fromkeys(playlist,details)
print(playlist_dict)
print()

#details = ("Jorja Smith", "Be Honest", "3:27")

#get
print('Example get')
playlist = {
    "artist": "Jorja Smith",
    "song": "Be Honest",
    "duration": "3:27"
}
song = playlist.get("song")
print(song)
print()

#items
print('Example items')
playlist = {
    "artist": "Jorja Smith",
    "song": "Be Honest",
    "duration": "3:27"
}
items = playlist.items()
print(items)
print()

#keys
print('Example keys')
playlist = {
    "artist": "Jorja Smith",
    "song": "Be Honest",
    "duration": "3:27"
}
keys = playlist.keys()
print(keys)
print()

#pop
print('Example pop')
playlist = {
    "artist": "Jorja Smith",
    "song": "Be Honest",
    "duration": "3:27"
}
which_artist = playlist.pop("song")
print(which_artist)
print()

playlist = {
    "artist": "Jorja Smith",
    "song": "Be Honest",
    "duration": "3:27"
}
playlist.pop("song")
print(playlist)
print()

#popitem
print('Example popitem')
playlist = {
    "artist": "Jorja Smith",
    "song": "Be Honest",
    "duration": "3:27"
}
playlist.popitem()
print(playlist)
print()

#setdefault
print('Example setdefault')
playlist = {
    "artist": "Jorja Smith",
    "song": "Be Honest",
    "duration": "3:27"
}
artist = playlist.setdefault("artist")
print(artist)
print()

#update
print('Example update')
playlist = {
    "artist": "Jorja Smith",
    "song": "Be Honest",
    "duration": "3:27"
}
feat = playlist.update({"feat":"Burna Boy"})
print(playlist)
print()

#values
print('Example values')
playlist = {
    "artist": "Jorja Smith",
    "song": "Be Honest",
    "duration": "3:27"
}
data = playlist.values()
print(data)
print()
