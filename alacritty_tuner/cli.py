import argparse


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="AlacrittyTuner",
        description="A command line interface to change Alacritty configuration.",
    )

    parser.add_argument("-t", "--theme", help="Name of the theme to apply")

    parser.add_argument(
        "-l", "--list", action="store_true", help="List available themes"
    )

    args = parser.parse_args()

    return args
