from backend.wordToMood import *
import random

# def determineTopic():
#     try:
#         topthree = getEmotions()
#         topEmotion = getEmotions()[2]
#         top2 = getEmotions()[1]
#         top3 = getEmotions()[0]
#tags: holds a list of tags from a picture
def determineMusic(tags):
    result = determineGenreOrMood(tags)
    if (result == None):
        return "hiphop"
    return result

def determineGenreOrMood(tags):
    genreToWord = {}
    for tag in tags:
        if tag in dictionary:
            for genre in dictionary[tag].keys():
                if (dictionary[tag][genre] == 1):
                    if genre in genreToWord:
                        genreToWord[genre] +=1
                    else:
                        genreToWord[genre] = 1
    total = float(sum(genreToWord.values()))
    for genre in genreToWord:
        genreToWord[genre] = genreToWord[genre] / total
    biggestVal = genreToWord[max(genreToWord, key = lambda genre: genreToWord[genre])]
    biggestGenre = []
    for genre in genreToWord:
        if genreToWord[genre] == biggestVal:
            biggestGenre.append(genre)
    if (len(genreToWord) == 0):
        return None
    return random.choice(biggestGenre)
