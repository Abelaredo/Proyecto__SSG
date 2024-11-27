import matplotlib.pyplot as plt
import requests

# API de GitHub para obtener contribuciones
REPO = "Abelaredo/Proyecto__SSG"  # Cambia esto por tu repositorios
API_URL = f"https://api.github.com/repos/{REPO}/contributors"

response = requests.get(API_URL)
data = response.json()

# Procesar datos de las contribuciones
contributors = [user['login'] for user in data]
contributions = [user['contributions'] for user in data]

# Crear gráfico
plt.barh(contributors, contributions, color='skyblue')
plt.xlabel('Contributions')
plt.ylabel('Users')
plt.title('GitHub Contributions')

# Guardar gráfico como imagen
plt.savefig('contributions.png')
