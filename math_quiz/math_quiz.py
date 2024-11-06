import random

def randomInteger(min, max):
    """
    Calculates a random integer between a given minimum and maximum (minimum and maximum are included).

    Args:
        min (int): a given minimum.
        max (int): a given maximum.
    
    Returns: 
        int: a random number between a given minimum and maximum (minimum and maximum are included).
    """
    try:
        # Check if both arguments are int values
        if not isinstance(min, int) or not isinstance(max, int):
            raise ValueError("Both min and max must be integers.")
        
        #Check if min is smaller than max 
        if min >= max:
            raise ValueError("min must be less than max.")
        
        return random.randint(min, max)
    
    except ValueError as e:
        print(f"Error: {e}")
        return None  


def randomOperator():
    """
    Picks an arithmetic operator randomly.
    
    Returns:
        char: a randomly chosen arithmetic operator between +, -, * 
    """
    return random.choice(['+', '-', '*'])


def calculator(num1, num2, operator):
    """
    Calculates a solution based on the given numbers and the operator. 
    
    Args:
        num1 (int): First given integer.
        num2 (int): Second given integer.
        operator (char): Operator for calculation.
    
    Returns: 
        prob (str): The calculation that is done.
        sol (int): The calculated solution.

    """
    prob = f"{num1} {operator} {num2}" #convertes the calculation into a string
    if operator == '+': 
        sol = num1 + num2  #if operator is '+' the sum of the two numbers is gererated
    elif operator == '-': 
        sol = num1 - num2  #if operator is '-' the difference of the two numbers is gererated
    else: 
        sol = num1 * num2  #if operator is '*' the product of the two numbers is gererated
    return prob, sol


def math_quiz():
    score = 0   #score of the user
    rounds = 3  #the number of rounds that are played

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(rounds):
        number1 = randomInteger(-6, -1);  
        number2 = randomInteger(2, 5); 
        operator = randomOperator()

        PROBLEM, ANSWER = calculator(number1, number2, operator)
        print(f"\nQuestion: {PROBLEM}")

        try:
            useranswer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue  # Start next round if user input is invalid

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1  #if the answer of the user is correct the score is increased by 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{rounds}")

if __name__ == "__main__":
    math_quiz()
