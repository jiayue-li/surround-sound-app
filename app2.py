from flask import Flask, render_template, request
from genreMood import main

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    if request.method == 'POST':
        imageLink = request.form['imageLink']
        return music(imageLink)

# @app.route('/hello/')
def music(imageLink):
    info = main(imageLink)
    if info:
        tags = info["imageDescriptions"]
        genreMood = info["toneWord"]
        spotifyLink = info["playlist"]
        return render_template('displayMusic.html', tags=tags, imageLink = imageLink, genreMood = genreMood,spotifyLink=spotifyLink)
    else:
        return render_template('home.html')
        # return render_template('link.html', spotifyLink=spotifyLink)

@app.route('/test')
def test():
    tags = ["a", "b", "c"]
    return render_template('displayMusic.html', tags=tags, imageLink = "https://www.city-journal.org/sites/cj/files/New-York.jpg")
