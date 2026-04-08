cont = 0
soma_dois = 0

while cont < 5:

    n = int(input('me fale um número :'))
    
    if n % 2 == 0 :
        soma_dois += n
        print('Esse número é par')
        print('A soma dos números pares é :',soma_dois)
    else:
       print('Esses numeros não são compativeis')
    
    if soma_dois <= 25:
        print('Ele pertence ao intervalo de 0,25')
    elif soma_dois <= 50:
        print('Ele pertence ao intervalo de 25,50')
    elif soma_dois <= 75:
        print('Ele pertence ao intervalo de 50,75')
    elif soma_dois <= 100:
        print('Ele pertence ao intervalo de 75,100')
    else:
        print('Fora do intervalo')    
        cont += 1
