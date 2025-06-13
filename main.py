#all imports
import time


from content import menu, player, fastmatch, clear
from fastmath import ffastmatch
import randomizator
import asyncio




def NumberWorld():
    while True:
     clear()
     print('> / * Number World * \ <')
     for i, menuoption in enumerate(menu):
        print(f'{i + 1}- {menuoption}')
        i += 1
     select = int(input('---> '))

     if select == 1:
        ffastmatch()
   

NumberWorld()