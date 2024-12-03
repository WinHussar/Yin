from bakery import assert_equal

# Page class to represent a route's return value
class Page:
    def __init__(self, content: str):
        self.content = content

    def __str__(self):
        return self.content

# Dataclass to store the state of the application
class State:
    def __init__(self):
        self.title = "Welcome to My Game"
        self.user_scores = []  # List of user scores
        self.message = "Hello, world!"

# Global application state
app_state = State()

# Define the five routes
def index() -> Page:
    """Index route"""
    return Page(app_state.title)

def about() -> Page:
    """About route"""
    return Page("This is a game about exploration and fun!")

def scores() -> Page:
    """Scores route"""
    if app_state.user_scores:
        scores_list = ', '.join(map(str, app_state.user_scores))
        return Page(f"User scores: {scores_list}")
    return Page("No scores yet!")

def add_score(score: str) -> Page:
    """Add score route"""
    try:
        score = int(score)
        app_state.user_scores.append(score)
        return Page(f"Score {score} added!")
    except ValueError:
        return Page("Invalid score! Please enter a number.")

def message() -> Page:
    """Message route"""
    return Page(app_state.message)

# Router to map routes
def router(route: str) -> Page:
    """Router to handle routes"""
    if route == "/index":
        return index()
    elif route == "/about":
        return about()
    elif route == "/scores":
        return scores()
    elif route.startswith("/add_score "):
        score = route.split("/add_score ")[-1]
        return add_score(score)
    elif route == "/message":
        return message()
    else:
        return Page("404 Not Found: Unknown route!")

# Unit tests for routes
def test_routes():
    assert_equal(str(index()), "Welcome to My Game")
    assert_equal(str(about()), "This is a game about exploration and fun!")
    assert_equal(str(scores()), "No scores yet!")
    
    assert_equal(str(add_score("50")), "Score 50 added!")
    assert_equal(str(scores()), "User scores: 50")
    assert_equal(str(add_score("abc")), "Invalid score! Please enter a number.")
    assert_equal(str(message()), "Hello, world!")

# Main function to run the program
def main():
    print("Welcome to the game server!")
    print("Available routes: /index, /about, /scores, /add_score <number>, /message")

    while True:
        route = input("Enter a route (or 'quit' to exit): ")
        if route == "quit":
            print("Goodbye!")
            break
        else:
            print(router(route))

# Run tests before starting the server
test_routes()

# Start the main server
main()