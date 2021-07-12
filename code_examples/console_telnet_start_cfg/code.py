import time

from netmiko import ConnectHandler, redispatch


def device_startup_config():
    console_params = {
        'device_type': 'generic_termserver_telnet',
        'ip': "127.0.0.1",
        'port': '60104'
    }
    with ConnectHandler(**console_params) as console:
        output = console.read_until_pattern("yes|>")
        print("Found yes/no")
        if "yes" in output:
            console.write_channel('no\n')
            time.sleep(1)
        console.write_channel('\r\n')
        console.read_until_pattern("Press RETURN to get started")
        print("Loading finished")
        console.write_channel('\r\n')
        time.sleep(1)
        console.write_channel('show clock\n')
        output = console.read_until_pattern(">")

        print(output)
        redispatch(console, device_type='cisco_ios')
        output = console.send_command("show clock")
        print("REDISPATCH SUCCESS", output)
        console.enable()
        print(console.send_config_set(["hostname R55", "logging 101.1.1.1"]))


if __name__ == "__main__":
    device_startup_config()
