# Simple AI Assistant
import random
import datetime

def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

def get_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs! ",
        "Why was the computer cold? It left its Windows open! ",
        "Why don't programmers trust atoms? Because they make up everything!"
    ]
    return random.choice(jokes)

def calculate(expression):
    try:
        return eval(expression)
    except:
        return "Sorry, I can't calculate that."

def main():
    print(f"\n🤖 {greet()}! I am your Personal AI Assistant.")
    print("Type 'help' to see what I can do.\n")
    
    while True:
        command = input("You: ").lower().strip()
        
        if command in ["hi", "hello", "hey"]:
            print(f"Assistant: {greet()}! How can I help you today?")
            
        elif "joke" in command:
            print(f"Assistant: {get_joke()}")
            
        elif "time" in command:
            print(f"Assistant: The current time is {datetime.datetime.now().strftime('%I:%M %p')}")
            
        elif "date" in command:
            print(f"Assistant: Today's date is {datetime.date.today()}")
            
        elif command.startswith("calculate"):
            expr = command.replace("calculate", "").strip()
            result = calculate(expr)
            print(f"Assistant: {expr} = {result}")
            
        elif "weather" in command:
            print("Assistant: It's 28°C and sunny in Jeddah today! ☀️")
            
        elif command in ["help", "what can you do"]:
            print("""Assistant: I can do these things:
- Say hello
- Tell jokes
- Tell current time and date
- Do calculations (example: calculate 25 * 4)
- Give weather (simulated)
- Type 'exit' to close""")
            
        elif command in ["exit", "bye", "quit"]:
            print("Assistant: Goodbye! Have a great day! 👋")
            break
            
        else:
            print("Assistant: I'm still learning! Try saying 'help' to see what I can do.")

if __name__ == "__main__":
    main()
