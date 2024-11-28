import matplotlib.pyplot as plt
import requests

# Configuración
REPO = "Abelaredo/Proyecto__SSG"
API_URL = f"https://api.github.com/repos/{REPO}/contributors"

# Solicitar datos de la API
try:
    response = requests.get(API_URL)
    response.raise_for_status()  # Lanza un error si la respuesta no es exitosa
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error al obtener datos de la API: {e}")
    exit(1)

# Filtrar contribuyentes válidos
data = [user for user in data if user.get('login') and user['login'] != 'actions-user']

# Manejo de caso: No hay contribuyentes
if not data:
    print("No hay contribuyentes para mostrar.")
    exit(0)

# Preparar datos para la gráfica
contributors = [user['login'] for user in data]
contributions = [user['contributions'] for user in data]

# Crear gráfica
plt.barh(contributors, contributions, color='skyblue')
plt.xlabel('Contributions')
plt.ylabel('Users')
plt.title('GitHub Contributions')

# Guardar gráfica
plt.tight_layout()
plt.savefig('contributions.png')
