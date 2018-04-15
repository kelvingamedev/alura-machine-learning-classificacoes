import pandas as pd
df = pd.read_csv('buscas2.csv')
x_df = df[['home', 'busca', 'logado']]
y_df = df['comprou']
xDummies_df = pd.get_dummies(x_df)
yDummies_df = y_df
x = xDummies_df.values
y = yDummies_df.values

porcentagem_de_treino = 0.8
porcentagem_de_teste = 0.1
tamanho_de_treino = int(porcentagem_de_treino * len(y))
tamanho_de_teste = int(porcentagem_de_teste * len(y))
tamanho_de_validacao = len(y) - tamanho_de_treino - tamanho_de_teste
treino_dados = x[:tamanho_de_treino]
treino_marcacoes = y[:tamanho_de_treino]
fim_de_treino = tamanho_de_treino + tamanho_de_teste
teste_dados = x[tamanho_de_treino:fim_de_treino]
teste_marcacoes = y[tamanho_de_treino:fim_de_treino]
validacao_dados = x[fim_de_treino:]
validacao_marcacoes = y[fim_de_treino:]

def fit_and_predict(modelo, treino_dados, treno_marcacoes,
                    teste_dados, teste_marcacoes, nome):
    modelo.fit(treino_dados, treino_marcacoes)
    resultado = modelo.predict(teste_dados)
    acertos = resultado == teste_marcacoes
    total_de_acertos = sum(acertos)
    total_de_elementos = len(teste_marcacoes)
    taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos
    print('Taxa de acerto {0}:'.format(nome), taxa_de_acerto, '%')
    return taxa_de_acerto

from sklearn.naive_bayes import MultinomialNB
modeloMultinomial = MultinomialNB()
resultadoMultinomial = fit_and_predict(modeloMultinomial, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes, 'MultinomialNB')

from sklearn.ensemble import AdaBoostClassifier
modeloAdaBoost = AdaBoostClassifier()
resultadoAdaBoost = fit_and_predict(modeloAdaBoost, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes, 'AdaBoostClassifer')

from collections import Counter
acerto_base = max(Counter(teste_marcacoes).values())
taxa_de_acerto_base = acerto_base / len(teste_marcacoes) * 100.0
print("Taxa de acerto base: %f " %taxa_de_acerto_base)
print('Total de elementos:', len(teste_dados))

#if(resultadoMultinomial > resultadoAdaBoost)
#    vencedor = modeloMultinomial
#else
#    vencedor = modeloAdaBoost