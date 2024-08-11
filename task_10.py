import re
import socket

# решение с библиотекой re (с ошибкой Т_Т)
# def check_ip(ip_address):
#     match = re.match(r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$', ip_address)
#     if not match:
#         return False
#     spisok = match.groups()
#     for i in spisok:
#         if not spisok or (0 <= int(i) <= 255):
#             return False
#     return True


# решение с использованием socket.inet_aton
def check_ip2(ip_address):
    if not isinstance(ip_address, str):
        return False
    try:
        socket.inet_aton(ip_address)
        return True
    except socket.error:
        return False


assert check_ip2('') is False
assert check_ip2('192.168.0.1') is True
assert check_ip2('0.0.0.1') is True
assert check_ip2('10.100.500.32') is False
assert check_ip2(700) is False
assert check_ip2('127.0.1') is True



# assert check_ip('') is False
# assert check_ip('192.168.0.1') is True
# assert check_ip('0.0.0.1') is True
# assert check_ip('10.100.500.32') is False
# assert check_ip(700) is False
# assert check_ip('127.0.1') is True

