import pandas as pd

# Criando uma função para contar os caracteres no campo "Director"
def contar_caracteres(diretor):
    return len(diretor)

# Lendo o arquivo CSV e carregando os dados em um DataFrame
df_filmes = pd.read_csv('netflix_titles.csv')

# Ordenando os dados pela coluna "data_added"
df_ordenado_por_data = df_filmes.sort_values(by='data_added')

# Ordenando os dados pela coluna "released_year"
df_ordenado_por_ano = df_filmes.sort_values(by='released_year')

# Contando a quantidade de filmes por ano
contagem_por_ano = df_filmes['release_year'].value_counts()
print(contagem_por_ano)

# Obtendo os anos únicos dos filmes
anos_unicos = df_filmes['release_year'].unique()
print(anos_unicos)

# Verificando as primeiras linhas do DataFrame para garantir que os dados foram carregados corretamente
print(df_filmes.head())

# Gerando uma lista com os países dos filmes
lista_paises = df_filmes['country'].value_counts()

# Exibindo a lista de países
print(lista_paises)

# Contagem de ocorrências para a coluna 'country'
contagem_paises = df_filmes['country'].value_counts()

# Contagem de ocorrências para a coluna 'rating'
contagem_classificacao = df_filmes['rating'].value_counts()

# Exibindo as contagens de ocorrências
print("Contagem de países:")
print(contagem_paises)

print("\nContagem de classificação de idade:")
print(contagem_classificacao)

# Criando novas colunas com o quarto e décimo caractere do campo "Director"
df_filmes['quarto_caractere'] = df_filmes['Director'].apply(lambda x: x[3] if len(x) > 3 else None)
df_filmes['decimo_caractere'] = df_filmes['Director'].apply(lambda x: x[9] if len(x) > 9 else None)

# Exibindo as primeiras linhas do DataFrame para verificar as novas colunas
print(df_filmes.head())

# Aplicando a função a cada linha do DataFrame
df_filmes['tamanho_do_nome_do_diretor'] = df_filmes['Director'].apply(contar_caracteres)

# Exibindo as primeiras linhas do DataFrame para verificar a nova coluna
print(df_filmes.head())

# Exibindo as primeiras linhas dos DataFrames ordenados
print("Ordenado por data_added:")
print(df_ordenado_por_data.head())

print("\nOrdenado por released_year:")
print(df_ordenado_por_ano.head())

