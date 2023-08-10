import pandas as pd
import matplotlib.pyplot as plt

# Carregar o conjunto de dados
df = pd.read_csv('sales_data.csv')

# Extrair os dados de meses e vendas
meses = df['Mês']
vendas = df['Vendas']

# Plotar o gráfico de tendências
plt.figure(figsize=(10, 6))
plt.plot(meses, vendas, marker='o', color='b', linestyle='-', linewidth=2)
plt.title('Tendência de Vendas Mensais')
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Mostrar o gráfico
plt.show()
