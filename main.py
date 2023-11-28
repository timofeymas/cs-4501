from speedtests import connection_tor_test, ip_test
import json



myip_normal = json.loads(ip_test.query("https://api.ipify.org?format=json", tor=False))
print("Normal IP:")
print(myip_normal['ip'])
myip_tor = json.loads(ip_test.query("https://api.ipify.org?format=json", tor=True))
print("Tor IP:")
print(myip_tor['ip'])

print("Normal Connection:")
connection_tor_test.speed_test(10, tor=False)

print("Tor Connection:")
connection_tor_test.speed_test(10, tor=True)