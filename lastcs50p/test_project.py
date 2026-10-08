import sys
from pathlib import Path
import types

sys.path.insert(0, str(Path(__file__).resolve().parent))

import project


def test_serch_usdt_pair_filters_usdt_markets():
    payload = {
        "symbols": [
            {"symbol": "BTCUSDT"},
            {"symbol": "ETHBTC"},
            {"symbol": "SOLUSDT"},
            {"symbol": "DOGEUSDC"},
        ]
    }

    assert project.serch_usdt_pair(payload) == ["BTC", "SOL"]


def test_format_price_formats_numeric_value():
    assert project.format_price(1234.5) == "$1,234.50"
    assert project.format_price(0) == "$0.00"


def test_ai_recomendation_returns_openai_response(monkeypatch):
    class FakeResponses:
        def create(self, model, input):
            assert model == "gpt-4.1-mini"
            assert "Binance" in input
            assert "1000" in input
            assert "BTC" in input
            return types.SimpleNamespace(output_text="Buy BTC for long-term growth.")

    class FakeOpenAI:
        def __init__(self, api_key):
            self.api_key = api_key
            self.responses = FakeResponses()

    monkeypatch.setattr(project, "api_key", "test-key")
    monkeypatch.setattr(project, "OpenAI", FakeOpenAI)

    result = project.ai_recomendation("Binance", 1000, ["BTC", "ETH"])

    assert result == "Buy BTC for long-term growth."
