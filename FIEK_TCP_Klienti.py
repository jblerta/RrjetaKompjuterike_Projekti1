import socket
import sys


serverName = 'localhost'
klientPort = 5555
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((serverName , 12000))
print("Mireserdhet une jam Klienti\n")
print('FIEK-TCP klienti')
print('============================================================================')
print('''Opsionet:
    1.IPADDR - Kthen IP adresen e klientit.
    2.PORTNR - Kthen portin e klientit.
    3.BASHKETINGELLORE - Gjen numrin e bashketingelloreve ne tekst.
    4.PRINTO - Kthen fjalin e shtypur ne tekst.
    5.HOST - Kthen emrin e kompjuterit/hostit
    6.KOHA - Percakton kohen aktuale ne server 
    7.LOJA - Kthen 7 numra nga rangu [1,49].
    8.FIBONACCI - Gjen numrin FIBONACCI si rezultat i parametrit te dhene hyres.
    9.KONVERTO - Konvertime te ndryshme.
    10.GUESSGAME - Duhet te gjeni numrin e kerkuar.
    11.HOROSKOPIKINEZ - Kthen shenjen e juaj ne horoskopin kinez.''')
print('=============================================================================')
while True:
    print('_____________________________________________________________________________________')
    var=input('--> Shkruani kerkesen tuaj ose shtypni 0 per shkeputje te lidhjes me serverin: ')
    mesazhi= var.upper()

    if mesazhi=='PORTNR':
        s.sendall(str.encode(mesazhi))
        porti= str(klientPort)
        s.sendall(str.encode(porti))
        data=s.recv(128).decode('utf-8')
        print('>> Porti juaj eshte: '+str(klientPort))
    elif mesazhi == 'PRINTO':
        s.sendall(str.encode(mesazhi))
        fjalia = input('<< Shkruani nje fjali:')
        s.sendall(str.encode(fjalia))
        data=s.recv(128).decode('utf-8')
        print('>> Fjalia e dhene eshte:' +data)
    elif mesazhi=='HOST':
        s.sendall(str.encode(mesazhi))
        data=s.recv(128).decode('utf-8')
        print('>> Hosti juaj eshte: '+data)
    elif mesazhi== 'IPADDR':
        s.sendall(str.encode(mesazhi))
        data=s.recv(128).decode('utf-8')
        print('>> IP e juaj eshte: ' + data)
       
    elif mesazhi=='FAKTORIEL':
        s.sendall(str.encode(mesazhi))
        numri=input('<< Jepni numrin: ')
        s.sendall(str.encode(numri))
        data=s.recv(128).decode('utf-8')
        print('>> Faktorieli i '+ str(numri)+' eshte '+str(data))
    elif mesazhi=='BASHKETINGELLORE':
        s.sendall(str.encode(mesazhi))
        Fjalia=input('<< Shtypni fjaline tuaj: ')
        s.sendall(str.encode(Fjalia))
        data=s.recv(128).decode('utf-8')
        print(f'>> Teksti i derguar permbane {data} bashketingellore.')
    elif mesazhi == 'KOHA':
        s.sendall(str.encode(mesazhi))
        data=s.recv(128).decode('utf-8')
        print('>> Koha aktuale ne server: '+data)   
    elif mesazhi =='LOJA':
        s.sendall(str.encode(mesazhi))
        data=s.recv(128).decode('utf-8')
        print('>> Numrat random te gjeneruar jane: '+data)
    elif mesazhi == 'FIBONACCI':
        s.sendall(str.encode(mesazhi)) 
        numri= input('<< Jepni nje numer')
        s.sendall(str.encode(numri))
        data=s.recv(128).decode('utf-8')
        print('>> Fibonacci i numrit te dhene eshte ' +data)
    elif mesazhi=='HOROSKOPIKINEZ':
        s.sendall(str.encode(mesazhi)) 
        numri= input('<< Jepni vitin e lindjes: ')
        s.sendall(str.encode(numri))
        data=s.recv(128).decode('utf-8')
        print(data)
    elif mesazhi=='GUESSGAME':
         s.sendall(str.encode(mesazhi))
         numri=input('<< Jepni nje numer nga 1 deri 10: ')
         s.sendall(str.encode(numri))
         data=s.recv(128).decode('utf-8')
         print(data)
    elif mesazhi == 'KONVERTO': 
        s.sendall(str.encode(mesazhi))
        print('>> Ju mund te beni keto konvertime: \nCelsiusToKelvin \nKelvinToCelsius \nCelsiusToFahrenheit \nFahrenheitToCelsius \nKelvinToFahrenheit \nFahrenheitToKelvin \nPoundToKilogram \nKilogramToPound')
        zgjedhja = input('Zgjedhni nje opsion: ')
        s.sendall(str.encode(zgjedhja))
        sasia = input('<< Jepni numrin qe doni te konvertoni')
        s.sendall(str.encode(sasia))
        data=s.recv(128).decode('utf-8')
        print('>> Madhesia e konvertuar: '+data)
    elif mesazhi=='0':
        break
    else:
        print('Komanda qe keni shtypur nuk eshte valide!!')
    print()
s.close()
