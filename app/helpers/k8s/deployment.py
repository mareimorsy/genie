import requests, json
import subprocess
import os
from app.config import config
# from app.helpers.ansi2html import Ansi2HTMLConverter
# from app.helpers.ansi2html import Ansi2HTMLConverter
# export PYTHONWARNINGS="ignore:Unverified HTTPS request"
# requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def get_namespaces(config):
    r = requests.get(config['api_server'] + "/api/v1/namespaces", headers={"Authorization":"Bearer " + config["token"]}, verify=False)
    assert r.status_code == 200
    namespaces = []
    for i in r.json()["items"] :
        namespaces.append(i["metadata"]["name"])
    return namespaces

# result = get_namespaces(config)

# print(result)


def get_pods(config):
    r = requests.get(config['api_server'] + "/api/v1/pods", headers={"Authorization":"Bearer " + config["token"]}, verify=False)
    assert r.status_code == 200
    # return r
    pods = []
    for i in r.json()["items"] :
        pods.append({"n": i["metadata"]["name"], "ns": i["metadata"]["namespace"]})
    return pods

def exec(cmd):
    # return subprocess.run(cmd.split(), stdout=subprocess.PIPE).stdout.decode('utf-8').splitlines()
    return subprocess.run(cmd.split(), stdout=subprocess.PIPE).stdout.decode('utf-8')
    # conv = Ansi2HTMLConverter()
    # ansi = "".join(subprocess.run(cmd.split(), stdout=subprocess.PIPE).stdout.decode('utf-8').splitlines())
    # html = conv.convert(ansi)
    # return html
    # return ansi2html.Ansi2HTMLConverter.convert( subprocess.run(cmd.split(), stdout=subprocess.PIPE).stdout.decode('utf-8') )
    # return os.system(cmd)


# x = exec("echo \"This is \033[0;31m Hello \033[0m world\"")

# print(get_pods(config))

# def exec(cmd):
#     cmd_arr = cmd.split()
#     if len(cmd_arr) > 1:
#         return subprocess.run([cmd_arr[0], cmd_arr[1]], stdout=subprocess.PIPE).stdout.decode('utf-8')
#     else:
#         return subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode('utf-8')

def pod_cmd(pod_name, namespace, cmd):
    # return exec("echo \"This is \033[0;31m Hello \033[0m world\"")
    return exec(f"kubectl exec -it {pod_name} -n {namespace} -- {cmd}")

# x = pod_cmd("hub-ops-66d4f9cf89-z6fnn", "do", "./app ops pg-migrate hub")
# x = pod_cmd("hub-ops-66d4f9cf89-z6fnn", "do", "ls")

# print(x)