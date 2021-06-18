from pprint import pprint
import pexpect
from getpass import getpass


def send_show_command(host, username, password, enable_pass, command, prompt="#"):
    print(f"Connecting to {host}")
    with pexpect.spawn(f"telnet {host}", encoding="utf-8", timeout=5) as telnet:
        telnet.expect("[Uu]sername")
        telnet.sendline(username)
        telnet.expect("[Pp]assword")
        telnet.sendline(password)
        telnet.expect(">")
        if enable_pass:
            telnet.sendline("enable")
            telnet.expect("Password")
            telnet.sendline(enable_pass)
            telnet.expect("#")
        else:
            prompt = ">"

        telnet.sendline("terminal length 0")
        telnet.expect(prompt)

        telnet.sendline(command)
        telnet.expect(prompt)
        output = telnet.before
    return output.replace("\r\n", "\n")


if __name__ == "__main__":
    login = {
        "username": "cisco",
        "password": "ciscod",
        "enable_pass": "cisco"
    }
    login_2 = {
        "username": "cisco",
        "password": "cisco2",
        "enable_pass": None
    }
    login_3 = {
        "username": "cisco",
        "password": "cisco2",
        "enable_pass": "cisco"
    }
    logins = [login, login_2, login_3]
    done = []

    with open("ip_list.txt") as f:
        ip_list = f.read().strip().split("\n")
        for ip in ip_list:
            for login_dict in logins:
                try:
                    out = send_show_command(ip, **login_dict, command="sh ip int br")
                    pprint(out, width=120)
                    done.append(ip)
                    break
                except pexpect.exceptions.TIMEOUT as error:
                    print("Не получилось подключиться")
            if ip not in done:
                print("Никакие варианты логина не сработали.\nПопробуйте ввести нужный логин/пароль руками:")
                username = input("Username: ")
                password = getpass("Password: ")
                enable_password = getpass("Enable password: ")
                try:
                    out = send_show_command(ip, username, password, enable_password, command="sh ip int br")
                    pprint(out, width=120)
                except pexpect.exceptions.TIMEOUT as error:
                    print("Не получилось подключиться")
