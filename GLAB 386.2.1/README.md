📘 GLAB 386.2.1 — NumPy Random Module Examples
This lab demonstrates how to use the NumPy random module to generate random numbers, arrays, selections, and distributions. The script includes multiple examples that help build familiarity with NumPy’s randomization functions and how they behave.

🧠 Learning Objectives
Understand how to import and use the NumPy library

Generate random integers and floats

Create random arrays with specific shapes

Use choice() to select random items from a list

Shuffle arrays in place

Generate values from a normal distribution

Practice printing and formatting output

📂 Project Structure
Code
GLAB 386.2.1/
│── random_examples.py
│── outputs/        (optional folder for screenshots or results)
│── assets/         (optional folder for notes or images)
│── README.md
▶️ How to Run the Program
1. Activate your virtual environment
bash
source /Users/shaileeburgos/may1st/.venv/bin/activate
2. Navigate to the GLAB folder
bash
cd /Users/shaileeburgos/may1st/GLAB\ 386.2.1
3. Run the script
bash
python3 random_examples.py
You should see output similar to:

Code
Random integer between 1 and 100:
67

Random float between 0 and 1:
0.4839201

Random array of integers:
[12 88 34 55 90]

Random dish selected:
Pizza

Shuffled list:
['pasta', 'tacos', 'sushi', 'pizza']
(Your numbers will differ — that’s the point!)

🛠 Features Demonstrated
✔ Random Integers
Using np.random.randint() to generate integers within a range.

✔ Random Floats
Using np.random.rand() to generate floating‑point values between 0 and 1.

✔ Random Arrays
Creating arrays of random values with a specified size.

✔ Random Choice
Selecting a random item from a list (e.g., a random dish).

✔ Shuffling
Using np.random.shuffle() to reorder a list in place.

✔ Normal Distribution
Generating values from a Gaussian distribution using np.random.normal().

🧪 Example Output (Formatted)
Code
🎲 Random Integer (1–100): 42
🌊 Random Float (0–1): 0.2948
📊 Random Array: [12 55 88 23 90]
🍽 Random Dish: Sushi
🔀 Shuffled List: ['tacos', 'pizza', 'sushi', 'pasta']
📈 Normal Distribution Sample: [-0.12  0.88  1.44 -0.55]
📝 Reflection
In this lab, I practiced using the NumPy random module to generate different types of random values. I learned how to create random integers, floats, arrays, and selections, as well as how to shuffle lists and generate values from a normal distribution. This helped reinforce my understanding of NumPy’s core randomization functions and how they can be used in data analysis, simulations, and testing.