def clean_string(unclean: str) -> set:
    return set(unclean.lower().replace('<', '').replace('>', '').replace("'", '"').split(" "))


def tags_equal(first_string: str, second_string: str) -> bool:
    return clean_string(first_string).difference(clean_string(second_string)) == set()
