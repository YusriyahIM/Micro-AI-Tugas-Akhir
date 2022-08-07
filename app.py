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

@app.route('/predict/', methods=['POST'])
def predict():
    place = request.form['b']
    
    data1 = request.form['a']
    
    month = request.form['c']
    if month == 'agustus':
        data2 = int(data1) + int(214)
    else:
        data2 = int(data1) + int(244)
    
    transformed_data = transf.transform([[data2]])

    if place == 'Indonesia':
        pred = model.predict(transformed_data)
    elif (place == 'Aceh') :
        pred = ac.predict(transformed_data)
    elif (place == 'Bali') :
        pred = bl.predict(transformed_data)
    elif (place == 'Banten') :
        pred = btn.predict(transformed_data)
    elif (place == 'babel') | (place == 'Kep. Bangka Belitung') :
        pred = bbl.predict(transformed_data)
    elif (place == 'Bengkulu') :
        pred = bngk.predict(transformed_data)
    elif (place == 'diy') | (place == 'DI Yogyakarta') :
        pred = diy.predict(transformed_data)
    elif (place == 'DKI Jakarta') :
        pred = jkt.predict(transformed_data)
    elif (place == 'Jambi') :
        pred = jmb.predict(transformed_data)
    elif (place == 'jabar') | (place == 'Jawa Barat'):
        pred = jbr.predict(transformed_data)
    elif (place == 'jateng') | (place == 'Jawa Tengah'):
        pred = jtn.predict(transformed_data)
    elif (place == 'jatim') | (place == 'Jawa Timur'):
        pred = jtm.predict(transformed_data)
    elif (place == 'kalbar') | (place == 'Kalimantan Barat'):
        pred = klbr.predict(transformed_data)
    elif (place == 'kaltim') | (place == 'Kalimantan Timur'):
        pred = kltm.predict(transformed_data)
    elif (place == 'kalteng') | (place == 'Kalimantan Tengah'):
        pred = kltng.predict(transformed_data)
    elif (place == 'kalsel') | (place == 'Kalimantan Selatan'):
        pred = klsl.predict(transformed_data)
    elif (place == 'kaltara') | (place == 'Kalimantan Utara'):
        pred = kltu.predict(transformed_data)
    elif (place == 'Kep. Riau') | (place == 'kepulauan riau'):
        pred = kria.predict(transformed_data)
    elif (place == 'Nusa Tenggara Barat') :
        pred = ntb.predict(transformed_data)
    elif (place == 'sumsel') | (place == 'Sumatra Selatan'):
        pred = smsl.predict(transformed_data)
    elif (place == 'sumbar') | (place == 'Sumatra Barat'):
        pred = smbr.predict(transformed_data)
    elif (place == 'sulut') | (place == 'Sulawesi Utara'):
        pred = slt.predict(transformed_data)
    elif (place == 'sumut') | (place == 'Sumatra Utara'):
        pred = smut.predict(transformed_data)
    elif (place == 'sultra') | (place == 'Sulawesi Tenggara'):
        pred = sltr.predict(transformed_data)
    elif (place == 'sulsel') | (place == 'Sulawesi Selatan'):
        pred = slsl.predict(transformed_data)
    elif (place == 'sulteng') | (place == 'Sulawesi Tengah'):
        pred = sltg.predict(transformed_data)
    elif (place == 'Lampung') :
        pred = lmpg.predict(transformed_data)
    elif (place == 'Riau') :
        pred = ria.predict(transformed_data)
    elif (place == 'malut') | (place == 'Maluku Utara'):
        pred = malut.predict(transformed_data)
    elif (place == 'Maluku') :
        pred = mlku.predict(transformed_data)
    elif (place == 'papbar') | (place == 'Papua Barat'):
        pred = papbr.predict(transformed_data)
    elif (place == 'Papua') :
        pred = ppa.predict(transformed_data)
    elif (place == 'sulbar') | (place == 'Sulawesi Barat'):
        pred = slbr.predict(transformed_data)
    elif (place == 'Nusa Tenggara Timur') :
        pred = ntt.predict(transformed_data)
    elif (place == 'Gorontalo') :
        pred = grtl.predict(transformed_data)
    else:
        pred = 'wrong input'
    
    return render_template('index.html', data=int(pred[0,0]), date = data1, month = month, place = place)


if __name__ == "__main__":
    app.run(debug=False)