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
        print(spotifyLink)
        return render_template('displayMusic.html', tags=tags, imageLink = imageLink, genreMood = genreMood,spotifyLink=spotifyLink)
    else:
        return render_template('home.html')
        # return render_template('link.html', spotifyLink=spotifyLink)

@app.route('/images/<imageName>')
def imageURL(imageName):
    images = ["concert-sample.jpg", "empty-road-sample.jpg", "nightlife-sample.jpg", "studying-sample.jpg", "sunrise-sample.jpg"]
    if imageName in images:
        return render_template('sampleimage.html', imageName=imageName)
    else:
        return render_template('home.html')

@app.route('/test')
def test():
    tags = ["a", "b", "c"]
    return render_template('displayMusic.html', tags=tags, imageLink = "https://www.city-journal.org/sites/cj/files/New-York.jpg")
