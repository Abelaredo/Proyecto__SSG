import matplotlib.pyplot as plt
import requests

REPO = "Abelaredo/Proyecto__SSG"
API_URL = f"https://api.github.com/repos/{REPO}/contributors"

response = requests.get(API_URL)
data = response.json()

data = [user for user in data if user['login'] != 'actions-user']

contributors = [user['login'] for user in data]
contributions = [user['contributions'] for user in data]

# Filter ticks to show only multiples of 5
ticks = [x for x in range(min(contributions), max(contributions) + 1) if x % 5 == 0]

plt.barh(contributors, contributions, color='skyblue')
plt.xlabel('Contributions')
plt.ylabel('Users')
plt.title('GitHub Contributions')

# Set x-axis ticks and labels
plt.xticks(ticks)
plt.gca().xaxis.set_major_locator(plt.MultipleLocator(5))  # Set major tick spacing to 5

plt.savefig('contributions.png')
