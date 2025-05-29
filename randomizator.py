from content import fastmatch, challengematch, difficult, clear, matchconfig, menu, player
import time
import random

xpfacil = 5
xpmedio = 10
xpdificil = 20
xpinsano = 40


def randomAd(config):
    cadernoContas = []
    dificuldade_selecionada = config['dificuldade']
    acerto = 0
  
    if dificuldade_selecionada == 0:
        clear()
        print(f'> / * Number World * \ <')
        print(f'> {menu[0]} - {matchconfig['conta']} - {difficult[0]} ')
        print('Carregando...')
        time.sleep(2)
        for i in range(10):
            minimo = 3
            limite = 40
            n1 = random.randint(minimo,limite)
            n2 = random.randint(minimo,limite)

            conta = { 'a': n1, 'b': n2, 'resultado': n1+n2 }
            cadernoContas.append(conta)
        start = time.time()    
        for i, book in enumerate(cadernoContas):
     
            clear()
            print(f'> / * Number World * \ <')
            print(f'> {menu[0]} - {matchconfig['conta']} - {difficult[0]} ')
            print(f'Questão {i+1} - Acertos: {acerto}/{len(cadernoContas)}')
            print(f'{book['a']} + {book['b']} = ?')
            print()
            resultinput = int(input('Resposta: '))
            if resultinput == book['resultado']:
                acerto += 1 
        fim = time.time() - start

        print(f'Acertos {acerto}/{len(cadernoContas)} - Tempo: {fim:.0f}s')
        if acerto > 7:
            player['xp'] += xpfacil
            print(f'+{xpfacil} xp')
        time.sleep(5)


    if dificuldade_selecionada == 1:
        clear()
        print(f'> / * Number World * \ <')
        print(f'> {menu[0]} - {matchconfig['conta']} - {difficult[1]} ')
        print('Carregando...')
        time.sleep(2)
        for i in range(10):
            minimo = 50
            limite = 150
            n1 = random.randint(minimo,limite)
            n2 = random.randint(minimo,limite)

            conta = { 'a': n1, 'b': n2, 'resultado': n1+n2 }
            cadernoContas.append(conta)
        start = time.time()    
        for i, book in enumerate(cadernoContas):
     
            clear()
            print(f'> / * Number World * \ <')
            print(f'> {menu[0]} - {matchconfig['conta']} - {difficult[1]} ')
            print(f'Questão {i+1} - Acertos: {acerto}/{len(cadernoContas)}')
            print(f'{book['a']} + {book['b']} = ?')
            print()
            resultinput = int(input('Resposta: '))
            if resultinput == book['resultado']:
                acerto += 1 
        fim = time.time() - start

        print(f'Acertos {acerto}/{len(cadernoContas)} - Tempo: {fim:.0f}s')
        if acerto > 7:
            player['xp'] += xpmedio
            print(f'+{xpmedio} xp')
        time.sleep(5)
       


allMath = {
    'Adição': randomAd
}
       
def matchgenerator(config):
    print(f'{config}')
    conta = allMath.get(config['conta'])
    if conta:
        conta(config)
    else:
        print(f"⚠️ Operação '{config['conta']}' não encontrada!")
        time.sleep(5)
 