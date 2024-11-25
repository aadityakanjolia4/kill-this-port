import subprocess
import re
import sys


def find_kill_pid(port):
    result = subprocess.run(["lsof", f"-i:{port}"], capture_output=True, text=True)
    output = result.stdout
    split_string = output.split("\n")
    updated_data = [re.sub(r"\s+", " ", line).strip() for line in split_string]
    new_data = updated_data[1:]
    pid_list = []
    for line in new_data:
        arr = line.split(" ")
        if len(arr) > 1:
            pid_list.append(arr[1])

    for pid in pid_list:
        try:
            subprocess.run(["kill", pid], capture_output=True, text=True, check=True)
            print(f"Successfully killed process with PID: {pid}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to kill process with PID: {pid}. Error: {e}")

    return


def force_kill_pid(port):
    result = subprocess.run(["lsof", f"-i:{port}"], capture_output=True, text=True)
    output = result.stdout
    split_string = output.split("\n")
    updated_data = [re.sub(r"\s+", " ", line).strip() for line in split_string]
    new_data = updated_data[1:]
    pid_list = []
    for line in new_data:
        arr = line.split(" ")
        if len(arr) > 1:
            pid_list.append(arr[1])

    for pid in pid_list:
        try:
            subprocess.run(
                ["kill", "-9", pid], capture_output=True, text=True, check=True
            )
            print(f"Successfully killed process with PID: {pid}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to kill process with PID: {pid}. Error: {e}")

    return

def check_port(port):
    result = subprocess.run(["lsof", f"-i:{port}"], capture_output=True, text=True)
    output = result.stdout
    print(output)
    return

def check_main():
    if len(sys.argv) == 2:
        port = sys.argv[1]
        if port.isdigit():
            check_port(port)
        else:
            print("Not a valid port.")
    return        

def main():
    if len(sys.argv) == 2:
        port = sys.argv[1]
        if port.isdigit():
            find_kill_pid(port)
        else:
            print("Not a valid port.")

    elif len(sys.argv) == 3:
        port = sys.argv[2]
        if sys.argv[1] == "--f" or sys.argv[1] == "--force":
            if port.isdigit():
                force_kill_pid(port)

            else:
                print("Not a valid port.")
        else:
            print("Not a valid command; Usage: kill-port --f [port]")

    else:
        print("Invalid command")

    # port = sys.argv[1].lstrip("-")
    # if not port.isdigit():
    #     print("Please provide a valid port number.")
    return


if __name__ == "__main__":
    main()
