# 🔐 Python Password Cracking Simulator

A beginner Python project that simulates a brute-force attack against
a locally provided 3-digit password.

## Features

- Generates combinations from 000 to 999
- Checks each combination
- Counts the number of attempts
- Validates user input
- Stops when the password is found

## Concepts Practiced

- Variables
- Input
- If statements
- For loops
- Range
- F-strings
- String formatting
- Counters
- Break
- Input validation

## How It Works

The program generates every possible 3-digit combination from `000`
to `999` and compares each attempt with the password provided by
the user.

This is a local educational simulation and does not interact with
real accounts or systems.

## Example

```text
Enter your 3-digit password: 472

Checking: 000
Checking: 001
...
Checking: 472

🔐 Password Cracked!
Password: 472
Attempts: 473