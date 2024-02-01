import json
from flask import Flask, jsonify, render_template, request

DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)






@app.route('/')
def index():
    return render_template('index.html', )

@app.route('/qaGeneration')
def qaGeneration():
  return render_template('qaGeneration.html', )

@app.route('/shortAnswerEval')
def shortAnswerEval():
  return render_template('shortAnswerEval.html', )

@app.route('/trainer')
def trainer():
  return render_template('trainer.html', )


@app.route('/summarization')
def summarization():
  return render_template('summarization.html', )





if __name__ == '__main__':
    app.run()
