import subprocess


def enable():
    subprocess.run("ifconfig wlan0 down", shell=True)
    subprocess.run("ifconfig wlan0 mode monitor", shell=True)
    subprocess.run("ifconfig wlan0 up", shell=True)


def disable():
    subprocess.run("airmon-ng stop wlan0", shell=True)
    subprocess.run("ifconfig wlan0 up", shell=True)
    subprocess.run("service NetworkManager start", shell=True)



enable()