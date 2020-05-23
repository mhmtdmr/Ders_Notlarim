from matplotlib import pyplot as plt

x_ekseni = [1,2,3,4,5]
y_ekseni_ayse = [50,80,90,100,110]
y_ekseni_ali = [40,60,100,105,130]
y_ekseni_arzu = [55,70,110,115,150]

plt.title("Yaş-Boy Tablosu")
plt.xlabel("Yaşlar")
plt.ylabel("Boy Uzunluğu(cm)")

# el ile renk vs. verme işlemleri.
'''
plt.plot(x_ekseni,y_ekseni_ayse,color='b',linestyle='--',marker='.',label='Ayşe')
plt.plot(x_ekseni,y_ekseni_ali,'k-o',label='Ali') #color,linestyle ve marker'ı kısayol ile verdik.
plt.plot(x_ekseni,y_ekseni_arzu,color='#f54245',linestyle='-.',marker='o',linewidth=5,label='Arzu') #color'ı hex kodu ile verdik.
'''

# otomatik stil kullanımı için
plt.plot(x_ekseni,y_ekseni_ayse,label='Ayşe')
plt.plot(x_ekseni,y_ekseni_ali,label='Ali')
plt.plot(x_ekseni,y_ekseni_arzu,label='Arzu')


plt.legend() # plot etiketlerini göstermek için.
plt.grid(True)
plt.tight_layout()

# Üstteki stilleri silip aşağıdaki hazır stiller kullanılabilir.
# plt.style.use('ggplot')        # hazır style kullanımı
# plt.style.use('fivethirtyeight')
# print(plt.style.available)     # varolan stilleri listeleme
'''
['bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-bright', 
'seaborn-colorblind', 'seaborn-dark-palette', 'seaborn-dark', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 
'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 
'seaborn-whitegrid', 'seaborn', 'Solarize_Light2', 'tableau-colorblind10', '_classic_test']
'''
# https://matplotlib.org/tutorials/introductory/customizing.html?highlight=style

# hazır tema
plt.xkcd()

# otomatik kaydet
plt.savefig('cizim.png')

plt.show()

#######################################################################################################################
####   Grafik içinde kullanımı   ###
#######################################################################################################################
'''
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.pyplot import xticks,yticks

class Grafik:
    @staticmethod
    def Ciz(pencere,listx,listy,baslik):
        #Döviz grafik oluşturma bölümü
        figure = Figure(figsize=(20,6))
        g = figure.gca()
        g.plot(listx,listy)
        g.grid(True)
        figure.autofmt_xdate(rotation=45)

        g.set_title(baslik,fontsize=12)
        g.set_xlabel("Günler",fontsize=10)
        g.set_ylabel("Kur", fontsize=10)
        #Doviz grafiğini pencereye ekleme bölümü

        #tab_altin gelirse bu grafik tab_altin çerçevesine eklenir.
        canvas = FigureCanvasTkAgg(figure,master=pencere)
        canvas.get_tk_widget().grid(row=3,column=0,columnspan=10)
        canvas.draw()
'''


# Daha fazlası için: https://www.youtube.com/watch?v=UO98lJQ3QGI&list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_