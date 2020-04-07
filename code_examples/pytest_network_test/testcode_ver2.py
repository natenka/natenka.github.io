import yaml
from netmiko import ConnectHandler
import pytest
import pytest_check as check


with open("devices.yaml") as f:
    devices = yaml.safe_load(f)


@pytest.fixture(scope="module")
def routers_from_devices_yaml():
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
        options = {"timeout": 5, "fast_cli": True}
        for device in devices:
            device.update(options)
    return devices


@pytest.fixture(scope="module")
def routers_test_connection(routers_from_devices_yaml):
    connections = {}
    for params in routers_from_devices_yaml:
        ssh = ConnectHandler(**params)
        ssh.enable()
        connections[params["host"]] = ssh
    yield connections
    for r in connections.values():
        r.disconnect()


device_route_map = {
    "192.168.100.1": ["1.1.1.1", "2.2.2.1", "4.4.4.4"],
    "192.168.100.2": ["1.1.1.1"],
}


@pytest.mark.parametrize(
    "device, route",
    [
        (device, route)
        for device, routes in device_route_map.items()
        for route in routes
    ],
)
def test_ssh(routers_test_connection, device, route):
    ssh = routers_test_connection[device]
    result = ssh.send_command("sh ip route")
    assert route in result
