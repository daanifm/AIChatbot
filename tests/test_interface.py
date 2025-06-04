import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from interface import get_html


def test_get_html_contains_expected_css():
    html = get_html()
    assert "<style>" in html
    assert "#chatbot" in html

