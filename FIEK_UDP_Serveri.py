from socket import * 
import sys 
from _thread import * 
import datetime
import random 
import os 

host = 'localhost'
port = 12000
serverSocket= socket(AF_INET , SOCK_DGRAM)

try: 
    serverSocket.bind((host,port))
except: 
    print('Lidhja me klientin nuk u realizu!')
    sys.exit()

print('Serveri u startua ne localhost '+str(port))
print('Serveri eshte i gatshem te pranoje kerkesa')

def faktoriel(n):
    a=1
    while int(n)>=1:
        a=a*int(n)
        n=int(n)-1
    return a

def bashketingellore(fjalia):
    bashketingelloret=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z']
    numratori=0
    for x in fjalia:
        if x.lower() in bashketingelloret:
            numratori+=1
    return numratori

def fibonacci(number):
     x=1
     y=1
     for numeruesi in range(2,number):
            fibonaccia = x + y;
            x = y;
            y = fibonaccia;
     return fibonaccia

def IP():
    return gethostbyname(gethostname())
def HOST(): 
    return gethostname()

def koha():
    T=datetime.datetime.now()
    T = T.strftime('%H:%M:%S')
    return T

def konverto(zgjedh, vlera):
    if zgjedh=="CelsiusToKelvin":
        rezultati=vlera+273

    elif zgjedh=="KelvinToCelsius":
        rezultati=vlera-273 

    elif zgjedh=="CelsiusToFahrenheit":
        rezultati = 9.0/5.0 * vlera + 32 

    elif zgjedh=="FahrenheitToCelsius":
        rezultati = (vlera - 32) * 5.0/9.0 

    elif zgjedh=="KelvinToFahrenheit":
         rezultati = ((9.0/5.0)*(vlera-273)) + 32 
     
    elif zgjedh=="FahrenheitToKelvin":
         rezultati = (5.0/ 9.0)*(vlera-32)+273

    elif zgjedh=="PoundToKilogram":
         rezultati = vlera * 0.453592

    elif zgjedh=="KilogramToPound":
        rezultati = vlera/0.453592
    else:
        rezultati="Gabim"
    return rezultati

def LOJA():
    nums = random.sample(range(1,49),7)
    
    numrat = str(nums)
    return numrat

def guessgame(nr):
    secret_number=random.randint(1,10)
    sn=str(secret_number)
    print("Numri i kerkuar eshte: "+sn)
    if nr<11:
       if nr==secret_number:
         rezultati=">> You Won :)"
       else:
         rezultati=">> You loose :( \n  Numri i kerkuar eshte: "+sn
    else:
        rezultati="->GABIM:Numri duhet te jete nga 1 deri te 10."
    return rezultati

def HoroskopiKinez(viti):
    if viti in [1924, 1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020]:
        rezultati=">> Miu: i zgjuar,i shkathet,i gjithanshem,i sjellshem."
    elif viti in [1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021]:
        rezultati=">> Bualli: i përkushtuar,i besueshem,i forte,i vendosur."
    elif viti in [1926, 1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022]:
        rezltati=">> Tigri: konkurrues,trim,me besim ne vete."
    elif viti in [1927, 1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023]:
        rezultati=">> Lepuri: i qete, elegant, i sjellshem, i pergjegjshem."
    elif viti in [1928, 1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024]:
        rezultati=">> Dragoi: besim ne vete,inteligjent,entuziast."
    elif viti in [	1929, 1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025]:
        rezultati=">> Gjarperi: enigmatik,inteligjent,i mençur."
    elif viti in [1930, 1942, 1954, 1966, 1978, 1990, 2002, 2014, 2026]:
        rezultati=">> Kali: i gjalle,aktiv,energjik."
    elif viti in [1931, 1943, 1955, 1967, 1979, 1991, 2003, 2015, 2027]:
        rezultati=">> Dhia: qetë,i bute,dashamires."
    elif viti in [1932, 1944, 1956, 1968, 1980, 1992, 2004, 2016, 2028]:
        rezultati=">> Majmuni: i mprehte,i zgjuar,kurioziteti."
    elif viti in [1933, 1945, 1957, 1969, 1981, 1993, 2005, 2017, 2029]:
        rezultati=">> Gjeli: vemendshem, i zellshem, i guximshem."
    elif viti in [1934, 1946, 1958, 1970, 1982, 1994, 2006, 2018, 2030]:
        rezultati=">> Qeni: i dashur, i sinqerte, i kujdesshem."
    elif viti in [1935, 1947, 1959, 1971, 1983, 1995, 2007, 2019, 2031]:
        rezultati=">> Derri: meshireplote,bujar,i zellshem."
    else:
        rezultati=">> Viti juaj  nuk eshte ne list"
    return rezultati

def clientthread (input , address):
    try:
        data = input.decode('utf-8')
    except IOError:
        print('Ka ndodhur nje gabim')
    komanda=str(data).rsplit(' ')
    fjalia=''
    i=len(komanda)
    for fjala in range(1,i):
        fjalia=fjalia+komanda[fjala]
        if(fjala!=i):
            fjalia+=' ';
    fund=str(fjalia)
    if komanda[0]=='FAKTORIEL':
        serverSocket.sendto(str(faktoriel(komanda[1])).encode('utf-8') , address)
    elif komanda[0]=='BASHKETINGELLORE':
        serverSocket.sendto(str(bashketingellore(fund)).encode('utf-8') , address)
    elif komanda[0]=='HOST':
        serverSocket.sendto(str(HOST()).encode('utf-8'), address)
    elif komanda[0]=='FIBONACCI':
        nr=int(komanda[1])
        serverSocket.sendto(str(fibonacci(nr)).encode('utf-8'),address)
    elif komanda[0]== 'IPADDR':
        serverSocket.sendto(str(IP()).encode('utf-8') , address)
    elif komanda[0]=='PORTNR':
        serverSocket.sendto(str(port).encode('utf-8') , address)
    elif komanda[0] == 'PRINTO':
        serverSocket.sendto(str(fund).encode('utf-8') , address)
    elif komanda[0]== 'KOHA':
        serverSocket.sendto(str(koha()).encode('utf-8') , address)
    elif komanda[0] == 'LOJA':
        serverSocket.sendto(str(LOJA()).encode('utf-8') , address)
    elif komanda[0] == 'KONVERTO':
        print('Klienti ka zgjedhur te konvertoj ' + komanda[1])
        nr=int(komanda[2])
        serverSocket.sendto(str(konverto(komanda[1], nr)).encode('utf-8'),address)
    elif komanda[0]=='GUESSGAME':
        nr=int(komanda[1])
        serverSocket.sendto(str(guessgame(nr)).encode('utf-8'),address)
    elif komanda[0]=='HOROSKOPIKINEZ':
        nr=int(komanda[1])
        serverSocket.sendto(str(HoroskopiKinez(nr)).encode('utf-8'),address)
    else:
        serverSocket.sendto(str('GABIM!').encode('utf-8'))
while True:
    data , address=serverSocket.recvfrom(128)
    print('Serveri eshte lidh me' + str(address))
    start_new_thread(clientthread , (data,address,))
serverSocket.close()

