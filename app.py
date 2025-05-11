#!/usr/bin/env python3
#make a flask hello world app
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import os

from api.fetch_data import fetch_tripadvisor_data

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
@app.route('/')
def index():
    session['city'] = 'Tacoma'
    session['state'] = 'WA'
    categories = ['restaurants', 'hotels', 'attractions']
    if request.method == 'GET':
        if request.args.get('city'):
            session['city'] = request.args.get('city')
        if request.args.get('state'):
            session['state'] = request.args.get('state')
    # Create a data object with business information
    all_data = {}
    all_data ['restaurants'] = fetch_tripadvisor_data(session['city'], session['state'], 'restaurants', use_cache_only=True)
    all_data ['hotels'] = fetch_tripadvisor_data(session['city'], session['state'], 'hotels', use_cache_only=True)
    all_data ['attractions'] = fetch_tripadvisor_data(session['city'], session['state'], 'attractions', use_cache_only=True)
    
    print(all_data)
    print("Preston")
    return render_template('index.html', city=session['city'], state=session['state'], categories=categories, location_data=all_data)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
 