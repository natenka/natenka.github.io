import textfsm
#from my_scripts.network.connect_ssh import send_show_command
from my_scripts import send_show_command


def parse_data_textfsm(output, template):
    with open(template) as f:
        re_table = textfsm.TextFSM(f)
        header = re_table.header
        result = re_table.ParseText(output)
        results = [dict(zip(header, row)) for row in result]
    return results


def send_command_and_parse_data(device, command, template):
    output = send_show_command(device, command)
    return parse_data_textfsm(output, template)


