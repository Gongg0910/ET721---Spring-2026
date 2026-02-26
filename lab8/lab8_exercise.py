import pandas as pd
import requests
import matplotlib.pyplot as plt

# url = "https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/en.1.csv"          which result epl_matches.csv same thing as "https://raw.githubusercontent.com" 

# or 

url = "https://raw.githubusercontent.com"   
file_name = "epl_matches.csv"

print("\nDownloading external data...")
response = requests.get(url)
if response.status_code == 200:
    with open(file_name, "wb") as f:
        f.write(response.content)
    print("Download complete.")
else:
    print(f"Download failed")


games = pd.read_csv(file_name)
print("\nGames data from CSV file:")
print(games.head())


arsenal_vs_chelsea = games[((games['Team 1'] == 'Arsenal') & (games['Team 2'] == 'Chelsea')) | ((games['Team 1'] == 'Chelsea') & (games['Team 2'] == 'Arsenal'))].copy()


arsenal_home_vs_chelsea = arsenal_vs_chelsea[arsenal_vs_chelsea['Team 1'] == 'Arsenal'].copy()
arsenal_away_vs_chelsea = arsenal_vs_chelsea[arsenal_vs_chelsea['Team 2'] == 'Arsenal'].copy()


arsenal_home_vs_chelsea['Goals'] = arsenal_home_vs_chelsea['FT'].str.split('-').str[0].astype(int)
arsenal_away_vs_chelsea['Goals'] = arsenal_away_vs_chelsea['FT'].str.split('-').str[1].astype(int)

home_avg_goals = arsenal_home_vs_chelsea['Goals'].mean()
away_avg_goals = arsenal_away_vs_chelsea['Goals'].mean()

print(f"Arsenal home average goals: {home_avg_goals}")
print(f"Arsenal away average goals: {away_avg_goals}")


metrics = ['Average Goals']
home_values = [home_avg_goals]
away_values = [away_avg_goals]

x = range(len(metrics))
bar_width = 0.35

plt.figure(figsize=(8, 5))
plt.bar([i - bar_width/2 for i in x], home_values, width=bar_width, label='Home', color='skyblue')
plt.bar([i + bar_width/2 for i in x], away_values, width=bar_width, label='Away', color='orange')

plt.xticks(x, metrics)
plt.title('Arsenal vs. Chelsea — Home vs Away Comparison')
plt.ylabel('Average Goals')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show(block=True)

input("Press Enter to close...")
