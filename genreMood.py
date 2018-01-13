from backend.topicAlgo import determineGenreOrMood
from backend.imageTagger import analyze_tone
from backend.imageTagger import getToneWords

playlists = {"hiphop": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX0XUsuxWHRQd",
"pop": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DXcBWIGoYBM5M",
"popculture": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWWF3yivn1m3D",
"country": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX1lVhptIYRda",
"workout": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWSJHnPb1f0X3",
"chill": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX4WYpdgoIcn6",
"electronic": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX8tZsk68tuDw",
"rock": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DXcF6B6QPhFDv",
"focus": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX4sWSpwq3LiO",
"religious": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DXcb6CQIjdqKy",
"indie": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX2Nc3B70tvx0",
"outside": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX9wC1KY45plY",
"happy": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX7KNKjOK0o75",
"anger": ["https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX3YSRoSdA634", "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWSqBruwoIXkA", "https://open.spotify.com/user/sonymusic/playlist/6dm9jZ2p8iGGTLre7nY4hf", "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWX83CujKHHOn"],
"contempt": ["https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWX83CujKHHOn", "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWSqBruwoIXkA", "https://open.spotify.com/user/sonymusic/playlist/6dm9jZ2p8iGGTLre7nY4hf"],
"disgust": ["https://open.spotify.com/user/sonymusic/playlist/6dm9jZ2p8iGGTLre7nY4hf", "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWSlw12ofHcMM"],
"fear": ["https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX4fpCWaHOned"],
"happiness":["https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX6ALfRKlHn1t","https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWSkMjlBZAZ07", "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWSqmBTGDYngZ", "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX9T8P88bzbxH", "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX7KNKjOK0o75", "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DXdPec7aLTmlC", "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX9XIFQuFvzM4", "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DXca8AyWK6Y7g"],
"neutral": ["https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWTkxQvqMy4WW", "https://open.spotify.com/user/kristitalbott/playlist/39ysfhYS5guAY5sP8UqSkJ", "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWUNIrSzKgQbP", "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX7K31D69s4M1", "https://open.spotify.com/user/myplay.com/playlist/2wW2k1Hu2WeEDKvdOMyxzT", "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX1s9knjP51Oa", "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX4E3UdUs7fUx"],
"sadness": ["https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX7gIoKXt0gmx"],
"surprise": ["https://open.spotify.com/user/spotify/playlist/37i9dQZF1DXca8AyWK6Y7g"],
"calm": ["https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX4WYpdgoIcn6"]}

def determinePlaylist(toneWord):
    if toneWord in playlists:
        return playlists[toneWord]
    else:
        return "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DXcBWIGoYBM5M"

def main(url):
    toneWords = getToneWords(url)
    if not toneWords:
        return "Error"
    # print(toneWords)
    toneWord = determineGenreOrMood(toneWords)
    # print(toneWord)
    if not toneWord:
        toneWord = "pop"
    playlist = determinePlaylist(toneWord)
    info = {"imageDescriptions": toneWords, "toneWord": toneWord, "playlist": playlist}
    return info

# main("https://www.city-journal.org/sites/cj/files/New-York.jpg")
