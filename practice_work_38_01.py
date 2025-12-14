""" 01 Безопасная флешка

Создайте класс SecureUSB, представляющий защищённую флешку.
При создании объекта передаётся:
- секретное содержимое
- и пароль

Продумайте, какие атрибуты следует скрыть, а какие оставить доступными.

Методы класса SecureUSB:
- unlock(password):
    - если пароль верный:
        - разблокирует флешку,
        - печатает: "Access granted.",
        - возвращает True,
    - иначе:
        - печатает "Access denied.",
        - возвращает False.
- lock():
    - блокирует устройство
- read():
    - если устройство разблокировано:
        - возвращает хранящиеся на флешке данные,
    - иначе:
        - выбрасывает исключение PermissionError: "Access denied: device is locked."

"""

class SecureUSB:
    pass


if __name__ == "__main__":
    usb = SecureUSB("Secret plans", "1234")

    usb.lock()
    usb.unlock("0000")
    usb.unlock("1234")
    print("Data:", usb.read())

# Device is locked.
# Access denied.
# Access granted.
# Data: Secret plans
