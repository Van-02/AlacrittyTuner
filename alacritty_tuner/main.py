from sys import stderr
from alacritty_tuner.config_manager import AlacrittyTuner
from alacritty_tuner.cli import cli
from alacritty_tuner.exceptions import ConfigError


def main():
    args = cli()
    tuner = AlacrittyTuner()

    try:
        changed = False

        if args.theme:
            tuner.change_theme(args.theme)
            changed = True

        if args.list_themes:
            themes = tuner.list_themes()
            print("--- Themes ---")
            for t in themes:
                print(f" - {t}")
            return

        if args.list_fonts:
            aliases = tuner.list_fonts()
            print(f"{'ALIAS':<15} | {'FULL FONT NAME'}")
            print("-" * 50)
            for alias, full_name in aliases.items():
                print(f"{alias:<15} -> {full_name}")
            return

        if args.font:
            tuner.change_font(args.font)
            changed = True

        if args.opacity:
            tuner.change_opacity(args.opacity)
            changed = True

        if args.size:
            tuner.change_size(args.size)
            changed = True

        if args.padding:
            x, y = args.padding
            tuner.change_padding(x, y)
            changed = True

        if changed:
            tuner.apply()

    except ConfigError as e:
        print(e, file=stderr)
        exit(1)


if __name__ == "__main__":
    main()
