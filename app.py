from flask import Flask
import random
app = Flask(__name__)

jokes = [
    "Relationship status? I'll leave the relations to the database.",
    "I'd tell you a UDP joke, but you might not get it",
    "A pair of jumper cables walks into a bar. Bartender says: “Ill serve you, but dont start anything.” ",
    "Q. How do you catch an Ether Bunny.A. With an Ethernet!!",
    "Q. What is Tom Hanks' wireless password? A. 1Forrest1",
    "Q.What did the fish say when he swam into a wall? A. DAM"
]


@app.get("/")
def tell_a_joke():
    joke = random.choice(jokes)
    return f"<p>{joke}</p>"
