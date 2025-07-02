# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Add more routes here if you plan to calculate via Flask backend later

if __name__ == '__main__':
    app.run(debug=True)
# To run the Flask app, use the command: python app.py
# Make sure to have Flask installed in your environment             
# You can install Flask using pip if you haven't already:
# pip install Flask
# Note: This is a basic Flask app setup. You can expand it with more routes and logic as needed.
# Note: This app currently serves a static HTML page. You can add more functionality later. 

