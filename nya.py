import amino
import json
import os

client = amino.Client()
x = 0

try:
    with open("/storage/emulated/0/adro_gantiam/accounts/emails.txt") as json_file:
        emails = json.load(json_file)
except:
    os.system("cd /storage/emulated/0/adro_gantiam/ && mkdir 'accounts'")
    open("/storage/emulated/0/adro_gantiam/accounts/emails.txt", "w").write("[]")
    with open("/storage/emulated/0/adro_gantiam/accounts/emails.txt") as json_file:
        emails = json.load(json_file)

try: password = open("/storage/emulated/0/adro_gantiam/accounts/password.txt", "r").read()
except:
    open("/storage/emulated/0/adro_gantiam/accounts/password.txt", "w").write(input("password for all accounts: "))
    password = open("/storage/emulated/0/adro_gantiam/accounts/password.txt", "r").read() 

print("Your password: " + str(password))

id = amino.lib.util.helpers.generate_device_info()["device_id"]

print(id)

while x < 3:
    print("Всего аккаунтов создано: " + str(len(emails)) + "\n")

    email = input("email: ")

    client.request_verify_code(email)

    client.register("koshak", email, password, input("code: "), id)
    client.login(email, password)
    client.configure(17, "Female")
    client.logout()

    emails.append({"email": email, "password": password})

    with open("/storage/emulated/0/adro_gantiam/accounts/emails.txt", "w") as outfile:
        json.dump(emails, outfile)

    open("/storage/emulated/0/adro_gantiam/accounts/test.txt", "a").write("\n" + str(email) + "\n" + str(password))

    x += 1

os.system("python nya.py")
