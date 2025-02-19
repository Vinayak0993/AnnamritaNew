from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__, template_folder='template')

model1=pickle.load(open('trained_model_samosa.pkl','rb'))
model2=pickle.load(open('trained_model_rice.pkl','rb'))
model3=pickle.load(open('trained_model_dal.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("samosa.html")


@app.route('/predict',methods=['POST','GET'])
def predict1():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model1.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>str(0.5):
        return render_template('samosa.html',pred='Samosa is not spoiled')
    else:
        return render_template('samosa.html',pred='Samosa is spoiled')
    

@app.route('/predict2',methods=['POST','GET'])
def predict2():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model2.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>str(0.5):
        return render_template('rice.html',pred='rice is not spoiled')
    else:
        return render_template('rice.html',pred='rice is spoiled')

@app.route('/predict3',methods=['POST','GET'])
def predict3():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model3.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>str(0.5):
        return render_template('lentil.html',pred='lentil soup is not spoiled')
    else:
        return render_template('lentil.html',pred='lentil soup is spoiled')



if __name__ == '__main__':
    app.run(debug=True)
