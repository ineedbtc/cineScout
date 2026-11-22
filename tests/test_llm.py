# tests/test_llm.py

from ollama import ChatResponse, Message

from cinescout import llm


def test_ask_returns_answer_text(monkeypatch):

    def fake_chat(model, messages) -> ChatResponse:

        fake_message = Message(role="assistant", content="Hello")
        response = ChatResponse(message=fake_message)

        return response

    monkeypatch.setattr(llm.ollama, "chat", fake_chat)

    assert llm.ask("Hallo fake chat") == "Hello"


def test_ask_sends_question_as_user_message(monkeypatch):

    captured = {}
    question = "Hallo fake chat, wie geht es dir?"

    def fake_chat(model, messages) -> ChatResponse:

        captured["messages"] = messages
        fake_message = Message(role="assistant", content="Hello")
        response = ChatResponse(message=fake_message)

        return response

    monkeypatch.setattr(llm.ollama, "chat", fake_chat)

    llm.ask(question)

    assert captured["messages"][-1]["role"] == "user"
    assert captured["messages"][-1]["content"] == question
