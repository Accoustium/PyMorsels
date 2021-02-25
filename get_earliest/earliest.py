def get_earliest(early, *dates):
    for date in dates:
        month, day, year = date.split("/")
        if int(year) < int(early.split("/")[2]):
            early = date
        elif (
            int(month) < int(early.split("/")[0]) and
            int(year) == int(early.split("/")[2])
        ):
            early = date
        elif (
            int(day) < int(early.split("/")[1]) and
            int(month) == int(early.split("/")[0]) and
            int(year) == int(early.split("/")[2])
        ):
            early = date

    return early
