import sys
from pathlib import Path
from unittest.mock import patch
import types

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

# Provide dummy openai before importing config
sys.modules.setdefault("openai", types.SimpleNamespace(OpenAI=object))

import config
import app


def test_main_calls_init_and_launch():
    with patch.object(config, "init_client") as mock_init, \
         patch.object(app, "launch_gradio_interface") as mock_launch:
        if "main" in sys.modules:
            del sys.modules["main"]
        import main
        mock_init.assert_called_once()
        mock_launch.assert_called_once()

