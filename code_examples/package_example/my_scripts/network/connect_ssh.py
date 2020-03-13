from netmiko import ConnectHandler
from my_scripts import log


def send_show_command(device, command):
    log.debug("Подключаюсь к output['host']")
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result


def send_config_commands(device, config_commands):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_set(config_commands)
    return result

