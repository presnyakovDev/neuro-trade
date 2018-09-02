#!/usr/bin/python
import requests
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
import numpy as np
import json
from dataset import Dataset
from neuralNetwork import NeuralNetwork
from neuralNetworkv2 import NeuralNetworkv2

PORT_NUMBER = 8080

def getJson():
    with open('/home/conor/Downloads/baba-3m.json') as json_file:
        response = json.load(json_file)
        print(len(response))
    return response;

def getApi():
    r = requests.get('https://api.iextrading.com/1.0/stock/baba/chart/3m')
    return r.json()

def getData():
    return getJson();

dataset = Dataset(getApi())
nn = NeuralNetworkv2(dataset.X, dataset.y)
@app.route('/getpredictions/')
def getPredictions():
    return jsonify(nn.result)
