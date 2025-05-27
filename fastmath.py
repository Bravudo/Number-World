
from content import menu, fastmatch, player, clear, matchconfig, difficult

import time

ad = 0

async def ffastmatch():   
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
        for i, dif in enumerate(difficult):
            print(f'{i + 1}- {dif}')
        print('💀 Selecione a Dificuldade 💀')            
        select == int(input(f'--->'))
        matchconfig['dificuldade'] = select
        await mathgenerator(matchconfig)



    
    # Voltar
    if select == lastoption:
        return