import pytest
from alacritty_tuner.config_manager import AlacrittyTuner
from alacritty_tuner.exceptions import ConfigError


def test_change_theme_valid_merge(mocker):
    mocker.patch.object(AlacrittyTuner, "__init__", return_value=None)
    tuner = AlacrittyTuner()

    from pathlib import Path

    tuner.base_path = Path("/tmp/fake_alacritty")
    tuner.config = {
        "font": {"size": 12},
        "colors": {"primary": {"background": "#000000"}},
    }

    mocker.patch("pathlib.Path.exists", return_value=True)

    theme_content = {
        "colors": {
            "primary": {"background": "#282a36", "foreground": "#f8f8f2"}
        }
    }

    mocker.patch.object(tuner, "_load", return_value=theme_content)
    tuner.change_theme("dracula")

    assert tuner.config["colors"]["primary"]["background"] == "#282a36"
    assert tuner.config["font"]["size"] == 12


def test_change_theme_missing_colors_section(mocker):
    mocker.patch.object(AlacrittyTuner, "__init__", return_value=None)
    tuner = AlacrittyTuner()

    from pathlib import Path

    tuner.base_path = Path("/tmp/fake_alacritty")
    tuner.config = {}

    mocker.patch("pathlib.Path.exists", return_value=True)

    invalid_theme = {"metadata": {"author": "Unknown"}}
    mocker.patch.object(tuner, "_load", return_value=invalid_theme)

    with pytest.raises(ConfigError, match="does not contain color config"):
        tuner.change_theme("broken_theme")


def test_change_font_with_alias(mocker):
    mocker.patch.object(AlacrittyTuner, "__init__", return_value=None)
    tuner = AlacrittyTuner()

    tuner.config = {}

    mocker.patch.object(
        tuner,
        "_get_font_map",
        return_value={"aliases": {"ubuntu": "UbuntuMono Nerd Font"}},
    )

    tuner.change_font("UBUNTU".lower())

    assert tuner.config["font"]["normal"]["family"] == "UbuntuMono Nerd Font"
    assert tuner.config["font"]["bold"]["family"] == "UbuntuMono Nerd Font"
    assert tuner.config["font"]["italic"]["family"] == "UbuntuMono Nerd Font"


def test_change_font_direct_name(mocker):
    mocker.patch.object(AlacrittyTuner, "__init__", return_value=None)
    tuner = AlacrittyTuner()
    tuner.config = {}

    mocker.patch.object(tuner, "_get_font_map", return_value={"aliases": {}})

    tuner.change_font("Comic Sans")

    assert tuner.config["font"]["normal"]["family"] == "Comic Sans"


def test_change_opacity_valid_value(mocker):
    """
    Test that opacity updates correctly within the 0.0 - 1.0 range.
    """
    mocker.patch.object(AlacrittyTuner, "__init__", return_value=None)

    tuner = AlacrittyTuner()
    tuner.config = {}

    tuner.change_opacity(0.5)

    assert tuner.config["window"]["opacity"] == 0.5


def test_change_opacity_invalid_value(mocker):
    """
    Test that opacity raises ConfigError if value is out of bounds.
    """
    mocker.patch.object(AlacrittyTuner, "__init__", return_value=None)
    tuner = AlacrittyTuner()

    with pytest.raises(ConfigError, match="Opacity must be between 0.0 to 1.0"):
        tuner.change_opacity(1.5)


def test_change_padding(mocker):
    mocker.patch.object(AlacrittyTuner, "__init__", return_value=None)
    tuner = AlacrittyTuner()
    tuner.config = {}

    tuner.change_padding(20, 25)

    assert tuner.config["window"]["padding"]["x"] == 20
    assert tuner.config["window"]["padding"]["y"] == 25


def test_change_size(mocker):
    mocker.patch.object(AlacrittyTuner, "__init__", return_value=None)
    tuner = AlacrittyTuner()
    tuner.config = {}

    tuner.change_size(16)
    assert tuner.config["font"]["size"] == 16


def test_init_raises_error_if_no_directory(mocker):
    mocker.patch("pathlib.Path.exists", return_value=False)

    with pytest.raises(ConfigError, match="Alacritty directory not found"):
        AlacrittyTuner()  #


def test_change_theme_missing_dir(mocker):
    mocker.patch.object(AlacrittyTuner, "__init__", return_value=None)
    tuner = AlacrittyTuner()
    from pathlib import Path

    tuner.base_path = Path("/tmp/fake")

    mocker.patch("pathlib.Path.exists", return_value=False)

    with pytest.raises(ConfigError, match="Themes directory not found"):
        tuner.change_theme("any")  #


def test_apply_writes_to_file(tmp_path, mocker):
    """
    Verifies that apply() actually saves the TOML document to disk.
    """

    d = tmp_path / "alacritty"
    d.mkdir()
    f = d / "alacritty.toml"
    f.write_text("[window]\nopacity = 1.0")

    mocker.patch.object(AlacrittyTuner, "__init__", return_value=None)
    tuner = AlacrittyTuner()
    tuner.config_file = f
    tuner.config = {"window": {"opacity": 0.8}}

    tuner.apply()

    content = f.read_text()
    assert "opacity = 0.8" in content
