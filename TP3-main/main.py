import schedule
import time
import subprocess
import psutil

def start_einsamerigel_stream():
    subprocess.run(['python', 'start_stream_einsamerigel.py'])

def start_cozylofi_stream():
    subprocess.run(['python', 'start_stream_cozylofi.py'])

def start_einsamerigel_docker():
    subprocess.run(['python', '/Twitch_Project-einsamerigel/script.py'])

def start_cozylofi_docker():
    subprocess.run(['python', '/Twitch_Project-cozylofi/script.py'])

def terminate_script_by_name(script_name):
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        if script_name in proc.info['cmdline']:
            print(f"Terminating {proc.info['name']} (PID: {proc.info['pid']})")
            proc.terminate()  # or proc.kill() for immediate termination

# Schedule the tasks
schedule.every().day.at("01:00").do(start_cozylofi_stream)
schedule.every().day.at("01:00").do(start_cozylofi_docker)

schedule.every().day.at("09:00").do(terminate_script_by_name, 'start_stream_cozylofi.py')
schedule.every().day.at("09:00").do(terminate_script_by_name, '/Twitch_Project-cozylofi/script.py')
schedule.every().day.at("09:00").do(start_einsamerigel_stream)
schedule.every().day.at("09:00").do(start_einsamerigel_docker)

schedule.every().day.at("17:00").do(terminate_script_by_name, 'start_stream_einsamerigel.py')
schedule.every().day.at("17:00").do(terminate_script_by_name, '/Twitch_Project-einsamerigel/script.py')

# Run the schedule
while True:
    schedule.run_pending()
    time.sleep(1)
