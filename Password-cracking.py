import time

print("<==Welcome to the password cracking program==>")
password = input("Enter your 3-digit password: ")
if password == "" or len(password) != 3 or not password.isdigit():
    print("Password is invalid!\nPlease enter a 3-digit password.")
    exit()
counter = 0
start = time.time()
for i in range(0, 1000):
    counter += 1
    attempt = f"{i:03d}"
    print(f"Checking: {attempt}")
    if attempt == password:
        print("\n🔐Password Cracked!")
        print(f"Password: {password}")
        print(f"Attempts: {counter}")
        break
end = time.time()
time_taken = end - start
print(f"Time taken: {time_taken:.4f} seconds")