# https://www.quora.com/How-do-I-save-a-Python-request-session
import requests, pickle, time, random, re
  

def cookie_test(session_type, address=False):

    try: 
        with open('pickle jars/' + session_type +'.pkl', 'rb') as f: 
            session = pickle.load(f) 
    except IOError: 
        session = requests.session() 

    print("The amount of cookies in " + session_type + " session is: " + str(len(session.cookies.get_dict())))

    with open('tests/resources/top500Domains.csv', newline='') as csvfile:
        lines = csvfile.readlines()
        if not address:
            address = random.choice(lines).strip()
            address = address.split(',')[1].replace('"', '')
        try:
            session.get('https://'+address) 
        except:
            print("Connection has been refused.")
            time.sleep(5)

    with open('pickle jars/' + session_type+'.pkl', 'wb') as f: 
        pickle.dump(session, f) 
    print("After connecting to " + address + " the amount of cookies in the " + session_type + " session is: " + str(len(session.cookies.get_dict())))
    return address