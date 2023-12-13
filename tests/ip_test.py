# https://www.youtube.com/watch?v=r3JPjtb0Asc
import json, io, pycurl, platform, time, os, requests
from ipaddress import ip_network, ip_address

def known_ip(ip):
    ip_add = ip_address(ip)
    with open('tests/resources/torbulkexitlist.txt', 'r') as file:
        for line in file:
            ip_exit = line.strip()
            if ip == ip_exit:
                return "This is a known TOR exit IP."
    with open('tests/resources/vpnbulklist.txt', 'r') as file:
        for line in file:
            ip_block = line.strip()
            if ip_add in ip_network(ip_block):
                return "This is a known VPN IP."
    return "This IP is not known to be associated with a TOR or VPN IP."

def ip_details(ip):
    response = requests.get(f"https://ipinfo.io/{ip}/json")
    if response.status_code == 200:
        data = response.json()
        city = data.get("city")
        coordinates = data.get("loc")
        isp = data.get("org")
        country = data.get("country")
        print(f"City: {city}")
        print(f"Coordinates: {coordinates}")
        print(f"ISP: {isp}")
        print(f"Country: {country}")

def query(url, tor=False, vpn = False):
    output = io.BytesIO()

    query = pycurl.Curl()
    query.setopt(pycurl.URL, url)

    if tor:
        from stem import Signal
        from stem.control import Controller

        SOCKS_PORT = 9050

        def setup():
            with Controller.from_port(port=9051) as controller:
                controller.authenticate()
                controller.signal(Signal.NEWNYM)

        setup()

        query.setopt(pycurl.PROXY, 'localhost')
        query.setopt(pycurl.PROXYPORT, SOCKS_PORT)
        query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5_HOSTNAME)

    if vpn:
        # https://github.com/sttz/expresso?tab=readme-ov-file
        version = platform.system()
        if version == "Linux" or version == "Darwin":
            command = "expresso connect --random"+" > /dev/null 2>&1"
        os.system(command)
        time.sleep(10)

    query.setopt(pycurl.WRITEFUNCTION, output.write)

    try:
        query.perform()
        return output.getvalue()
    except pycurl.error as exc:
        return "Unable to reach %s (%s)" % (url, exc)
        