import random, string


def random_str(length: int = 10) -> str:
    return "".join(random.choices(string.ascii_letters, k=length))
