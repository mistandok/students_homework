# реализуйте декоратор вида @retry(count: int, delay: timedelta, handled_exceptions: tuple[type(Exceptions)])

from datetime import timedelta


def retry(count: int, delay: timedelta, handled_exceptions: tuple = (Exception,)):
    """Декоратор для повторных попыток выполнения функции."""
    # TODO: реализовать декоратор
    pass

