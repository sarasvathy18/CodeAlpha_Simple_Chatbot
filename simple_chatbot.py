print("WELCOME TO CHATBOT SASH!!!!")
print("I AM HERE TO INTERACT WITH YOU (SEND BYE TO EXIT)")
while True:   #to interact continuously-loop used
    user_input=input("User : ").lower() #converting to lowercase
    if user_input == "hello":
        print("Bot SASH : hi!")
    elif user_input == "how are you":
        print("Bot SASH : I'm fine,thanks!")
    elif user_input == "bye":
        print("Bot SASH : Goodbye!")
        break  #it stop looping
    else:
        print("bot SASH : I cant understand, try agin!")
