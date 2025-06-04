import sys
from pathlib import Path
from unittest.mock import patch, Mock
import types

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

# Provide a dummy openai module so config can be imported
sys.modules.setdefault("openai", types.SimpleNamespace(OpenAI=Mock()))

import config


def test_init_client_creates_openai_instance():
    with patch("config.OpenAI") as mock_openai:
        client = config.init_client()
        mock_openai.assert_called_once_with(
            base_url="https://openrouter.ai/api/v1",
            api_key="OpenRouter ApiKey",
        )
        assert client is mock_openai.return_value

