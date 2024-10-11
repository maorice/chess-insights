from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

CHESS_API_URL = 'https://api.chess.com/pub'

