from tests import ip_test, speed_test, cookie_test, browser_test
from colorama import Fore, Style
import json, os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_termux_screen():
    os.system('clear')

def privacy_test():
    term_size = os.get_terminal_size()
    
    if 'TERMUX' in os.environ:
        clear_termux_screen()
    else:
        clear_screen()

    address = normal_test()

    print(u'\u2500' * term_size.columns)

    vpn_test(address)

    print(u'\u2500' * term_size.columns)

    tor_test(address)

def normal_test():
    print(Fore.GREEN + "Normal Test:" + Style.RESET_ALL)
    print("Testing the unique fingerprint of the normal browser:")
    browser_test.browser_test()
    myip_normal = json.loads(ip_test.query("https://api.ipify.org?format=json"))
    print(myip_normal['ip'])
    ip_test.ip_details(myip_normal['ip'])
    print(ip_test.known_ip(myip_normal['ip']))
    print()
    print("Normal Connection:")
    speed_test.speed_test(10)
    print()
    print("Number of Cookies in Normal Connection:")
    address = cookie_test.cookie_test('normal')
    return address

def vpn_test(address):
    print(Fore.YELLOW + "VPN Test:" + Style.RESET_ALL)
    print("Testing the unique fingerprint of the VPN browser:")
    browser_test.browser_test()
    myip_vpn = json.loads(ip_test.query("https://api.ipify.org?format=json", vpn=True))
    print(myip_vpn['ip'])
    ip_test.ip_details(myip_vpn['ip'])
    print(ip_test.known_ip(myip_vpn['ip']))
    print()
    print("VPN Connection:")
    speed_test.speed_test(10, vpn=True)
    print()
    print("Number of Cookies in VPN Connection:")
    cookie_test.cookie_test('vpn', address)

def tor_test(address):
    print(Fore.RED + "TOR Test:" + Style.RESET_ALL)
    print("Testing the unique fingerprint of the TOR browswer:")
    browser_test.browser_test(tor=True)
    myip_tor = json.loads(ip_test.query("https://api.ipify.org?format=json", tor=True))
    print(myip_tor['ip'])
    ip_test.ip_details(myip_tor['ip'])
    print(ip_test.known_ip(myip_tor['ip']))
    print()
    print("Tor Connection:")
    speed_test.speed_test(10, tor=True)
    print()
    print("Number of Cookies in TOR Connection:")
    cookie_test.cookie_test('tor', address)

if __name__ == "__main__":
    privacy_test()
    input("Press Enter to exit...")