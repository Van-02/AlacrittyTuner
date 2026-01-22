import argparse


def cli() -> argparse.Namespace:
    """
    Configures the CLI arguments for AlacrittyTuner.
    Uses subcommands for better scalability and UX.
    """
    parser = argparse.ArgumentParser(
        prog="AlacrittyTuner",
        description="A command line interface to change Alacritty configuration.",
    )

    parser.add_argument("-t", "--theme", help="Name of the theme to apply")

    parser.add_argument(
        "-l", "--list", action="store_true", help="List available themes"
    )

    parser.add_argument(
        "-o", "--opacity", type=float, help="Window opacity (0.0 to 1.0)"
    )
    args = parser.parse_args()

    return args
