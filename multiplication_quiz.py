import pyinputplus as pyip
import time, random
num_questions = 10
correct = 0
for question_number in range(num_questions):
    n = random.randint(0 , 9)
    n1 = random.randint(0 , 9)
    correct_num = n * n1
    try:
        question = pyip.inputInt(prompt = f'What is {n} x {n1}?', timeout=8)
        if question == correct_num:
            correct += 1
            print('Correct!')
            time.sleep(1)
            continue
        else:
            print('incorrect!')
    except pyip.TimeoutException:
        print('Out of time!')
print(f'You got {correct} answers correct!')