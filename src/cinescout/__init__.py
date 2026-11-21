import sys

from cinescout import llm


# src/cinescout/__init__.py
def main() -> None:

    if len(sys.argv) > 1:
        print(llm.ask(sys.argv[1]))
    else:
        print("Du hast keine Frage gestellt.")
