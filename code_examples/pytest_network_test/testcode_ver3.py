import yaml
from netmiko import ConnectHandler
import pytest
import pytest_check as check


with open("devices.yaml") as f:
    devices = yaml.safe_load(f)


device_route_map = {
    "192.168.100.1": ["1.1.1.1", "2.2.2.1", "4.4.4.4"],
    "192.168.100.2": ["1.1.1.1"],
}


@pytest.fixture(scope="module")
def routers_connection():
    routers = device_route_map.keys()
    params = {
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
        "device_type": "cisco_ios",
        "fast_cli": True,
    }
    connections = {}
    for ip in routers:
        params["host"] = ip
        ssh = ConnectHandler(**params)
        ssh.enable()
        connections[ip] = ssh
    yield connections
    for r in connections.values():
        r.disconnect()


@pytest.mark.parametrize(
    "device, route",
    [
        (device, route)
        for device, routes in device_route_map.items()
        for route in routes
    ],
)
def test_ssh(routers_connection, device, route):
    ssh = routers_connection[device]
    result = ssh.send_command("sh ip route")
    assert route in result
