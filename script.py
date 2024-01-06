import os
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed

# Список URL-ов для получения прокси
proxy_urls = [
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
    "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
    "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt",
    "https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
    "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/fahimscirex/proxybd/master/proxylist/http.txt",
    "https://raw.githubusercontent.com/casals-ar/proxy-list/main/http"
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
    "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks4.txt",
    "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks4.txt",
    "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt",
    "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/socks4_proxies.txt",
    "https://raw.githubusercontent.com/prxchk/proxy-list/main/socks4.txt",
    "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks4.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks4/socks4.txt",
    "https://raw.githubusercontent.com/casals-ar/proxy-list/main/socks4"
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
    "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks5.txt",
    "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks5.txt",
    "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/socks5_proxies.txt",
    "https://raw.githubusercontent.com/prxchk/proxy-list/main/socks5.txt",
    "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks5.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks5/socks5.txt",
    "https://raw.githubusercontent.com/fahimscirex/proxybd/master/proxylist/socks5.txt",
    "https://raw.githubusercontent.com/casals-ar/proxy-list/main/socks5"
]

# Указываем абсолютный путь к файлу proxies.txt
file_path = "proxies.txt"

# Удаляем существующий файл proxies.txt, если он существует
try:
    os.remove(file_path)
except FileNotFoundError:
    pass

# Счетчик для подсчета общего количества прокси
total_proxies = 0

# Проходим по каждому URL-у и сохраняем прокси в файл
for url in proxy_urls:
    try:
        response = requests.get(url)
        response.raise_for_status()

        proxies = response.text.strip().split("\n")
        total_proxies += len(proxies)

        with open(file_path, "a") as file:
            file.write("\n".join(proxies) + "\n")

    except requests.exceptions.RequestException as e:
        print(f"[!] Error scraping {url}: {e}")

# Отправляем вебхук Discord
webhook_url = "https://discord.com/api/webhooks/1192883303804575865/vL2v4_548NOj-Q0FhMjcA45gzCPqRhG4IerrHSS08c85UhmHkYZUxzVPHanhBLFwaaqO"
webhook = DiscordWebhook(url=webhook_url)

# Создаем Embed для сообщения
embed = DiscordEmbed(title="Github | Proxy scraped!", color=0x3498db)
embed.set_author(name="Mozaika")
embed.add_embed_field(name="Count", value=total_proxies)
embed.set_footer(text=f"Author: <@1180178134197354570>")

# Добавляем Embed в вебхук
webhook.add_embed(embed)

# Отправляем файл proxies.txt вместе с вебхуком
with open(file_path, "rb") as file:
    webhook.add_file(file.read(), filename="proxies.txt")

# Отправляем вебхук
webhook.execute()
