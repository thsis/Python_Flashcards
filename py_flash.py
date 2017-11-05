from sys import argv
import json
import random

script_name, dictionary_path = argv

print("""Welcome to Python Flashcards. To see the next Flashcard hit RETURN.
To end the script hit CTRL-D.""")

with open(dictionary_path) as qa_dict:
        d = json.load(qa_dict)
        q = list(d.keys())
        a = list(d.values())
        try:
            while True:
                i = random.randint(0, len(d) - 1)
                print("QUESTION:\n {}\n".format(q[i]))
                input(">")
                print("ANSWER:\n {}\n".format(a[i]))
                input(">")
        except EOFError:
            print("\nBye!")
