
import matplotlib.pyplot as plt
import requests

REPO = "Abelaredo/rProyecto__SSG"
API_URL = f"https://api.github.com/repos/{REPO}/contributors"

response = requests.get(API_URL)
data = response.json()

contributors = [user['login'] for user in data]
contributions = [user['contributions'] for user in data]

plt.barh(contributors, contributions, color='skyblue')
plt.xlabel('Contributions')
plt.ylabel('Users')
plt.title('GitHub Contributions')

# Set ticks on X-axis to show multiples of 5
max_contributions = max(contributions)
plt.xticks(range(0, max_contributions + 1, 5))  # Multiples of 5 up to the max contributions

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


