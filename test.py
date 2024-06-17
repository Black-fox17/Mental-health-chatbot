from assistants import BasicAssistant

assistant = BasicAssistant("advance.json")

assistant.fit_model(epochs=400)
assistant.save_model()

done = False

while not done:
    message = input("Enter a message: ")
    if message == "STOP":
        done = True
    else:
        print(assistant.process_input(message))