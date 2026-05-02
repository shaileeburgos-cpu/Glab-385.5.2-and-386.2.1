📘 GLAB 385.5.2 — Event Management System
A simple Python-based console application that allows users to add, list, and delete events using an in‑memory dictionary. This lab demonstrates user input handling, date parsing, sorting, and basic CRUD operations.

🧠 Learning Objectives
Organize logic with functions

Store data using dictionaries

Parse and validate dates with datetime.strptime()

Sort events by date using a custom key function

Build a menu-driven console application

Handle invalid input gracefully

📂 Project Structure
text
GLAB 385.5.2/
│── event_management_system.py
│── README.md
▶️ How to Run the Program
1. Activate your virtual environment
bash
source /Users/shaileeburgos/may1st/.venv/bin/activate
2. Navigate to the GLAB folder
bash
cd /Users/shaileeburgos/may1st/GLAB\ 385.5.2
3. Run the script
bash
python3 event_management_system.py
You should see:

text
📝 Event Management System 📝
1. Add Event
2. List Events
3. Delete Event
4. Quit
🛠 Features
Add Event

Prompts for event name

Prompts for date in YYYY-MM-DD

Validates date format

Stores event in a dictionary

List Events

Shows all upcoming events

Sorted by date

Displays days remaining until each event

Delete Event

Deletes an event by name

Handles missing events gracefully

Quit

Exits the program cleanly

🧪 Example Output
text
📝 Event Management System 📝
1. Add Event
2. List Events
3. Delete Event
4. Quit
Enter your choice: 1
Enter the event name: Graduation
Enter the event date (YYYY-MM-DD): 2026-06-15
🎉 Success! Added "Graduation" to events!
📝 Reflection
In this lab, I built a menu-driven Python application that uses functions, dictionaries, and date handling to manage events. I practiced validating user input, converting strings into datetime objects, and sorting events by date using a custom key function. I also added error handling to prevent crashes when users enter invalid dates or event names that don’t exist. This reinforced my understanding of control flow, data structures, and modular program design in Python.