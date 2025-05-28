from content import fastmatch, challengematch, difficult
import time


def randomAd(config):
    dificuldade_selecionada = config['dificuldade']
  
    if dificuldade_selecionada == 0:
        print('Dificuldade Facil pronta pra iniciar')
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
 