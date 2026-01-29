# AlacrittyTuner 

**Language**

🇺🇸 English
[🇪🇸 Spanish](/README.es.md)

**AlacrittyTuner** is a professional-grade CLI tool designed to manage and hot-reload your Alacritty terminal configuration. Change themes, fonts, and padding instantly

## Key Features

- **Font Aliasing**: Map short, easy-to-remember names to complex Nerd Font families via `fonts.toml`.
- **Live Theme Switching**: Swap color schemes without manual file editing.
- **Dynamic Padding**: Adjust opacity, font size, and padding on the fly.
- **Developer Friendly**: Built with clean, modular Python code.

## Installation

### For Arch Linux Users (AUR)

If you are on Arch, you can install it using your favorite AUR helper:

```bash
paru -S alacrittytuner
```

## Configuration

The tool automatically finds your `alacritty.toml` at `~/.config/alacritty/`.

### Font Aliases

Create a `fonts.toml` file in your Alacritty config directory to define your aliases:

```Toml
[aliases]
mononoki = "Mononoki Nerd Font Mono"
ubuntumono = "UbuntuMono Nerd Font"
hack = "Hack Nerd Font Mono"
firacode = "FiraCode Nerd Font Mono"
```

### Theme Config

Place your theme files in `~/.config/alacritty/themes/*.toml`.

```Toml
[colors.primary]
background = ''
foreground = ''

[colors.normal]
black = ''
red = ''
green = ''
yellow = ''
blue = ''
magenta = ''
cyan = ''
white = ''

[colors.bright]
black = ''
red = ''
green = ''
yellow = ''
blue = ''
magenta = ''
cyan = ''
white = ''
```

## Usage

| Option              | Description                     | Usage              |
| ------------------- | ------------------------------- | ------------------ |
| --list-themes (-lt) | List all available themes       | atuner -lt         |
| --list-fonts (-lf)  | List all defined font aliases   | atuner -lf         |
| --theme (-t)        | Apply a specific color theme    | atuner -t dracula  |
| --font (-f)         | Apply a font family or alias    | atuner -f mononoki |
| --opacity (-o)      | Set window opacity (0.0 to 1.0) | atuner -o 0.85     |
| --size (-s)         | Set global size                 | atuner -s 14       |
| --padding (-p)      | Set window padding (X and Y)    | atuner -p 20 20    |
