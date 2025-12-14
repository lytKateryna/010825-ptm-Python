""" 02. Данные через свойство

Доработайте класс SecureUSB:
- доработайте метод read(), а именно:
    - превратите метод read() в атрибуте data

Теперь доступ к содержимому осуществляется через обращение к usb.data,
а не вызовом метода read().

При попытке чтения в заблокированном состоянии должно по-прежнему выбрасываться PermissionError.
"""

class SecureUSB:
    pass





if __name__ == "__main__":
    usb = SecureUSB("Secret plans", "1234")

    usb.lock()  # Device is locked.
    usb.unlock("0000")  # Device is locked. Access denied.
    usb.unlock("1234")  # Access granted.
    print("Data:", usb.data)  # Data: Secret plans

# Device is locked.
# Device is locked. Access denied.
# Access granted.
# Data: Secret plans
