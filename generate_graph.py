import matplotlib.pyplot as plt
import requests

REPO = "Abelaredo/Proyecto__SSG"
API_URL = f"https://api.github.com/repos/{REPO}/contributors"

response = requests.get(API_URL)
data = response.json()

data = [user for user in data if user['login'] != 'actions-user']

contributors = [user['login'] for user in data]
contributions = [user['contributions'] for user in data]

# Filter contributions to show only multiples of 5
contributions_filtered = [contrib for contrib in contributions if contrib % 5 == 0]

# Filter contributors based on filtered contributions
filtered_contributors = [contributor for contributor, contrib in zip(contributors, contributions_filtered) 
                         if contrib == contrib]  # Keep only contributors with displayed contributions

# Create the plot with filtered data
plt.barh(filtered_contributors, contributions_filtered, color='skyblue')

# Set x-axis ticks and labels to only show multiples of 5
plt.xticks(range(0, max(contributions_filtered) + 1, 5))  # Generate ticks from 0 to max with 5 interval
plt.xlabel('Contributions')
plt.ylabel('Users')
plt.title('GitHub Contributions (Multiples of 5)')
plt.savefig('contributions.png')
