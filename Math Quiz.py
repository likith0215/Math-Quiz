import random
import time

def generate_2_variable_equation():
    x = random.randint(1, 10)
    y = random.randint(1, 10)

    a1, b1 = random.randint(1, 5), random.randint(1, 5)
    a2, b2 = random.randint(1, 5), random.randint(1, 5)

    c1 = a1 * x + b1 * y
    c2 = a2 * x + b2 * y

    return (a1, b1, c1, a2, b2, c2, x, y)

def generate_3_variable_equation():
    x = random.randint(1, 5)
    y = random.randint(1, 5)
    z = random.randint(1, 5)

    a1, b1, c1 = random.randint(1, 3), random.randint(1, 3), random.randint(1, 3)
    a2, b2, c2 = random.randint(1, 3), random.randint(1, 3), random.randint(1, 3)
    a3, b3, c3 = random.randint(1, 3), random.randint(1, 3), random.randint(1, 3)

    d1 = a1 * x + b1 * y + c1 * z
    d2 = a2 * x + b2 * y + c2 * z
    d3 = a3 * x + b3 * y + c3 * z

    return (a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3, x, y, z)

print("🎉 Welcome to the Math Quiz Game!")
username = input("Enter your name: ")
print(f"Hello {username}, let's begin!\n")

print("Choose difficulty level: Easy / Medium / Hard")
difficulty = input("Enter difficulty: ").strip().lower()

# Set question settings
if difficulty == "easy":
    total_questions = 5
    time_limit = 20
elif difficulty == "medium":
    total_questions = 5
    time_limit = 40
elif difficulty == "hard":
    total_questions = 3
    time_limit = 50
else:
    print("Invalid input. Defaulting to Medium.")
    difficulty = "medium"
    total_questions = 5
    time_limit = 40

score = 0

for i in range(1, total_questions + 1):
    print(f"\nQuestion {i} (⏳ {time_limit} sec):")

    start_time = time.time()

    if difficulty == "easy":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(['+', '-'])
        question = f"{num1} {operation} {num2}"
        correct_answer = eval(question)
        print(f"What is {question}?")

        try:
            user_input = input("Your answer: ")
            elapsed = time.time() - start_time
            if elapsed > time_limit:
                print("⏰ Time's up!")
                break
            user_answer = int(user_input)
            if user_answer == correct_answer:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer is {correct_answer}")
        except ValueError:
            print("⚠️ Please enter a valid number!")

    elif difficulty == "medium":
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.randint(1, 10)
        op1 = random.choice(['+', '-', '*'])
        op2 = random.choice(['+', '-', '*'])
        question = f"({a} {op1} {b}) {op2} {c}"
        correct_answer = eval(question)
        print(f"What is {question}?")

        try:
            user_input = input("Your answer: ")
            elapsed = time.time() - start_time
            if elapsed > time_limit:
                print("⏰ Time's up!")
                break
            user_answer = int(user_input)
            if user_answer == correct_answer:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer is {correct_answer}")
        except ValueError:
            print("⚠️ Please enter a valid number!")

    elif difficulty == "hard":
        if random.choice([True, False]):
            # 2-variable system
            a1, b1, c1, a2, b2, c2, correct_x, correct_y = generate_2_variable_equation()
            print("Solve for x and y:")
            print(f"{a1}x + {b1}y = {c1}")
            print(f"{a2}x + {b2}y = {c2}")

            try:
                user_x = float(input("x = "))
                user_y = float(input("y = "))
                elapsed = time.time() - start_time
                if elapsed > time_limit:
                    print("⏰ Time's up!")
                    break
                if abs(user_x - correct_x) < 0.01 and abs(user_y - correct_y) < 0.01:
                    print("✅ Correct!")
                    score += 1
                else:
                    print(f"❌ Wrong! Correct: x = {correct_x}, y = {correct_y}")
            except ValueError:
                print("⚠️ Please enter valid numbers!")

        else:
            # 3-variable system
            a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3, correct_x, correct_y, correct_z = generate_3_variable_equation()
            print("Solve for x, y, and z:")
            print(f"{a1}x + {b1}y + {c1}z = {d1}")
            print(f"{a2}x + {b2}y + {c2}z = {d2}")
            print(f"{a3}x + {b3}y + {c3}z = {d3}")

            try:
                user_x = float(input("x = "))
                user_y = float(input("y = "))
                user_z = float(input("z = "))
                elapsed = time.time() - start_time
                if elapsed > time_limit:
                    print("⏰ Time's up!")
                    break
                if (
                    abs(user_x - correct_x) < 0.01 and
                    abs(user_y - correct_y) < 0.01 and
                    abs(user_z - correct_z) < 0.01
                ):
                    print("✅ Correct!")
                    score += 1
                else:
                    print(f"❌ Wrong! Correct: x = {correct_x}, y = {correct_y}, z = {correct_z}")
            except ValueError:
                print("⚠️ Please enter valid numbers!")

print("\n🎯 Quiz Over!")
print(f"{username}, you scored {score}/{total_questions}")
