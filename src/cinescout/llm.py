import ollama

MODEL = "qwen2.5:7b"


def ask(question: str) -> str:

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "Du bist ein Filmexperte, der kurz und auf Deutsch antwortet.",
            },
            {"role": "user", "content": question},
        ],
    )
    return response.message.content
