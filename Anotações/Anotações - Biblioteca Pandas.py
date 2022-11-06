#Alguns comandos e funções da biblioteca Pandas


#Fazer leitura de linhas dos arquivos em forma de planilha

df.head(n=4) #Ira mostrar as 4 primeiras linhas



#Saber quantas linhas e colunas o arquivo possui

df.shape #(549, 7) irá trazer linhas, colunas



#Para saber qual o formato cada coluna esta

df.info() #Irá trazer o nome da coluna e qual o seu formato




#Para fazer alterações incluindo colunas

df.columns
Index(['id', 'data_aq', 'produto', 'quantidade', 'valor UN', 'Total', 'setor'], dtype='object')

df.columns = ['id', 'data_aq', 'produto', 'quantidade', 'valor_un', 'valor_total', 'setor']




#Verificar se tem dados faltantes no conjunto

df.isnull().sum()




#Verificar quais os valores são únicos no conjunto de dados

df['setor'].unique()
	# array9['Mesa_banho', 'mesa_banho', 'mesa_Banho', 'perfumaria',
			 'informarica', 'Informatica', 'informaticA',
			 'brinquedos', 'brinqueEdos', 'Brinquedos'], dtype=object)
			 
			 


#Agrupar os dados e mostrar em gráfico (utiliza a biblioteca matplotlib)

df['setor'].value_counts().plot(kind='bar')




#Mostrar alguns dados estatisticos (contagem, media, desvio, minimo, percentil)

df.describe()






