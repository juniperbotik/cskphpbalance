import os
import requests
from github import Github
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime
import pytz

proxy_urls = [
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt", 
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4",
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
    "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt", 
    "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt", 
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt"
]

# Получаем имя репозитория из переменной окружения GITHUB_REPOSITORY
repo_name = os.environ.get('GITHUB_REPOSITORY', 'cskphpbalance')

# Получаем токен доступа GitHub из переменной окружения
github_token = os.environ.get('GGK_TKK')

# Инициализируем объект Github
g = Github(github_token)

# Получаем репозиторий
repo = g.get_repo(repo_name)
file = repo.get_contents(file_path)
current_content = file.decoded_content.decode('utf-8')

# Счетчик для подсчета общего количества прокси
total_proxies = 0

# Проходим по каждому URL-у и добавляем прокси в список
new_proxies = []
for url in proxy_urls:
    try:
        response = requests.get(url)
        response.raise_for_status()

        proxies = response.text.strip().split("\n")
        total_proxies += len(proxies)
        new_proxies.extend(proxies)

    except requests.exceptions.RequestException as e:
        print(f"[!] Error scraping {url}: {e}")

# Объединяем старые и новые прокси
all_proxies = current_content.strip().split("\n") + new_proxies

# Обновляем содержимое файла в репозитории
repo.update_file(f"proxies.txt", f"Update proxies.txt - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", "\n".join(all_proxies), file.sha)

# Выводим информацию о скрапинге
print("[=] Scraping socks4,socks5 proxies....")
print(f"[=] Scraped! | {total_proxies} proxies")
print(f"[=] Updated proxies.txt in the repository!")

# Получаем текущее время UTC
current_utc_time = datetime.utcnow().replace(tzinfo=pytz.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

# Отправляем вебхук Discord
webhook_url = "https://discord.com/api/webhooks/1192883303804575865/vL2v4_548NOj-Q0FhMjcA45gzCPqRhG4IerrHSS08c85UhmHkYZUxzVPHanhBLFwaaqO"

webhook = DiscordWebhook(url=webhook_url)
embed = DiscordEmbed(title="Github | Proxy scraped!", description=f"{total_proxies} proxies", color=0x3498db)
embed.set_author(name="Mozaika")
embed.add_embed_field(name="Current UTC Time", value=current_utc_time)
webhook.add_embed(embed)
webhook.execute()
