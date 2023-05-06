import pytest
from unittest.mock import patch
from typer.testing import CliRunner
from app.main import app

runner = CliRunner()

@pytest.fixture
def mock_os_path_exists():
    with patch("app.cli.os.path.exists", autospec=True) as mock_exists:
        yield mock_exists

def test_init_already_initialized(mock_os_path_exists):
    mock_os_path_exists.return_value = True

    result = runner.invoke(app, ["init"])
    assert result.exit_code == 0
    assert "Initialisierung bereits abgeschlossen" in result.stdout


def test_init_successful(mock_os_path_exists):
    mock_os_path_exists.return_value = False

    with patch("app.cli.create_env_file") as mock_create_env_file, \
         patch("app.cli.create_tables") as mock_create_tables:

        result = runner.invoke(app, ["init"])

        mock_create_env_file.assert_called_once()
        mock_create_tables.assert_called_once()

        assert result.exit_code == 0
        assert "Initialisierung erfolgreich" in result.stdout


