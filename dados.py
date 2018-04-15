import csv
def carregar_acessos():
    x = []
    y = []
    arquivo = open('acesso.csv', 'r', encoding='utf-8')
    leitor = csv.reader(arquivo)
    next(leitor) 
    for home, como_funciona, contato, comprou in leitor:
        x.append(   [int(home), 
                     int(como_funciona),
                     int(contato)])
        y.append(int(comprou))
    return x, y
def carregar_buscas():
    x = []
    y = []
    arquivo = open('busca.csv', 'r')
    leitor = csv.reader(arquivo)
    next(leitor)
    for home, busca, logado, comprou in leitor:
        dado = [int(home), busca, int(logado)]
        x.append(dado)
        y.append(int(comprou))
    return x, y

