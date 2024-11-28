import matplotlib.pyplot as plt
import requests

REPO = "Abelaredo/Proyecto__SSG"
API_URL = f"https://api.github.com/repos/{REPO}/contributors"

response = requests.get(API_URL)
data = response.json()

data = [user for user in data if user['login'] != 'actions-user']

contributors = [user['login'] for user in data]
contributions = [user['contributions'] for user in data]

# Obtener el rango de contribuciones
min_contrib = min(contributions)
max_contrib = max(contributions)

# Crear una lista con todos los números del rango
all_ticks = list(range(min_contrib, max_contrib + 1))

plt.barh(contributors, contributions, color='skyblue')
plt.xlabel('Contributions')
plt.ylabel('Users')
plt.title('GitHub Contributions')

# Establecer los ticks en todos los números
plt.xticks(all_ticks)

# Configurar para que solo se muestren las etiquetas de los múltiplos de 5
plt.gca().xaxis.set_major_locator(plt.MultipleLocator(5))

plt.savefig('contributions.png')
