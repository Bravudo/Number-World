from content import fastmatch, challengematch, difficult
import time


def randomAd(config):
    dificuldade = config['dificuldade']
    if dificuldade == difficult[dificuldade]:
        print('funcionou')
       


allMath = {
    'Adição': randomAd
}
       
def matchgenerator(config):
    print(f'{config}')
    conta = allMath.get(config['conta'])
    if conta:
        conta(config)
        time.sleep(5)