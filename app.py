import random
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/randomgreeting")
def root(user_name: str = None):
    greetings_incl_names = ["Welcome, FIRSTNAME!", "Great to see you, FIRSTNAME!", "Hi, FIRSTNAME!", "Welcome back, FIRSTNAME!", "Thanks for being here, FIRSTNAME!", "Hope you're having a great day, FIRSTNAME!"]
    greetings_no_names = ["Welcome!", "Great to see you!", "Hi!", "Welcome back!"]

    if user_name:
        random_index = random.randrange(len(greetings_incl_names))
        greeting = greetings_incl_names[random_index]
        print(user_name)
        greeting = greeting.replace("FIRSTNAME", user_name.replace('"', ''))
    else:
        random_index = random.randrange(len(greetings_no_names))
        greeting = greetings_no_names[random_index]

    return {"greeting": greeting} 
