import time
from datetime import datetime as d

#hosts_path = r"C:\WINDOWS\System32\drivers\etc\hosts"
hosts_path = r"hosts.txt"
home_ip = "127.0.0.1"
websites = ["www.facebook.com", "www.youtube.com", "www.google.com"]
websites_hosts = [home_ip + " " + w + "\n" for w in websites]

while True:
    if (d(d.now().year, d.now().month, d.now().day, 8)) < d.now() < \
            (d(d.now().year, d.now().month, d.now().day, 20)):
        with open(hosts_path, "r+") as f:
            content = f.read()
            if websites[0] in content:
                pass
            else:
                f.writelines(websites_hosts)
    else:
        with open(hosts_path, "r+") as f:
            content = f.readlines()
            cont = "".join(content)
            if websites[0] in cont:
                content = content[:(len(content) - len(websites_hosts))]
                f.seek(0)
                f.writelines(content)
                f.truncate()
            else:
                pass
    print("OK")
    time.sleep(10)

