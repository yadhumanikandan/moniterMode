import subprocess
from argparse import ArgumentParser, Namespace

parser = ArgumentParser()

parser.add_argument('interface', help="name of the interface to perform the operations", type=str)
parser.add_argument('-e', '--enable', help="enable monitor mode", action='store_true')
parser.add_argument('-d', '--disable', help="disable monitor mode", action='store_true')
parser.add_argument('-a', '--attack', help="make use of aircrack-ng for furthur operations in handshack capturing", action='store_true')


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
    print("Monitor mode ENABLED !!!!")
elif args.disable:
    disable()
    print("Monitor mode DISABLED !!!!")


# extending capablities to make use of aircrack-ng

tools = 0

def attacks():
    if tool == 1:
        print("starting airodump-ng.....")
        subprocess.run(["airodump-ng", interface])


if args.attack:
    print(f"1 > airodump-ng")
    tool = input("select an attack: ")


attacks()