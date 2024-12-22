print("Welcome to the Pirate Island")
direction = input("Do you want to go 'left' or 'right'? ").lower()
if direction == "right":
    print("Game Over")
elif direction == "left":
    action = input("Do you want to 'dig for treasure' or 'sail the ship'? ").lower()
    if action == "dig for treasure":
        print("Game Over")
    elif action == "sail the ship":
        choice = input("Choose between 'shark', 'pirate ship', or 'mermaid': ").lower()
        if choice == "shark" or choice == "pirate ship":
            print("Game Over")
        elif choice == "mermaid":
            print("You Win")