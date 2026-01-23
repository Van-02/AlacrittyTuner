import sys
from .cli import cli
from .config_manager import change_opacity, change_theme, get_available_themes
from .exceptions import ATError


def main():
    try:
        if len(sys.argv) == 1:
            raise ATError("Use -h or --help for information.")

        args = cli()

        if args.list:
            themes = get_available_themes()
            print("--- Themes ---")
            for t in themes:
                print(f" - {t}")
            return

        if args.theme:
            change_theme(args.theme)

        if args.opacity is not None:
            change_opacity(args.opacity)

    except ATError as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    main()
