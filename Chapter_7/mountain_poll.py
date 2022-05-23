responses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like climb someday? ")

    #Store the response in a dictionary
    responses[name] = response

    #Find out if anyone else is going to take the poll
    repeat = input("Would you like let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

#Polling is complete 
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")