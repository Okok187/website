from flask import *
import random
app = Flask(__name__)
yazi=["yazı","tura"]
liste=["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
       "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
       "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.",
       "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor."]
@app.route("/")
def ok():
    return"<a href='/rastgele'>Rastgele bir gerçeği görüntüle!</a>"
@app.route("/rastgele")
def hello():
    return F"{random.choice(liste)}"
@app.route("/yazitura")
def yazitura():
    return F"{random.choice(yazi)}"
app.run(debug=True)
