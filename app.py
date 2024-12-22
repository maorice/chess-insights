from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)
chess_com_url = 'https://api.chess.com/pub'
headers = {
    'User-Agent': 'matthewliu218@gmail.com'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.get('/api/get_stats/<username>')
def get_user_data(username):
    
    try:
        response = requests.get(chess_com_url + f'/player/{username}/stats/', headers = headers)
        if response.status_code == 200:
            data = response.json()
            return str(data.get('chess_blitz', {}).get('best', {}).get('rating'))
        else:
            return jsonify({"error": "Player not found"}), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Unexpected error occurred"}), 500

if __name__ == "__main__":
    app.run()


