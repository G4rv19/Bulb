def main():
    state = on_off()
    bulb(state)

def on_off():
    while True:
        user_input = input("Enter 'on' or 'off': ").lower()  # Convert input to lowercase
        if user_input in ['on', 'off']:
            return user_input
        else:
            print("Invalid input. Please enter 'on' or 'off'.")

def bulb(state):
    if state == 'on':
        print("*O*")
    else:
        print("O")

if __name__ == "__main__":
    main()
