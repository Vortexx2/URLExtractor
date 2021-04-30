from datetime import datetime


def datetime_from_line(line: str, from_csv: bool = False) -> datetime:
    """
    Given line, return the date and time in the `datetime` format.
    :param from_csv: If you are reading
    :param line: The line to find the date and time from.
    :return: Return the `datetime` object.
    """

    # The below code is done via indexing and not via regex is because if the line has a date
    # and time as well as a link, it will break.
    # date = "dd/mm/yyyy" or "%d/%m/%y"
    # time = "hh/mm" or "%H:%M"
    # date, time = line[0:10], line[12:17]

    date_and_time = line[0:17]

    if not from_csv:
        return datetime.strptime(date_and_time, "%d/%m/%Y, %H:%M")

    else:
        return datetime.strptime(date_and_time, "%d/%m/%Y,%H:%M,")
