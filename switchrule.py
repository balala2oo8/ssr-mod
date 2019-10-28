from configloader import get_config


def getKeys():
    key_list = ["method", "port", "u", "d", "transfer_enable", "passwd", "enable"]
    if get_config().API_INTERFACE == "sspanelv3":
        key_list += ["id"]
    elif get_config().API_INTERFACE == "sspanelv3ssr":
        key_list += ["id", "obfs", "protocol"]
    elif get_config().API_INTERFACE == "glzjinmod":
        key_list += [
            "accountId id"
            "obfs",
            "obfs_param",
            "protocol",
            "protocol_param",
            "node_speedlimit",
            "forbidden_ip",
            "forbidden_port",
            "disconnect_ip",
            "is_multi_user",
        ]
    return key_list
    # return key_list + ['plan'] # append the column name 'plan'


def isTurnOn(row):
    return True
    # return row['plan'] == 'B' # then judge here
