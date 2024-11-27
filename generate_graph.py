import matplotlib.pyplot as plt
import requests

REPO = "Abelaredo/Proyecto__SSG"
API_URL = f"https://api.github.com/repos/{REPO}/contributors"

response = requests.get(API_URL)
data = response.json()

data = [user for user in data if user['login'] != 'actions-user']

contributors = [user['login'] for user in data]
contributions = [user['contributions'] for user in data]

plt.barh(contributors, contributions, color='skyblue')
plt.xlabel('Contributions')
plt.ylabel('Users')
plt.title('GitHub Contributions')
plt.savefig('contributions.png')
