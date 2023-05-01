import subprocess
from argparse import ArgumentParser, Namespace

parser = ArgumentParser()

parser.add_argument('interface', help="name of the interface to perform the operations", type=str)
parser.add_argument('-e', '--enable', help="enable monitor mode", action='store_true')
parser.add_argument('-d', '--disable', help="disable monitor mode", action='store_true')


args: Namespace = parser.parse_args()

interface = args.interface


def enable():
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["iwconfig", interface, "mode", "monitor"])
    subprocess.run(["ifconfig", interface, "up"])


def disable():
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["iwconfig", interface, "mode", "managed"])
    subprocess.run(["ifconfig", interface, "up"])
    subprocess.run("service NetworkManager start", shell=True)



if args.enable:
    enable()
elif args.disable:
    disable()