import matplotlib.pyplot as plt
import requests

REPO = "Abelaredo/Proyecto__SSG"
API_URL = f"https://api.github.com/repos/{REPO}/contributors"

response = requests.get(API_URL)

# Verificar si la solicitud fue exitosa
if response.status_code != 200:
    print(f"Error: La solicitud falló con el código {response.status_code}")
    print("Detalles:", response.text)
    exit(1)

try:
    data = response.json()
except ValueError:
    print("Error: La respuesta no es JSON válida.")
    print("Detalles:", response.text)
    exit(1)

# Verificar que `data` es una lista
if not isinstance(data, list):
    print("Error: La respuesta JSON no es una lista como se esperaba.")
    print("Detalles:", data)
    exit(1)

# Extraer datos de los contribuyentes
contributors = [user['login'] for user in data]
contributions = [user['contributions'] for user in data]

# Graficar
plt.barh(contributors, contributions, color='skyblue')
plt.xlabel('Contributions')
plt.ylabel('Users')
plt.title('GitHub Contributions')

# Establecer ticks en el eje X
max_contributions = max(contributions)
plt.xticks(range(0, max_contributions + 1, 5))  # Mostrar solo múltiplos de 5

plt.savefig('contributions.png')


'''import matplotlib.pyplot as plt
import requests

REPO = "user/repo"
API_URL = f"https://api.github.com/repos/{REPO}/contributors"

response = requests.get(API_URL)
data = response.json()

contributors = [user['login'] for user in data]
contributions = [user['contributions'] for user in data]

plt.barh(contributors, contributions, color='skyblue')
plt.xlabel('Contributions')
plt.ylabel('Users')
plt.title('GitHub Contributions')

plt.savefig('contributions.png')'''


