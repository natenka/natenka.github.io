from pprint import pprint
from getpass import getpass

import pexpect


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


def collect_network_info(logins, ip_list, show_command):
    cmd_output = {}
    done = []
    for ip in ip_list:
        for login_dict in logins:
            try:
                out = send_show_command(ip, **login_dict, command=show_command)
                pprint(out, width=120)
                cmd_output[ip] = out
                done.append(ip)
                break
            except pexpect.exceptions.TIMEOUT as error:
                print(f"Не получилось подключиться к {ip}")
        if ip not in done:
            print(
                f"Никакие варианты логина не сработали {ip}.\n"
                f"Попробуйте ввести нужный логин/пароль руками:"
            )
            username = input("Username: ")
            password = getpass("Password: ")
            enable_password = getpass("Enable password: ")
            try:
                out = send_show_command(
                    ip, username, password, enable_password, command=show_command
                )
                pprint(out, width=120)
                done.append(ip)
                cmd_output[ip] = out
            except pexpect.exceptions.TIMEOUT as error:
                print("Не получилось подключиться")
    if len(done) == len(ip_list):
        print("Получен вывод со всех устройств")
    else:
        print(
            "Не удалось подключиться на такие устройства",
            sorted(set(ip_list) - set(done)),
        )

    return cmd_output


if __name__ == "__main__":
    login = {"username": "cisco", "password": "cisco", "enable_pass": "cisco"}
    login_2 = {"username": "cisco", "password": "cisco", "enable_pass": None}
    login_3 = {"username": "cisco", "password": "cisco", "enable_pass": "cisco"}
    logins = [login, login_2, login_3]

    with open("ip_list.txt") as f:
        ip_list = f.read().strip().split("\n")

    all_data = collect_network_info(logins, ip_list, show_command="sh ip int br")
    pprint(all_data, width=120)
