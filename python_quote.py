import random

quotes = ("It's just a flesh wound.",
          "He's not the MEssiah. He's a very naughty boy!",
          "This is an EX-PARROT!!")


def random_python_qoute():
    rand_index = random.randint(0, len(quotes) - 1 )
    return quotes[rand_index]

if __name__ == '__main__':
    quote = random_python_qoute()
    print(quote)