import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def Aiintegration():

    print("Program started...")

    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )

    question1 = input("Enter income: ")
    question2 = input("Enter EMI: ")
    question3 = input("Enter living cost: ")
    question4 = input("Enter goal: ")

    question = f"""
Income: {question1}
EMI: {question2}
Living Cost: {question3}
Goal: {question4}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful financial assistant"},
                {"role": "user", "content": question}
            ]
        )

        print("\nAI Answer:\n")
        print(response.choices[0].message.content)

    except Exception as e:
        print("ERROR:", e)
