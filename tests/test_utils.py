import sys
from pathlib import Path
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from utils import create_completions


def test_create_completions_builds_prompt_and_calls_client():
    mock_client = Mock()
    mock_message = Mock(content="answer")
    mock_client.chat.completions.create.return_value = Mock(choices=[Mock(message=mock_message)])
    with patch("utils.build_prompt", return_value=[{"role": "user", "content": "hi"}]) as mock_build:
        result = create_completions(mock_client, "question", [("q", "a")])

    mock_build.assert_called_once_with("question", [("q", "a")])
    mock_client.chat.completions.create.assert_called_once_with(
        extra_body={},
        model="meta-llama/llama-4-maverick:free",
        messages=[{"role": "user", "content": "hi"}],
    )
    assert result == "answer"

