
import sys
import os

# Add the `src` folder to the system path dynamically
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from di_container import DIContainer

def chooseOption():
    print("-----------------------------------")    
    print("1 - Do you want to study a new topic?")
    print("2 - Do you want to review your studies?")
    try:
        numero = int(input("Choose an option:"))        
        return numero
    except ValueError:
        print("Invalid option chosen.")

def main():
    container = DIContainer()

    print("Let's start our lenguage study :)")
    optionChosen = chooseOption()
    print(f"Option {optionChosen} chosen.")
    
    try:
        worker = container.get_worker(optionChosen)
        worker.execute()
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()