import logging

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


from my_scripts.network.connect_ssh import send_show_command, send_config_commands
from my_scripts.general.parse_data import (
    parse_data_textfsm,
    send_command_and_parse_data,
)
