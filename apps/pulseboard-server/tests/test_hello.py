import pytest

from pulseboard_server.greeting import hello_message
from pulseboard_server.main import main


def test_hello_message() -> None:
    assert hello_message() == "Hello from pulseboard!"


def test_main_prints_hello(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from pulseboard!\n"
