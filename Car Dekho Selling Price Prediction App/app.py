from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd


app = Flask(__name__)


te = pickle.load(open('name_te.pkl','rb'))
scaler=pickle.load(open('slr.pkl','rb'))
rf=pickle.load(open('CDSPP_rf.pkl','rb'))


@app.route('/')
def hello_world():
	return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    modname = request.form.get("name")
    modname=[modname]
    modname=pd.DataFrame(modname,columns =['name'])
    modname=te.transform(modname['name'])
    modname=modname.values.tolist()[0][0]

    transmission = request.form.get("transmission")
    if transmission=='Automatic':
        transmission=0
    if transmission=='Manual':
        transmission=1


    fuel = request.form.get("fuel")
    if fuel=='Diesel':
        Petrol=0
        cng=0
        Disel=1
        lpg=0

        
    elif fuel=='Petrol':
        Petrol=1
        cng=0
        Disel=0
        lpg=0

        
    elif fuel=='CNG':
        Petrol=0
        cng=1
        Disel=0
        lpg=0

    elif fuel=='LPG':
        Petrol=0
        cng=0
        Disel=0
        lpg=1

        
    elif fuel=='Electric':
        Petrol=0
        cng=0
        Disel=0
        lpg=0
           


    seller_type = request.form.get("seller_type")
    if seller_type=='Individual':
        individual=1
        dealer=0

    elif seller_type=='Dealer':
        individual=0
        dealer=1

    elif seller_type=='Trustmark_Dealer':
        individual=0
        dealer=0


    year = int(request.form.get("year"))


    
    # name=te.transform([[name]])
    
    temp_arr=list()
    temp_arr=temp_arr+[year, transmission, dealer,individual,cng,Disel,lpg,Petrol,modname]
    data=np.array([temp_arr])
    temp_sc=scaler.transform(data)
    pred=rf.predict(temp_sc)[0]
    pred=round(pred, 2)
    print(temp_arr)     
    print(temp_sc)   
    print(pred)

    
    # return (temp_arr)

    return render_template('result.html', prediction=pred)


if __name__ == '__main__':
	app.run(debug=True)
