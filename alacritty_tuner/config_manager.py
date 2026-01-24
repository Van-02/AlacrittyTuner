from pathlib import Path
from tomlkit import dumps, parse
from alacritty_tuner.exceptions import ConfigError


class AlacrittyTuner:
    def __init__(self):
        self.base_path = Path().home() / ".config" / "alacritty"
        self.config_file = self.base_path / "alacritty.toml"

        if not self.base_path.exists():
            raise ConfigError("Alacritty directory not found")

        if not self.config_file.exists():
            raise ConfigError("Alacritty config file not found")

        self.config = self._load(self.config_file)

    def _load(self, toml_file):
        with open(toml_file, "r") as f:
            return parse(f.read())

    def apply(self):
        with open(self.config_file, "w") as f:
            f.write(dumps(self.config))

    def change_theme(self, theme_name: str):
        themes_directory = self.base_path / "themes"
        if not themes_directory.exists():
            raise ConfigError("Themes directory not found")

        theme_file = themes_directory / f"{theme_name}.toml"
        if not theme_file.exists():
            raise ConfigError(
                f"Theme '{theme_name}' not found in {themes_directory}"
            )

        theme = self._load(theme_file)
        if theme is None:
            raise ConfigError(f"File {theme_file.name} is empty")
        if "colors" not in theme:
            raise ConfigError(f"{theme_file} does not contain color config")

        self.config["colors"] = theme["colors"]

    def list_themes(self):
        themes_directory = self.base_path / "themes"
        return [f.stem for f in themes_directory.glob("*.toml")]

    def change_font(self, family_font: str):
        font_map = self._get_font_map()

        aliases = font_map.get("aliases", {})
        family_name = aliases.get(family_font.lower(), family_font)
        if "font" not in self.config:
            self.config["font"] = {}

        font_section = self.config["font"]
        styles = ["normal", "bold", "italic"]

        for style in styles:
            if style not in font_section:
                font_section[style] = {}

            font_section[style]["family"] = family_name

    def _get_font_map(self):
        font_file = self.base_path / "fonts.toml"
        if not font_file.exists():
            raise ConfigError("fonts file not found")

        fonts = self._load(font_file)
        return fonts

    def list_fonts(self):
        font_map = self._get_font_map()
        aliases = font_map.get("aliases", {})
        if not aliases:
            raise ConfigError("No font aliases found in fonts.toml")

        return aliases

    def change_opacity(self, value: float):
        if not (0.0 <= value <= 1.0):
            raise ConfigError("Opacity must be between 0.0 to 1.0")

        if "window" not in self.config:
            self.config["window"] = {}

        self.config["window"]["opacity"] = value

    def change_size(self, value: int):
        if "font" not in self.config:
            self.config["font"] = {}

        self.config["font"]["size"] = value

    def change_padding(self, x: int, y: int):
        if "window" not in self.config:
            self.config["window"] = {}
        if "padding" not in self.config["window"]:
            self.config["window"]["padding"] = {}

        self.config["window"]["padding"]["x"] = x
        self.config["window"]["padding"]["y"] = y
