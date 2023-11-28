from speedtests import connection_tor_test


print("Normal Connection:")
connection_tor_test.speed_test(10, tor=False)
print("Tor Connection:")
connection_tor_test.speed_test(10, tor=True)
