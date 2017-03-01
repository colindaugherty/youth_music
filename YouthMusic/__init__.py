from flask import Flask, flash, render_template, request, session, redirect, url_for, jsonify
import spotipy
from spotipy import oauth2

# Variables
# SP_client_id = 395c0c8b13eb418e9821084402274a16
# SP_client_secret = a35b178c33ba49129168d6a16aeedf65
# SPOTIPY_REDIRECT_URI = 'http://74.134.250.233/'
# SCOPE = 'user-read-email,user-follow-modify,streaming,user-top-read,playlist-read-collaborative,'
# CACHE = '.spotipyoauthcache'

# sp = spotipy.Spotipy()

app = Flask(__name__)

Flask.secret_key = "random"

@app.route("/search", methods=['POST'])
def search():
    return jsonify({
        'song': sp.search(q=request.form[song]) 
    })

@app.route("/")
def index():
    return render_template('index.html', cookie=True)

@app.route("/admin")
def admin():
    return render_template('admin.html')

@app.route("/worship")
def worship():
    return render_template('worship.html')

@app.route("/help")
def help():
    return render_template('help.html')

if __name__ == "__main__":
    app.run()
