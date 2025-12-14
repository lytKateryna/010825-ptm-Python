""" 04 Исключение при блокировке

Доработайте класс Door:
Создайте пользовательское исключение DoorBlockedError.
При попытке открыть дверь (или сменить код) во время блокировки
выбрасывайте это исключение вместо вывода сообщения.

Обработайте исключение в коде вызова.
"""

import time
from datetime import datetime, timedelta


class DoorBlockedError(Exception):
    """Raised when trying to access a blocked door."""
    pass


class Door:
    pass




if __name__ == "__main__":
    d = Door("1234", max_attempts=2, block_minutes=0.05)

    try:
        d.unlock("1111")
    except DoorBlockedError as e:
        print(f'{e.__class__.__name__}: {e}')

    try:
        d.change_code("0000", "9999")
    except DoorBlockedError as e:
        print(f'{e.__class__.__name__}: {e}')

    try:
        d.unlock("1234")
    except DoorBlockedError as e:
        print(f'{e.__class__.__name__}: {e}')

    time.sleep(5)

    try:
        d.unlock("1234")
    except DoorBlockedError as e:
        print(f'{e.__class__.__name__}: {e}')


# Access denied.
# Access denied. Code not changed.
# Too many failed attempts.
# DoorBlockedError: Door is blocked. Try again in 0 min 2 sec.
# Access granted.