# AlacrittyTuner

**Idioma**
E🇪🇸 Español
[🇺🇸 Ingles](./README.md)

AlacrittyTuner es una herramienta de CLI de grado profesional diseñada para gestionar y recargar instantáneamente la configuración de tu terminal Alacritty. Cambiá temas, fuentes y propiedades de la ventana al instante.

## Caracteristicas Clave

- **Alias de fuentes**: Mapeá nombres cortos y fáciles de recordar a familias complejas de Nerd Fonts a través de fonts.toml.
- **Cambio de temas en vivo**: Intercambia esquemas de colores sin tener que editar archivos a mano.
- **Control dinamico de Ventana**: Ajusta la opacidad, el tamaño de la fuente y el padding con facilidad.
- **Amigable para desarrolladores**: Construido con codigo Python limpio y modular.

## Instalacion

### Para usuarios de Arch Linux (AUR)

Si estas en Arch, podes instalarlo usando tu helper de AUR favorito.

```bash
paru -S alacrittytuner
```

## Configuración

La herramienta encuentra automáticamente tu `alacritty.toml` en `~/.config/alacritty/`

### Aliases de fuentes

Crea un archivo `fonts.toml` en tu directorio de configuracion de Alacritty para definir tus alias:

```Toml
[aliases]
mononoki = "Mononoki Nerd Font Mono"
ubuntumono = "UbuntuMono Nerd Font"
hack = "Hack Nerd Font Mono"
firacode = "FiraCode Nerd Font Mono"
```

### Temas personalizados

Guarda tus archivos de tema en `~/.config/alacritty/themes/*.toml`. Por ejemplo:

```custom.toml
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

## Uso

| Opción              | Descripción                                  | Uso                |
| ------------------- | -------------------------------------------- | ------------------ |
| --list-themes (-lt) | Lista todos los temas disponibles            | atuner -lt         |
| --list-fonts (-lf)  | Lista todos los aliases de fuentes           | atuner -lf         |
| --theme (-t)        | Aplica un tema de color especifico           | atuner -t dracula  |
| --font (-f)         | Aplica una familia de fuentes o alias        | atuner -f mononoki |
| --opacity (-o)      | Asigna la opacidad de la ventana (0.0 a 1.0) | atuner -o 0.85     |
| --size (-s)         | Asigna el tamaño de fuente global            | atuner -s 14       |
| --padding (-p)      | Asigna el padding de la ventana (X e Y)      | atuner -p 20 20    |
