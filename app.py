from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('pred.pkl', 'rb'))
ac = pickle.load(open('ac.pkl', 'rb'))
bl = pickle.load(open('bl.pkl', 'rb'))
btn = pickle.load(open('btn.pkl', 'rb'))
bbl = pickle.load(open('bbl.pkl', 'rb'))
bngk = pickle.load(open('bngk.pkl', 'rb'))
diy = pickle.load(open('diy.pkl', 'rb'))
jkt = pickle.load(open('jkt.pkl', 'rb'))
jmb = pickle.load(open('jmb.pkl', 'rb'))
jbr = pickle.load(open('jbr.pkl', 'rb'))
jtn = pickle.load(open('jtn.pkl', 'rb'))
jtm = pickle.load(open('jtm.pkl', 'rb'))
klbr = pickle.load(open('klbr.pkl', 'rb'))
kltm = pickle.load(open('kltm.pkl', 'rb'))
kltng = pickle.load(open('kltng.pkl', 'rb'))
klsl = pickle.load(open('klsl.pkl', 'rb'))
kltu = pickle.load(open('kltu.pkl', 'rb'))
kria = pickle.load(open('kria.pkl', 'rb'))
ntb = pickle.load(open('ntb.pkl', 'rb'))
smsl = pickle.load(open('smsl.pkl', 'rb'))
smbr = pickle.load(open('smbr.pkl', 'rb'))
slt = pickle.load(open('slt.pkl', 'rb'))
smut = pickle.load(open('smut.pkl', 'rb'))
sltr = pickle.load(open('sltr.pkl', 'rb'))
slsl = pickle.load(open('slsl.pkl', 'rb'))
sltg = pickle.load(open('sltg.pkl', 'rb'))
lmpg = pickle.load(open('lmpg.pkl', 'rb'))
ria = pickle.load(open('ria.pkl', 'rb'))
malut = pickle.load(open('malut.pkl', 'rb'))
mlku = pickle.load(open('mlku.pkl', 'rb'))
papbr = pickle.load(open('papbr.pkl', 'rb'))
ppa = pickle.load(open('ppa.pkl', 'rb'))
slbr = pickle.load(open('slbr.pkl', 'rb'))
ntt = pickle.load(open('ntt.pkl', 'rb'))
grtl = pickle.load(open('grtl.pkl', 'rb'))
# wb = pickle.load(open('wb.pkl', 'rb'))

transf = pickle.load(open('transform.pkl', 'rb'))


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data=0)


@app.route('/predict', methods=['POST'])
def predict():
    place = request.form['b']
    
    data1 = request.form['a']
    
    month = request.form['c']
    if month.lower() == 'september':
        data2 = int(data1) + int(214)
    else:
        data2 = int(data1) + int(244)
    
    transformed_data = transf.transform([[data2]])

    if place.lower() == 'indonesia':
        pred = model.predict(transformed_data)
    elif (place.lower() == 'aceh') :
        pred = ac.predict(transformed_data)
    elif (place.lower() == 'bali') :
        pred = bl.predict(transformed_data)
    elif (place.lower() == 'banten') :
        pred = btn.predict(transformed_data)
    elif (place.lower() == 'babel') | (place.lower() == 'bangka belitung') :
        pred = bbl.predict(transformed_data)
    elif (place.lower() == 'bengkulu') :
        pred = bngk.predict(transformed_data)
    elif (place.lower() == 'diy') | (place.lower() == 'yogyakarta') :
        pred = diy.predict(transformed_data)
    elif (place.lower() == 'jakarta') :
        pred = jkt.predict(transformed_data)
    elif (place.lower() == 'jambi') :
        pred = jmb.predict(transformed_data)
    elif (place.lower() == 'jabar') | (place.lower() == 'jawa barat'):
        pred = jbr.predict(transformed_data)
    elif (place.lower() == 'jateng') | (place.lower() == 'jawa tengah'):
        pred = jtn.predict(transformed_data)
    elif (place.lower() == 'jatim') | (place.lower() == 'jawa timur'):
        pred = jtm.predict(transformed_data)
    elif (place.lower() == 'kalbar') | (place.lower() == 'kalimantan barat'):
        pred = klbr.predict(transformed_data)
    elif (place.lower() == 'kaltim') | (place.lower() == 'kalimantan timur'):
        pred = kltm.predict(transformed_data)
    elif (place.lower() == 'kalteng') | (place.lower() == 'kalimantan tengah'):
        pred = kltng.predict(transformed_data)
    elif (place.lower() == 'kalsel') | (place.lower() == 'kalimantan selatan'):
        pred = klsl.predict(transformed_data)
    elif (place.lower() == 'kaltara') | (place.lower() == 'kalimantan utara'):
        pred = kltu.predict(transformed_data)
    elif (place.lower() == 'kep riau') | (place.lower() == 'kepulauan riau'):
        pred = kria.predict(transformed_data)
    elif (place.lower() == 'ntb') :
        pred = ntb.predict(transformed_data)
    elif (place.lower() == 'sumsel') | (place.lower() == 'sumatra selatan'):
        pred = smsl.predict(transformed_data)
    elif (place.lower() == 'sumbar') | (place.lower() == 'sumatra barat'):
        pred = smbr.predict(transformed_data)
    elif (place.lower() == 'sulut') | (place.lower() == 'sulawesi utara'):
        pred = slt.predict(transformed_data)
    elif (place.lower() == 'sumut') | (place.lower() == 'sumatra utara'):
        pred = smut.predict(transformed_data)
    elif (place.lower() == 'sultra') | (place.lower() == 'sulawesi tenggara'):
        pred = sltr.predict(transformed_data)
    elif (place.lower() == 'sulsel') | (place.lower() == 'sulawesi selatan'):
        pred = slsl.predict(transformed_data)
    elif (place.lower() == 'sulteng') | (place.lower() == 'sulawesi tengah'):
        pred = sltg.predict(transformed_data)
    elif (place.lower() == 'lampung') :
        pred = lmpg.predict(transformed_data)
    elif (place.lower() == 'riau') :
        pred = ria.predict(transformed_data)
    elif (place.lower() == 'malut') | (place.lower() == 'maluku utara'):
        pred = malut.predict(transformed_data)
    elif (place.lower() == 'maluku') :
        pred = mlku.predict(transformed_data)
    elif (place.lower() == 'papbar') | (place.lower() == 'papua barat'):
        pred = papbr.predict(transformed_data)
    elif (place.lower() == 'papua') :
        pred = ppa.predict(transformed_data)
    elif (place.lower() == 'sulbar') | (place.lower() == 'sulawesi barat'):
        pred = slbr.predict(transformed_data)
    elif (place.lower() == 'ntt') :
        pred = ntt.predict(transformed_data)
    elif (place.lower() == 'gorontalo') :
        pred = grtl.predict(transformed_data)
    else:
        pred = 'wrong input'
    
    return render_template('index.html', data=int(pred[0,0]), date = data1, month = month, place = place.lower())


if __name__ == "__main__":
    app.run(debug=False)