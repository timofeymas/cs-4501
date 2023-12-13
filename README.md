# cs-4501

## Refereneces:
https://moz.com/top500</br>
https://github.com/X4BNet/lists_vpn/blob/main/output/vpn/ipv4.txt </br>
https://www.youtube.com/watch?v=r3JPjtb0Asc </br>
https://www.quora.com/How-do-I-save-a-Python-request-session </br>
https://stackoverflow.com/questions/15316304/open-tor-browser-with-selenium </br>
https://stackoverflow.com/a/60359703 </br>

Webpage used for ip extraction: </br>
https://api.ipify.org?format=json </br>

Webpage used for browser fingerprinting: </br>
https://coveryourtracks.eff.org/kcarter?aat=1 </br>

Webpage used to downliad files </br>
http://{ipv}.download.thinkbroadband.com:{port}/{size}.zip

## How to run:
### 1. Make sure to install all necessary dependencies in the `requirements.txt` file
### 2. Using the terminal run `server.py`
### 3. Using with system `tor`
`tor` needs to be installed (`apt install tor`) and running on port 9050.</br>
`src/app/tor --controlport 9051 --socksport 9050`
### 4. run `main.py`

## Sample Test Output:
Normal Test:</br>
Testing the unique fingerprint of the normal browser:</br>
You are not protected against tracking on the web.</br>

USER-DATA:</br>
Detected OS: Host: 127.0.0.1:8080</br>
Connection: keep-alive</br>
sec-ch-ua: "Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"</br>
sec-ch-ua-mobile: ?0</br>
sec-ch-ua-platform: "macOS"</br>
Upgrade-Insecure-Requests: 1</br>
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36</br>
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7</br>
Sec-Fetch-Site: none</br>
Sec-Fetch-Mode: navigate</br>
Sec-Fetch-User: ?1</br>
Sec-Fetch-Dest: document</br>
Accept-Encoding: gzip, deflate, br</br>
Accept-Language: en-US,en;q=0.9</br>

IP DETAILS:</br>
XXX.XXX.XXX.XXX</br>
City: Charlottesville</br>
Coordinates: 38.0293,-78.4767</br>
ISP: AS225 University of Virginia</br>
Country: US</br>
This IP is not known to be associated with a TOR or VPN IP.</br>

Normal Connection:</br>
[==============================] 53.78636 Mbps</br>
10MB = 1.95 seconds</br>

Number of Cookies in Normal Connection:</br>
The amount of cookies in normal session is: 26</br>
After connecting to time.com the amount of cookies in the normal session is: 26</br>
─────────────────────────────────────────────────── </br>
VPN Test:</br>
Testing the unique fingerprint of the VPN browser:</br>
You are not protected against tracking on the web.</br>

USER-DATA:</br>
Detected OS: Host: 127.0.0.1:8080</br>
Connection: keep-alive</br>
sec-ch-ua: "Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"</br>
sec-ch-ua-mobile: ?0</br>
sec-ch-ua-platform: "macOS"</br>
Upgrade-Insecure-Requests: 1</br>
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36</br>
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7</br>
Sec-Fetch-Site: none</br>
Sec-Fetch-Mode: navigate</br>
Sec-Fetch-User: ?1</br>
Sec-Fetch-Dest: document</br>
Accept-Encoding: gzip, deflate, br</br>
Accept-Language: en-US,en;q=0.9v

IP DETAILS:</br>
157.97.121.102</br>
City: New York City</br>
Coordinates: 40.7143,-74.0060</br>
ISP: AS396356 Latitude.sh</br>
Country: US</br>
This IP is not known to be associated with a TOR or VPN IP.</br>

VPN Connection:</br>
[==============================] 55.69013 Mbps</br>
10MB = 1.88 seconds</br>

Number of Cookies in VPN Connection:</br>
The amount of cookies in vpn session is: 26</br>
After connecting to time.com the amount of cookies in the vpn session is: 26</br>
─────────────────────────────────────────────────── </br>
TOR Test:</br>
Testing the unique fingerprint of the TOR browswer:</br>
You have strong protection against web tracking.</br>

USER-DATA:</br>
Detected OS: Host: localhost:8080</br>
User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0</br>
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8</br>
Accept-Language: en-US,en;q=0.5</br>
Accept-Encoding: gzip, deflate, br</br>
Connection: keep-alive</br>
Upgrade-Insecure-Requests: 1</br>
Sec-Fetch-Dest: document</br>
Sec-Fetch-Mode: navigate</br>
Sec-Fetch-Site: none</br>
Sec-Fetch-User: ?1</br>

IP DETAILS:</br>
107.189.11.111</br>
City: Bettembourg</br>
Coordinates: 49.5186,6.1028</br>
ISP: AS53667 FranTech Solutions</br>
Country: LU</br>
This is a known TOR exit IP.</br>

Tor Connection:</br>
[==============================] 6.63182 Mbps</br>
10MB = 15.81 seconds</br>

Number of Cookies in TOR Connection:</br>
The amount of cookies in tor session is: 12</br>
After connecting to time.com the amount of cookies in the tor session is: 12</br>
─────────────────────────────────────────────────── </br>
