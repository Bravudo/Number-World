import os

player = { 'nome': '', 'level': 0, 'xp': 0, 'xpLimit': 10}
menu = ['Partida Rapida', 'Desafio Superior', 'Partida Personalizada', 'Perfil']

fastmatch = ['Adição', 'Subtração', 'Multiplicação','Divisão']

challengematch = ['Equação de Primeiro Grau', 'Equação de Segundo Grau']

difficult = ['Facíl', 'Médio', 'Difícil', 'Insano']

matchconfig = { 'conta': '', 'dificuldade': 0, 'Tempo': 0 }

#limpar terminal
def clear():
   os.system('cls' if os.name == 'nt' else 'clear')