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
        "-lt",
        "--list-themes",
        action="store_true",
        help="List available themes",
    )
    parser.add_argument(
        "-lf",
        "--list-fonts",
        action="store_true",
        help="List available font aliases",
    )

    parser.add_argument("-f", "--font", help="Name of the font family to apply")

    parser.add_argument(
        "-o", "--opacity", type=float, help="Window opacity (0.0 to 1.0)"
    )

    parser.add_argument("-s", "--size", type=int, help="Set font size")

    parser.add_argument(
        "-p",
        "--padding",
        type=int,
        nargs=2,
        metavar=("x", "y"),
        help="Window padding",
    )

    args = parser.parse_args()

    return args
