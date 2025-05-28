
from content import menu, fastmatch, player, clear, matchconfig, difficult
from randomizator import matchgenerator
import time

ad = 0

def ffastmatch():   
    clear()
    print(f'> / * Number World * \ <')
    print(f'> {menu[ad]} ')
    lastoption = 0
    for i, menuoption in enumerate(fastmatch):
        print(f'{i + 1}- {menuoption}')
        lastoption = i + 2
    print(f'{lastoption}- Voltar')
    select = int(input('---> '))    

    
    if select == 1:
        clear()
        matchconfig['conta'] = fastmatch[select - 1]
        print(f'> / * Number World * \ <')
        print(f'> {menu[ad]} - {matchconfig['conta']}  ')

        #lista das dificuldades
        for i, dif in enumerate(difficult):
            print(f'{i + 1}- {dif}')
        print('💀 Selecione a Dificuldade 💀')            
        dif_select = int(input(f'--->'))

        #geração de conta baseada na dificuldade escolhida
        matchconfig['dificuldade'] = dif_select - 1
        matchgenerator(matchconfig)



    
    # Voltar
    if select == lastoption:
        return