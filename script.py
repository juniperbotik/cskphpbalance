import os
import requests

# Список URL-ов для получения прокси
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

# Получаем абсолютный путь к файлу proxies.txt
file_path = os.path.abspath("proxies.txt")

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

# Выводим информацию о скрапинге
print("[=] Scraping socks4,socks5 proxies....")
print(f"[=] Scraped! | {total_proxies} proxies")
print(f"[=] Saved to {file_path}!")
