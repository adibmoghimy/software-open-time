import time
import psutil
import datetime

program_name = "Telegram.exe"


def softWare_open_time():
    was_open = False
    while True:
        is_open = check_process_is_running(program_name)
        if is_open and not was_open:
            opening_time = datetime.datetime.now()
            was_open = True
            print("Program opened at:", opening_time)
        elif was_open and not is_open:
            closing_time = datetime.datetime.now()
            was_open = False
            print("Program closed at:", closing_time)

        time.sleep(1)


def get_run_processes_list():
    name_proc_list = []
    for proc in psutil.process_iter(['name']):
        name_proc_list.append(proc.info['name'])
    return name_proc_list


def check_process_is_running(proc_name):
    name_proc_list = get_run_processes_list()
    return proc_name in name_proc_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    softWare_open_time()
