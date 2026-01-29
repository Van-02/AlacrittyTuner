from pathlib import Path
from tomlkit import dumps, parse, TOMLDocument
from alacritty_tuner.exceptions import ConfigError


class AlacrittyTuner:
    def __init__(self):
        """
        Initializes the tuner by locating Alacritty's config directory.
        Currently defaults to Linux/macOS standard path (~/.config/alacritty)
        """
        self.base_path = Path().home() / ".config" / "alacritty"
        self.config_file = self.base_path / "alacritty.toml"

        # Safety check: Ensure the directory and config exist before proceeding
        if not self.base_path.exists():
            raise ConfigError("Alacritty directory not found")

        if not self.config_file.exists():
            raise ConfigError("Alacritty config file not found")

        # Load existing configuration into memory
        self.config = self._load(self.config_file)

    def _load(self, toml_file: Path) -> TOMLDocument:
        """
        Helper to read and parse a TOML file into a dictionary.
        """
        with open(toml_file, "r") as f:
            return parse(f.read())

    def apply(self):
        """
        Writes the current in-memory configuration back to the alacritty.toml file.
        """
        with open(self.config_file, "w") as f:
            f.write(dumps(self.config))

    def change_theme(self, theme_name: str):
        """
        Updates the color scheme by merging a specific theme file
        located in the 'themes' subdirectory.
        """
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

        # Overwrite the 'colors' section in the main config
        self.config["colors"] = theme["colors"]

    def list_themes(self) -> list:
        """
        Returns a list of available theme names.
        """
        themes_directory = self.base_path / "themes"
        return [f.stem for f in themes_directory.glob("*.toml")]

    def change_font(self, family_font: str):
        """
        Sets the font family for normal, bold, and italic styles.
        Uses aliases from fonts.toml if available.
        """
        font_map = self._get_font_map()
        aliases = font_map.get("aliases", {})

        # Determine the real font name based on the alias or use the raw input
        family_name = aliases.get(family_font.lower(), family_font)
        if "font" not in self.config:
            self.config["font"] = {}

        font_section = self.config["font"]
        styles = ["normal", "bold", "italic"]

        # Apply the font family across all standard styles
        for style in styles:
            if style not in font_section:
                font_section[style] = {}

            font_section[style]["family"] = family_name

    def _get_font_map(self) -> TOMLDocument:
        """
        Retrieves font mapping from the dedicated fonts.toml file.
        """
        font_file = self.base_path / "fonts.toml"
        if not font_file.exists():
            default_content = '[aliases]\nubuntumono = "UbuntuMono Nerd Font"\n'
            font_file.write_text(default_content)

        fonts = self._load(font_file)
        return fonts

    def list_fonts(self) -> TOMLDocument:
        """
        Returns the full dictionary of font aliases for display purposes.
        """
        font_map = self._get_font_map()
        aliases = font_map.get("aliases", {})
        if not aliases:
            raise ConfigError("No font aliases found in fonts.toml")

        return aliases

    def change_opacity(self, value: float):
        """
        Sets the window background opacity. Value must be between 0.0 and 1.0
        """
        if not (0.0 <= value <= 1.0):
            raise ConfigError("Opacity must be between 0.0 to 1.0")

        if "window" not in self.config:
            self.config["window"] = {}

        self.config["window"]["opacity"] = value

    def change_size(self, value: int):
        """
        Updates the global font size in the configuration.
        """
        if "font" not in self.config:
            self.config["font"] = {}

        self.config["font"]["size"] = value

    def change_padding(self, x: int, y: int):
        """
        Updates the window padding (X and Y axis) for Alacritty.
        """
        if "window" not in self.config:
            self.config["window"] = {}
        if "padding" not in self.config["window"]:
            self.config["window"]["padding"] = {}

        self.config["window"]["padding"]["x"] = x
        self.config["window"]["padding"]["y"] = y
