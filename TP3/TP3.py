import pandas as pd
import re
import matplotlib.pyplot as plt

LOG_PATTERN = re.compile(r'(?P<ip>\S+) - - \[(?P<datetime>.*?)\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d+) "(?P<user_agent>.*?)"')
LOG_FILE = 'access.log'

print(f"--- Démarrage de l'analyse de {LOG_FILE} ---")

data = []
try:
    with open(LOG_FILE, 'r') as f:
        for line in f:
            match = LOG_PATTERN.match(line)
            if match:
                data.append(match.groupdict())
except FileNotFoundError:
    print(f"ERREUR: Le fichier '{LOG_FILE}' est introuvable.")
    exit()

if not data:
    print("Aucune donnée valide trouvée.")
    exit()

df = pd.DataFrame(data)
df['status'] = pd.to_numeric(df['status'])

df_404 = df[df['status'] == 404].copy()

if df_404.empty:
    print("Aucune erreur 404 trouvée.")
    exit()

top_ips = df_404['ip'].value_counts().head(5)

bots_404 = df_404[df_404['user_agent'].str.contains(r'bot|crawler|spider', case=False, regex=True)]
bot_ips_unique = bots_404['ip'].unique()
percent_bots = (len(bots_404) / len(df_404) * 100)

print("Génération du graphique...")

plt.figure(figsize=(10, 6))
bars = top_ips.plot(kind='bar', color='#FF5733', alpha=0.8, edgecolor='black')

plt.title('Top 5 des IPs responsables d\'erreurs 404', fontsize=14, fontweight='bold')
plt.xlabel('Adresse IP Source', fontsize=12)
plt.ylabel('Nombre d\'erreurs 404', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)

for i, v in enumerate(top_ips):
    plt.text(i, v + 0.1, str(v), ha='center', fontweight='bold')

plt.tight_layout()

print("\n" + "="*60)
print(f" RAPPORT D'ANALYSE APACHE - ERREURS 404 ".center(60, "="))
print("="*60 + "\n")

print(f"Total d'erreurs 404 analysées : {len(df_404)}")

print("\n" + "-"*30)
print(f" TOP 5 IPs FAUTIVES ".center(30, "-"))
print("-"*30)
for ip, count in top_ips.items():
    marker = "[BOT]" if ip in bot_ips_unique else ""
    print(f" >> IP: {ip:<18} | Erreurs: {count:>3} {marker}")

print("\n" + "-"*30)
print(f" ANALYSE DES BOTS ".center(30, "-"))
print("-"*30)
print(f"Pourcentage d'erreurs 404 dues à des bots : {percent_bots:.2f}%")
if len(bot_ips_unique) > 0:
    print(f"IPs de bots identifiées : {', '.join(bot_ips_unique)}")
else:
    print("Aucun bot évident détecté.")

print("\n" + "="*60 + "\n")
print("Ouverture du graphique...")

plt.show()