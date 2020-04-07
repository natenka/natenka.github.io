import yaml
from netmiko import ConnectHandler
import pytest
import pytest_check as check


with open("devices.yaml") as f:
    devices = yaml.safe_load(f)


def send_show_command(device, command):
    with ConnectHandler(**device) as ssh:
        output = ssh.send_command(command)
    return output


@pytest.mark.parametrize(
    "device, route",
    [
        *((devices[0], route) for route in ("1.1.1.1", "2.2.2.1", "4.4.4.4")),
        (devices[1], "1.1.1.1"),
    ],
)
def test_check_route(device, route):
    device.update({"fast_cli": True})
    command = "show ip route"
    output = send_show_command(device, command)
    assert (
        route in output
    ), f'Маршрут {route} отсутствует на устройстве {device["host"]}'
