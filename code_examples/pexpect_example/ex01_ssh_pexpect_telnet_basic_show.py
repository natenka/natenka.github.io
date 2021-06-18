from pprint import pprint
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


if __name__ == "__main__":
    main_login = {
        "username": "cisco",
        "password": "cisco",
        "enable_pass": "cisco"
    }
    secondary_login = {
        "username": "cisco",
        "password": "cisco",
        "enable_pass": None
    }
    with open("ip_list.txt") as f:
        ip_list = f.read().strip().split("\n")
        for ip in ip_list:
            try:
                out = send_show_command(ip, **main_login, command="sh ip int br")
                pprint(out, width=120)
            except pexpect.exceptions.TIMEOUT as error:
                try:
                    out = send_show_command(ip, **secondary_login, command="sh ip int br")
                    pprint(out, width=120)
                except pexpect.exceptions.TIMEOUT as error:
                    print("Два варианта логина не сработали")
