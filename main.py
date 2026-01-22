from alacritty_tuner.cli import cli
from alacritty_tuner.config_manager import (
    change_opacity,
    change_theme,
    get_available_themes,
)
from alacritty_tuner.exceptions import ATError


def main():
    try:
        args = cli()

        if args.list:
            themes = get_available_themes()
            print("--- Themes ---")
            for t in themes:
                print(f" - {t}")
            return

        if args.theme:
            change_theme(args.theme)

        if args.opacity:
            change_opacity(args.opacity)

        else:
            raise ATError("Use -h or --help for information.")

    except ATError as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    main()
