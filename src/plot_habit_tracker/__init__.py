import typer

from .plot import plot_habit_tracker


def main():
    typer.run(plot_habit_tracker)
