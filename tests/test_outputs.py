import json
from pathlib import Path

REPORT = Path("/app/report.json")


def load():
    return json.loads(REPORT.read_text())


def test_report_exists():
    """Criterion 1: /app/report.json exists."""
    assert REPORT.exists()


def test_schema():
    """Criterion 2: report.json is a JSON object whose keys are exactly total_requests, unique_ips, top_path."""
    assert set(load().keys()) == {"total_requests", "unique_ips", "top_path"}


def test_total_requests():
    """Criterion 3: total_requests equals the number of request lines in the log (6)."""
    assert load()["total_requests"] == 6


def test_unique_ips():
    """Criterion 4: unique_ips equals the number of distinct client IP addresses (3)."""
    assert load()["unique_ips"] == 3


def test_top_path():
    """Criterion 5: top_path is the path requested most often (/index.html)."""
    assert load()["top_path"] == "/index.html"
