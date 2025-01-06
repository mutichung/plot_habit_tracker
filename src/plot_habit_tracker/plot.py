import calendar
import os
import logging
from typing import Optional

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def int_to_month(month_int: int) -> str:
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }

    if month_int in month_names:
        return month_names[month_int]
    else:
        return "Invalid month number"


def get_days_in_month(month: int, year: int) -> int:
    """
    Returns the number of days in the given month.

    Args:
        month: The month (1-12).
        year: The year.

    Returns:
        The number of days in the month.
    """
    return calendar.monthrange(year, month)[1]


def plot_habit_tracker(
    name: str, habits: list[str], month: int, year: Optional[int] = None
):
    # Enable XKCD style
    plt.xkcd()

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(6, 4))  # set size to post card
    ax.set_aspect("equal", adjustable="datalim")

    # Set title and styling
    plt.title(f"{name}'s {int_to_month(month)} Habit Tracker\n", fontsize=15, pad=10)

    # Create grid for habits
    if year is None:
        import datetime

        year = datetime.date.today().year
    num_days = get_days_in_month(month, year)
    num_habits = len(habits)

    # Draw circles for each day and habit
    for i in range(num_habits):
        for j in range(num_days):
            circle = Circle(
                (j * 0.5, i * 1 + 0.5), 0.18, fill=False, color="black", alpha=0.3
            )
            ax.add_patch(circle)

    # Add habit labels with more space
    habits = habits[::-1]
    for i, habit in enumerate(habits):
        plt.text(
            -0.5,
            i * 1 + 0.5,
            habit,
            verticalalignment="center",
            horizontalalignment="right",
            fontsize=8,
        )

    # Add day numbers
    for i in range(num_days):
        plt.text(
            i * 0.5,
            num_habits + 0.6,
            str(i + 1),
            horizontalalignment="center",
            verticalalignment="center",
            fontsize=7,
        )
        day_capital = calendar.day_name[calendar.weekday(year, month, i + 1)][0]
        plt.text(
            i * 0.5,
            num_habits + 0.25,
            day_capital,
            horizontalalignment="center",
            verticalalignment="center",
            fontsize=7,
            color="red" if day_capital == "S" else "black",
        )

    # Set axis limits and remove ticks
    plt.xlim(-1.2, num_days * 0.5 + 0.2)
    plt.ylim(-0.5, num_habits + 0.5)
    plt.xticks([])
    plt.yticks([])

    # Adjust layout
    plt.tight_layout()

    # Remove spines
    for spine in ax.spines.values():
        spine.set_visible(False)

    filename = f"{name.lower()}_{int_to_month(month).lower()}.png"
    plt.savefig(
        filename,
        format="png",
        bbox_inches="tight",
        dpi=300,
    )
    logger.info(f"Image generated at {os.path.abspath(filename)}")
    # Show the plot
    plt.show()
