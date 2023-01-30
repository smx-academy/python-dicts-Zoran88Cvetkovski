 # 1. Da se kreira dictionary so 3 elementi po vas izbor i da se ispecati posledniot element
info = {    
    "ime":"Zoran",
    "prezime":"Cvetkovski",
    "godini":34
}
print (info["godini"])

#2.  Da se kreiara prazen dictionary, korisnikot da vnese 2 broevi koi ke se dodadt vo dictionary. 
# Da se izvrsat 4te osnovni matematicki operacii i da se dodadat rezultatite vo dictionary vo razlicni keys
kolekcija ={}
print ("Potrebno e da vnesete dva broja")
print ("Vnesete go prviot broj")
broj = int (input())
kolekcija["Br1"]=broj
print ("Vnesete go vtoriot broj")
broj = int (input())
kolekcija["Br2"]=broj
zbir=kolekcija["Br1"]+kolekcija["Br2"]
kolekcija["zbir"]=zbir
razlika=kolekcija["Br1"]-kolekcija["Br2"]
kolekcija ["razlika"] =razlika
mnozenje=kolekcija["Br1"]*kolekcija["Br2"]
kolekcija["mnozenje"]=mnozenje
delenje=kolekcija["Br1"]/kolekcija["Br2"]
kolekcija["delenje"]= delenje
print (kolekcija)

#3. Da se kreira programa vo koja korisnikot ke moze da vnese strani na pravoagolnik, da se vnesat vo dictionary,  
# da se presmeta plostina i perimetar koja ke bide zacuvana vo dictinary. Da se proveri dali plostinata ili perimetarot se pogolemi. 

pravoagolnik ={}
print ("Vnesete ja ednata strana na pravoagolniik")
p1=int (input ())
pravoagolnik["edna_strana"]=p1
print ("Vnesete ja vtorata strana na pravoagolnik")
p2=int (input())
pravoagolnik["vtora_strana"]=p2
perimetar = 2*p1+2*p2
pravoagolnik ["perimetar"]=perimetar
ploshtina= p1*p2
pravoagolnik["ploshtina"]=ploshtina
if perimetar>ploshtina:
    print("Perimetarot na pravoagolnikot e pogolem od negovata plostina")
else:
    print("Plostinata na pravoagolnikot e pogolema od negoviot perimetar")


#4.  Da se kreira programa koja ke bide za potrebide vo nekoja prodavnica. Da se kreira dictionary koj ke ima 2 indexi, produkti, 
# ceni koi kkao podatoci ke imaat prazni listi. Koristnikot da moze da vnesuva produkti i ceni na produktite se dodeka ne izbere deka poveke
# ne saka da vnese. Koga ke prestane da vnesuva produkti da se presmeta kolku treba da plati i da se zacuva vo nov index. 
#  Da mu se dade opcija na korisnikot da plati, d a se presmeta dali treba da se vrati kusur ili ne. 
# Ako treba da se zacuva vo dictionary kolku kusur treba da se vrati. Ako ne treba da se zacuva deka smetkata e platena.
produkt = []
cena=[]
dane ="da"
while dane =="da":
    print ("Vnesete go imeto na proizvodot")
    proizvod=str (input())
    produkt.append(proizvod)
    print ("Vneseto ja cenata na proizvodot {}".format(proizvod))
    iznos = int (input())
    cena.append(iznos)
    print ("Dali sakate da vnesete nov proizvod vo vasata lista:")
    dane=input ("Odgovorite so 'da' dokolku sakate da vnesete nov produkt: ")
prodavnica =dict(zip(produkt,cena))
print ("Vkupno za naplata {} mkd".format (sum(cena)))
prodavnica["Za_naplata"]=sum(cena)
print ("So kolku MKD ke platite: ")
plati= int (input ())
while True:
    if sum(cena)>plati:
        print("Ve molime uplatete {} MKD. Vnesete so kolku MKD ke platite".format(sum(cena)))
        plati =int (input())
    else:
        break
kusur=plati - sum(cena)
if kusur<=0:
    print ("Smetkata e platena")
    prodavnica ["kusur"]= ("Smetkata e platena")
else:
    print ("Kusur za vrakanje iznesuva: {} MKD".format (kusur))
    prodavnica["kusur"]= kusur