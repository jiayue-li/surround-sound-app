from flask import Flask, render_template, request
from genreMood import main

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'GET':
        return render_template('home.html', music = music)
    if request.method == 'POST':
        imageLink = request.form['imageLink']
        return music(imageLink)

# @app.route('/hello/')
def music(imageLink):
    info = main(imageLink)
    if info != "Error":
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
    # images = {"roadtrip-sample.jpg": "https://static.vinepair.com/wp-content/uploads/2017/04/roadtrip-inside.jpg", "concert-sample.jpg":"", "empty-road-sample.jpg":"", "nightlife-sample.jpg":"", "studying-sample.jpg":"https://fthmb.tqn.com/iO6R-KZ-eEVQGdMF9Lgn3okmhfU=/1500x1000/filters:fill(auto,1)/StudyingAtNight-58c2c2635f9b58af5ca0464b.jpg", "sunrise-sample.jpg": ""}
    images = {"party-sample.jpg": "https://images.pexels.com/photos/196652/pexels-photo-196652.jpeg?w=940&h=650&dpr=2&auto=compress&cs=tinysrgb", "roadtrip-sample.jpg": "https://static.vinepair.com/wp-content/uploads/2017/04/roadtrip-inside.jpg", "concert-sample.jpg":"https://surround-sound-app.herokuapp.com/static/images/concert-sample.jpg", "ny.jpg":"https://surround-sound-app.herokuapp.com/static/images/ny.jpg", "studying-sample.jpg":"https://fthmb.tqn.com/iO6R-KZ-eEVQGdMF9Lgn3okmhfU=/1500x1000/filters:fill(auto,1)/StudyingAtNight-58c2c2635f9b58af5ca0464b.jpg", "sunrise-sample.jpg": "https://surround-sound-app.herokuapp.com/static/images/sunrise-sample.jpg"}
    if imageName in images:
        # return render_template('sampleimage.html', imageName=imageName)
        return music(images[imageName])
    else:
        return render_template('home.html')

@app.route('/test')
def test():
    tags = ["a", "b", "c"]
    return render_template('displayMusic.html', tags=tags, imageLink = "https://www.city-journal.org/sites/cj/files/New-York.jpg")
