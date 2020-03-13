import telnetlib
import time


def send_command_telnetlib(ipaddress, username, password, enable_pass, command):
    t = telnetlib.Telnet("192.168.100.1")

    t.read_until(b"Username:")
    t.write(username.encode("ascii") + b"\n")

    t.read_until(b"Password:")
    t.write(password.encode("ascii") + b"\n")
    t.write(b"enable\n")

    t.read_until(b"Password:")
    t.write(enable_pass.encode("ascii") + b"\n")

    t.read_until(b"#")
    t.write(b"terminal length 0\n")
    t.write(command + b"\n")

    time.sleep(1)

    result = t.read_until(b"#").decode("utf-8")
    return result


