from socket import *
import sys

host='localhost'
port=12000
klientSocket=socket(AF_INET, SOCK_DGRAM)
print('Fiek Klienti:')
print('FIEK-UDP klienti')
print('=============================================================')
print('Opsionet:')
print('1.IPADDR \n2.PORTNR \n3.BASHKETINGELLOREE \n4.PRINTO \n5.HOST \n6.KOHA \n7.LOJA \n8.FIBONACCI {hapsire} Numri \n9.KONVERTO {hapsire} Opsioni {hapsire} vlera \nOpsionet:CelsiusToKelvin<-->KelvinToCelsius\n\t CelsiusToFahrenheit<-->FarenheitToCelsius\n\t KelvinToFahrenheit<-->FahrenheitToKelvin \n\t PoundToKilogram<-->KilogramToPound \n10.GUESSGAME {hapesire} Numri ndermjet 1-10 \n11.HOROSKOPIKINEZ {hapesire} viti i lindjes')
var=input('\nShkruani kerkesen tuaj ose shtypni 0 per shkeputje te lidhjes me serverin: ')
mesazhi=var.upper()  

address = (host,port)

while(mesazhi!='' and mesazhi!='0'):
    data=''
    if 'FAKTORIEL' in mesazhi: 
        klientSocket.sendto(mesazhi.encode(), (host,port))
        data=klientSocket.recv(128).decode('utf-8')
        print('Faktorieli i numrit te dhene eshte: '+ str(data))
        mesazhi=input('Shkruani kerkesen tuaj ose shtypni 0 per shkeputje te lidhjes me serverin: ')
    elif 'BASHKETINGELLORE' in mesazhi: 
        klientSocket.sendto(mesazhi.encode(), (host,port))
        data=klientSocket.recv(128).decode('utf-8')
        print('Numri i bashketingelloreve ne fjaline e dhene eshte :'+str(data))
        mesazhi=input('Shkruani kerkesen tuaj ose shtypni 0 per shkeputje te lidhjes me serverin: ')
    elif 'HOST' in mesazhi: 
        klientSocket.sendto(mesazhi.encode(), (host,port))
        data=klientSocket.recv(128).decode('utf-8')
        print('Emri i hostit tuaj eshte: '+ str(data))
        mesazhi=input('Shkruani kerkesen tuaj ose shtypni 0 per shkeputje te lidhjes me serverin: ')
    elif 'FIBONACCI' in mesazhi:
        klientSocket.sendto(mesazhi.encode() , (host , port))
        data=klientSocket.recv(128).decode('utf-8')
        print('Fibonacci i numrit te dhene eshte: '+str(data))
        mesazhi=input('Shkruani kerkesen tuaj ose shtypni 0 per shkeputje te lidhjes me serverin: ')
    elif 'IPADDR' in mesazhi: 
        klientSocket.sendto(mesazhi.encode(), address)
        data=klientSocket.recv(128).decode('utf-8')
        print('IP e juaj eshte: '+data)
        mesazhi=input('Shkruani kerkesen tuaj ose shtypni 0 per shkeputje te lidhjes me serverin: ')
    elif 'PORTNR' in mesazhi: 
        klientSocket.sendto(mesazhi.encode(), address)
        data=klientSocket.recv(128).decode('utf-8')
        print('Porti juaj eshte: '+str(data))
        mesazhi=input('Shkruani kerkesen tuaj ose shtypni 0 per shkeputje te lidhjes me serverin: ')
    elif 'PRINTO' in mesazhi: 
        klientSocket.sendto(mesazhi.encode(), address)
        data=klientSocket.recv(128).decode('utf-8')
        print('Fjalia e dhene eshte:' +data)
        mesazhi=input('Shkruani kerkesen tuaj ose shtypni 0 per shkeputje te lidhjes me serverin: ')
    elif 'KOHA' in mesazhi: 
        klientSocket.sendto(mesazhi.encode(), address)
        data=klientSocket.recv(128).decode('utf-8')
        print(data)
        mesazhi=input('Shkruani kerkesen tuaj ose shtypni 0 per shkeputje te lidhjes me serverin: ')
    elif 'LOJA' in mesazhi: 
        klientSocket.sendto(mesazhi.encode(), address)
        data=klientSocket.recv(128)
        print('Numrat e gjeneruar jane: '+str(data))
        mesazhi=input('Shkruani kerkesen tuaj ose shtypni 0 per shkeputje te lidhjes me serverin: ')
    elif 'KONVERTO' in mesazhi: 
        klientSocket.sendto(mesazhi.encode(), address)
        data=klientSocket.recv(128)
        print(data)
        mesazhi=input('Shkruani kerkesen tuaj ose shtypni 0 per shkeputje te lidhjes me serverin: ')
    elif 'GUESSGAME'in mesazhi:
        klientSocket.sendto(mesazhi.encode() , (host , port))
        data=klientSocket.recv(128).decode('utf-8')
        print(data)
        mesazhi=input('Shkruani kerkesen tuaj ose shtypni 0 per shkeputje te lidhjes me serverin: ')
    elif 'HOROSKOPIKINEZ' in mesazhi:
        klientSocket.sendto(mesazhi.encode() , (host , port))
        data=klientSocket.recv(128).decode('utf-8')
        print(data)
        mesazhi=input('Shkruani kerkesen tuaj ose shtypni 0 per shkeputje te lidhjes me serverin: ')
    else:
        print('Shtypni nje kerkese valide')
        break 
klientSocket.close()

