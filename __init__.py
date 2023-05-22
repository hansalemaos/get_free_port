import re
import subprocess

startupinfo = subprocess.STARTUPINFO()
creationflags = 0 | subprocess.CREATE_NO_WINDOW
startupinfo.wShowWindow = subprocess.SW_HIDE
invisibledict = {
    "startupinfo": startupinfo,
    "creationflags": creationflags,
}
dynp = set(range(49152, 65535))
regp = set(range(1025, 49151))


def get_all_used_ports():
    fp = subprocess.run(
        [
            "netstat",
            "-n",
        ],
        **invisibledict,
        capture_output=True
    )
    return set(
        [
            int(x)
            for x in list(set(re.findall(rb"\b\d+\.\d+.\d+.\d+:(\d+)\b", fp.stdout)))
        ]
    )


def get_dynamic_ports(qty=1):
    usedports = get_all_used_ports()
    return list(dynp - usedports)[:qty]


def get_registered_ports(qty=1):
    usedports = get_all_used_ports()
    return list(regp - usedports)[:qty]
