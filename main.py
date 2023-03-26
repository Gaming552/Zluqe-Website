from flask import Flask, render_template, request, send_from_directory, jsonify, redirect
import requests
import random
import config

app = Flask(__name__, static_folder='static', template_folder='views')

# Render Templates / HTML's

@app.route('/')
def index():
    return render_template('index.html')


# Redirects

@app.route('/discord')
def discord_invite():
    return redirect(config.DISCORD_INVITE, code=302)
@app.route('/github')
def github_link():
    return redirect(config.GITHUB, code=302)
@app.route('/create')
def zluqe_create():
    return redirect(config.PANEL_STORE_CREATE, code=302)
@app.route('/panel')
def zluqe_panel():
    return redirect(config.PANEL, code=302)


if __name__ == '__main__':
    app.run(debug=True)
