from shapley import shapley
from flask import Flask, render_template, request
app = Flask(__name__, template_folder='template')

@app.route('/')
def home_page():
    return render_template('home.html') # from the "templates" folder

@app.route('/res',methods = ['POST', 'GET'])
def res_page():
    shap = shapley()
    abc = {"":0, "Alice":(request.form['a']), "Bob":(request.form['b']), "Chen":(request.form['c']), 
        "AliceBob":(request.form['ab']), "AliceChen":(request.form['ac']), "BobChen":(request.form['bc']),
         "AliceBobChen": (request.form['abc'])}
    for i,j in abc.items():
        if j == "":
            abc[i]=0.0
        else:
            abc[i]=float(j)
    result =shap.values(abc, ["Alice","Bob","Chen"])
    return render_template('res.html', result=result) # from the "templates" folder


if __name__ == '__main__':
    app.run()
