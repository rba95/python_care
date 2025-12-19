import matplotlib.pyplot as plt
import re

pattern_ip = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
ip_attempts = {}
failed_logins = 0

try:
    with open('auth.log', 'r') as f:
        lines = f.readlines()

    for line in lines:
        if 'Failed password' in line:
            failed_logins += 1
            match = re.search(pattern_ip, line)
            if match:
                ip = match.group()
                ip_attempts[ip] = ip_attempts.get(ip, 0) + 1

    print(f"Total d'ip échoué {failed_logins}")

    sorted_ips = sorted(ip_attempts.items(), key=lambda x: x[1], reverse=True)[:10]

    if sorted_ips:
        ips, attempts = zip(*sorted_ips)
        plt.bar(ips, attempts)
        plt.xlabel('IP Address')
        plt.ylabel('Number of Failed Attempts')
        plt.title('Top 10 Failed Login Attempts by IP')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("Aucune donnée trouvée.")

except FileNotFoundError:
    print("Fichier introuvable.")