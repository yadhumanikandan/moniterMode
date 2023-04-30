import subprocess


def enable():
    subprocess.run("ifconfig wlan0 down", shell=True)
    subprocess.run("ifconfig wlan0 mode monitor", shell=True)
    subprocess.run("ifconfig wlan0 up", shell=True)


def disable():
    subprocess.run("ifconfig wlan0 down", shell=True)
    subprocess.run("iwconfig wlan0 mode managed", shell=True)
    subprocess.run("ifconfig wlan0 up", shell=True)
    subprocess.run("service NetworkManager start", shell=True)



enable()