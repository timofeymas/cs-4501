import json
import io
import pycurl
def query(url, tor=False):
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


    query.setopt(pycurl.WRITEFUNCTION, output.write)

    try:
        query.perform()
        return output.getvalue()
    except pycurl.error as exc:
        return "Unable to reach %s (%s)" % (url, exc)
        