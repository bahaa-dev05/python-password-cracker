🔐 Python Password Cracking Simulator

A beginner Python project that simulates a brute-force attack against a locally provided 3-digit password.

🚀 Features

* 🔢 Tests every possible 3-digit combination from 000 to 999
* 🔍 Checks each password attempt
* 🔢 Counts the number of attempts
* ⏱️ Measures how long the cracking simulation takes
* 🛡️ Validates that the user enters exactly 3 digits
* 🛑 Stops automatically when the password is found

🧠 Concepts Practiced

* Variables
* input()
* if statements
* for loops
* range()
* break
* F-strings
* String formatting
* Counters
* Input validation
* Time measurement

⚙️ How It Works

The program generates every possible 3-digit combination from 000 to 999 and compares each attempt with the password provided by the user.

Once the correct password is found, the program displays the password, number of attempts, and the time taken.

💻 Example

Welcome to the password cracking program
Enter your 3-digit password: 472
Checking: 000
Checking: 001
Checking: 002
...
Checking: 472
🔐 Password Cracked!
Password: 472
Attempts: 473
Time: 0.0002 seconds

⚠️ Disclaimer

This is an educational simulation that runs entirely locally. It does not attempt to access or attack real accounts, websites, or computer systems.
