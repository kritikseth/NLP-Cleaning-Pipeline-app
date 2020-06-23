from flask import Flask, render_template, request, redirect
import pandas as pd
import importlib
nlpc = importlib.import_module('nlpclean')
nlpl = importlib.import_module('nlplearn')

app = Flask(__name__)
@app.route('/')
def main():
    return redirect('https://kritikseth.github.io')

@app.route('/nlppipeline')
def nlp():
    return render_template('nlp.html')

@app.route('/nlppipeline/process', methods=['GET','POST'])
def nlpclean():
    if request.method == 'POST':
        toggle = request.form.to_dict(flat=False)
        cleantext, og = nlpc.clean(toggle)
        text = nlpl.learn(toggle)
    return render_template('nlp.html', orignal_input = og, clean_output = cleantext, clean_learn = text)

if __name__ == '__main__':
    app.run()
    
