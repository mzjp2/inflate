# -*- coding: utf-8 -*-
""" Implementation of the inflate cli"""
import click
from colorama import Fore, Style

from inflate.inflate import CURRENCY, Inflate, __version__


@click.command()
@click.option(
    "--country", "-c", help="Country [either US/UK], default is UK", default="UK"
)
@click.option(
    "--inclusive",
    "-i",
    help="Include ending year, default no",
    is_flag=True,
    default=False,
)
@click.option(
    "--average",
    "-a",
    help="Show average annualised inflation, default no",
    is_flag=True,
    default=False,
)
@click.argument("start", type=click.INT)
@click.argument("end", type=click.INT)
@click.argument("amount", default=1.0)
@click.version_option(__version__)
# pylint: disable=too-many-arguments
def main(
    country: str = "UK",
    start: int = 0,
    end: int = 0,
    amount: int = 1,
    inclusive: bool = False,
    average: bool = False,
):
    """The entry hook for the click CLI

        Args:
            country: The country you want to compute inflation in
            start: The starting year to compute inflation from
            end: The ending year to compute inflation to
            amount: The amount of currency to compute inflation on
            inclusive: Whether to include the ending year or not in calculations
            average: Return the average value of inflatiion across the time period

        """
    inflated_object = Inflate(
        start_year=start, end_year=end, country=country, inclusive=inclusive
    )
    inflated_amount = inflated_object.inflate(amount)
    inclusive_text = "inclusive" if inclusive else "exclusive"
    is_was = "was" if start > end else "is"
    formatted_string = "{}{}{}{} in {}{}{} {} worth {}{}{}{} in {}{}{} ({}).".format(
        Fore.BLUE,
        CURRENCY[country.lower()],
        amount,
        Style.RESET_ALL,
        Fore.BLUE,
        start,
        Style.RESET_ALL,
        is_was,
        Fore.GREEN,
        CURRENCY[country.lower()],
        inflated_amount,
        Style.RESET_ALL,
        Fore.GREEN,
        end,
        Style.RESET_ALL,
        inclusive_text,
    )

    if average:
        formatted_string += (
            " "
            + "The average inflation across this period was {}{}%{}.".format(
                Fore.BLUE, inflated_object.average_inflation(), Style.RESET_ALL
            )
        )

    print(formatted_string)


if __name__ == "__main__":
    main()
