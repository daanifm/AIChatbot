import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from prompt import build_prompt


def test_build_prompt_with_interaction_list():
    interaction = [("Q1", "A1"), ("Q2", "A2")]
    question = "Q3?"
    prompt_messages = build_prompt(question, interaction)

    expected_interaction_text = "\n".join([
        "Usuario: Q1\nAsistente: A1",
        "Usuario: Q2\nAsistente: A2",
    ])
    expected_user_content = (
        f"Interacci\u00f3n previa:\n{expected_interaction_text}\n\nPregunta:\n{question}"
    )

    # The result should be a list with system and user messages
    assert isinstance(prompt_messages, list)
    assert prompt_messages[1]["role"] == "user"
    assert prompt_messages[1]["content"] == expected_user_content.strip()
