from sklearn.naive_bayes import MultinomialNB
from dados import carregar_acessos
x, y = carregar_acessos()
treina_dados = x[:90]
treina_marcacoes = y[:90]
teste_dados = x[-9:]
teste_marcacoes = y[-9:]
modelo = MultinomialNB()
modelo.fit(treina_dados,treina_marcacoes)
resultado = modelo.predict(teste_dados)
diferencas = resultado - teste_marcacoes
acertos = [a for a in diferencas if a == 0 ]
total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)
taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos
print(taxa_de_acerto)
print(total_de_elementos)