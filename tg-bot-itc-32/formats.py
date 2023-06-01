DATE_FORMAT = "%d.%m.%Y"
HUMAN_READABLE_DATE_FORMAT = "день.месяц.год"
HUMAN_READABLE_DURATION_FORMAT = "час:минута:секунды"


def validate_duration(duration: str) -> bool:
    duration_list = duration.split(":")
    if len(duration_list) != 3:
        return False
    if not all(map(
        lambda duration_str: duration_str.isdecimal(),
        duration_list
    )):
        return False
    hour, minute, second = map(int, duration_list)
    return not any([
        hour > 23 or hour < 0,
        minute > 60 or minute < 0,
        second > 60 or second < 0
    ])
