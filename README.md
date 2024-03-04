AirBnB Clone Project
This project aims to develop a simplified version of AirBnB, a popular platform for renting accommodations. The project includes a command-line interpreter that allows users to manage various objects within the AirBnB system, such as users, listings, bookings, and more.

Command Interpreter
The command interpreter provides an interactive shell where users can input commands to interact with the AirBnB system. It also supports non-interactive mode for batch processing of commands.

How to Start the Command Interpreter
To start the command interpreter, follow these steps:

Clone the repository to your local machine:
git clone https://github.com/your_username/airbnb_clone.git

Navigate to the project directory:
cd airbnb_clone

Ensure that console.py has executable permissions:
chmod +x console.py

Run the command interpreter:
./console.py

How to Use the Command Interpreter
Once the command interpreter is started, you'll see the prompt (hbnb). You can input various commands to manage objects in the AirBnB system. Here are some available commands:

help: Display available commands and their usage.
quit: Exit the command interpreter.

Examples
Interactive Mode:

$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) quit
$
Non-Interactive Mode:

$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
