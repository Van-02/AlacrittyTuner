from tomlkit import dumps, parse
from pathlib import Path
from alacritty_tuner.exceptions import ATError


def get_alacritty_config_path():  # -> Path
    path = Path.home() / ".config" / "alacritty" / "alacritty.toml"
    return path


def get_themes_path() -> Path:
    """
    Returns the path to the user's themes folder.
    """
    path = Path.home() / ".config" / "alacritty" / "themes"

    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
    return path


def change_theme(name_theme):
    config_path = get_alacritty_config_path()

    if not config_path.exists():
        raise ATError("alacritty.toml not found")

    with open(config_path, "r") as f:
        config = parse(f.read())

    theme_path = get_themes_path() / f"{name_theme}.toml"

    if not theme_path.exists():
        raise ATError(f"The theme '{name_theme}' not found in {theme_path}")

    with open(theme_path, "r") as f:
        new_theme = parse(f.read())

    config["colors"] = new_theme["colors"]

    with open(config_path, "w") as f:
        f.write(dumps(config))

    print(f"Success: {name_theme} theme apply!")


def get_available_themes():
    theme_path = get_themes_path()
    return [f.stem for f in theme_path.glob("*.toml")]


def change_opacity(value: float):
    if not (0.0 <= value <= 1.0):
        raise ATError("Opacity must be between 0.0 to 1.0")

    config_path = get_alacritty_config_path()

    with open(config_path, "r") as f:
        config = parse(f.read())

    if "window" not in config:
        config["window"] = {}

    config["window"]["opacity"] = value

    with open(config_path, "w") as f:
        f.write(dumps(config))

    print(f"Success: Opacity set to {value}")
