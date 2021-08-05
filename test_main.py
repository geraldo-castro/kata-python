from main import greet

def test_should_greet_thoughtworker():
    greeting = greet("thoughtworker")
    assert greeting == "Hello, thoughtworker!"
