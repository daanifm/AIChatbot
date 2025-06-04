import sys
from pathlib import Path
from unittest.mock import patch
import types

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

# Provide dummy modules so app can be imported
sys.modules.setdefault("openai", types.SimpleNamespace(OpenAI=object))
sys.modules.setdefault(
    "gradio",
    types.SimpleNamespace(
        Blocks=object,
        Chatbot=object,
        Row=object,
        Textbox=object,
        Button=object,
        HTML=object,
        Markdown=object,
    ),
)

import app


def test_chatbot_interface_updates_history_and_interaccion():
    app.interaccion.clear()
    with patch("app.init_client") as mock_init_client, \
         patch("app.create_completions", return_value="resp") as mock_create:
        history = []
        updated, returned = app.chatbot_interface("hello", history)
        mock_init_client.assert_called_once()
        mock_create.assert_called_once()
        called_args = mock_create.call_args[0]
        assert called_args[0] is mock_init_client.return_value
        assert called_args[1] == "hello"
        assert updated == [("hello", "resp")]
        assert returned is updated
        assert app.interaccion == [("hello", "resp")]


def test_launch_gradio_interface_calls_launch():
    created = {}

    class DummyBlocks:
        def __enter__(self):
            created['demo'] = self
            return self
        def __exit__(self, exc_type, exc, tb):
            pass
        def launch(self):
            created['launched'] = True

    class DummyRow:
        def __enter__(self):
            return self
        def __exit__(self, exc_type, exc, tb):
            pass

    class DummyComponent:
        def __init__(self, *args, **kwargs):
            pass
        def click(self, *args, **kwargs):
            pass
        def submit(self, *args, **kwargs):
            pass

    with patch("app.gr.Blocks", return_value=DummyBlocks()), \
         patch("app.gr.Row", return_value=DummyRow()), \
         patch("app.gr.HTML", new=DummyComponent), \
         patch("app.gr.Markdown", new=DummyComponent), \
         patch("app.gr.Chatbot", new=DummyComponent), \
         patch("app.gr.Textbox", new=DummyComponent), \
         patch("app.gr.Button", new=DummyComponent), \
         patch("app.get_html", return_value="css"):
        app.launch_gradio_interface()

    assert created.get('launched') is True

