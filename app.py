from flask import Flask, render_template
import pandas as pd
from mplsoccer import Pitch
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rc
from load_animation import animLoad





app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
