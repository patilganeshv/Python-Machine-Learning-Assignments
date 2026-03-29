"""
Add below features in our project named as Platform Surveillance
System.
1. Add Thread Monitoring Feature
    For each running process, display:
        .Process Name
        .PID
        .Number of Threads created by that process
    Requirement: Store information in log file along with timestamp.

2.Add Open Files Monitoring Feature
    For each process, display:
        .Number of files opened by the process
    Requirement:
        .Count open file descriptors using system/library calls
        .Handle permission errors properly
        .Mention "Access Denied" in log if required

3.Add Actual Memory Allocation Feature
    Display real memory usage of each process
        .RSS (Resident Set Size - actaul RAM used)
        .VMS (Virtual Memory)
        .Memory Percentage
    Requirement
        show:
            .Top 10 Memory consuming processes

4.Add Periodic Email Reporting Feature
    Automatically send system report through email at regular intervals.
    Email must contain:
        .Log file attachment
        .Summary of:
            .Total processes
            .Top CPU usage processes
            .Top Memory usage processes
            .Top Thread cound processes
            .Top Open file processes

Usage:
platformSurveillance.py "MarvellousLogs", "receiver@gmail.com" 10

Where:
    . MarvellousLogs --> log folder
    . receiver@gmail.com --> receiver mail
    . 10 --> interval in minutes

Expected Output in Log File
each process entry should include:
    .Process Name
    .PID
    .CPU %
    .Memory (RSS)
    .Threads Count
    .Open Files Count
    .Timestamp
"""

import psutil
import sys
import os
import time
import schedule
import socket

# import urllib2
import urllib.request
import urllib.error
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# def is_connected():
# 	try:
# 		urllib.request.urlopen('http://216.58.192.142', timeout=1)
# 		return True
# 	except urllib.error.URLError as err:
# 		return False


def is_connected():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False


def MailSender(filename, time, data):
    body_summary = ""

    total_processes = len(data)
    body_summary += f"Total Processes: {total_processes}\n\n"

    # Top CPU
    body_summary += "Top CPU Usage Processes:\n"
    top_cpu = sorted(data, key=lambda p: p['cpu_percent'], reverse=True)[:5]
    for p in top_cpu:
        body_summary += f"\t{p['name']} - {p['cpu_percent']}%\n"

    # Top Memory
    body_summary += "\nTop Memory Usage Processes:\n"
    top_mem = sorted(data, key=lambda p: p['memory_percent'], reverse=True)[:5]
    for p in top_mem:
        body_summary += f"\t{p['name']} - {p['memory_percent']:.2f}%\n"

    # Top Threads
    body_summary += "\nTop Thread Count Processes:\n"
    top_threads = sorted(data, key=lambda p: p['no_of_threads'], reverse=True)[:5]
    for p in top_threads:
        body_summary += f"\t{p['name']} - {p['no_of_threads']} threads\n"

    # Top Open Files
    body_summary += "\nTop Open File Processes:\n"
    top_open_files = sorted(data, key=lambda x: x['open_files'], reverse=True)[:5]
    for p in top_open_files:
        body_summary += f"\t{p['name']} - {p['open_files']} open files\n"
    
    try:
        fromaddr = "patilganeshv@gmail.com"
        toaddr = sys.argv[2]
        
        msg = MIMEMultipart()
        
        msg['From'] = fromaddr
        msg['To'] = toaddr
		
        body = f"""
		Hello {toaddr},
		Please find attached document which contain log of running process and below system process summary.
		log file is created at : {time}

        {body_summary}

		This is auto generated mail.

		Thanks & Regards,
		Ganesh Patil
		"""
        
        Subject = """Process log generated at : %s"""%(time)
        
        msg['Subject'] = Subject
        msg.attach(MIMEText(body,'plain'))
        
        attachment = open(filename ,"rb")
        
        p = MIMEBase('application','octet-stream') 
        p.set_payload((attachment).read())
        
        encoders.encode_base64(p)
        
        p.add_header('Content-Disposition',"attachment; filename %s" % filename)
        
        msg.attach(p)
        
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, "---------")        
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit()
        print("Log file successfully sent through mail.")
    
    except Exception as e:
        print("Unable to send mail.", e) 

def create_log(folder_name):
    border = "-" * 50
    ret = False

    ret = os.path.exists(folder_name)
    if ret:
        is_dir = os.path.isdir(folder_name)
        if not is_dir:
            print("Unable to create folder")
            sys.exit(1)        
    else:
        os.mkdir(folder_name)
        print("Directory for log file gets created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    file_name = os.path.join(folder_name, "Marvellous_%s.log" %timestamp)
    print("Log file gets created with name: ", file_name)

    fobj = open(file_name, "w")
    fobj.write(border+"\n")
    fobj.write("----- Marvellous Platform Surveillance System-----\n")
    fobj.write("Log Created at: "+time.ctime()+"\n")
    fobj.write(border+"\n\n")

    fobj.write("------------- System Report ----------------------\n")
    fobj.write("CPU Usage:%s %%\n" %psutil.cpu_percent())
    fobj.write(border+"\n\n")

    mem = psutil.virtual_memory()
    fobj.write("RAM Usage:%s %%\n" %mem.percent)
    fobj.write(border+"\n\n")

    fobj.write("Disk Usage Report\n")
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            fobj.write("%s --> %s %% used\n" %(part.mountpoint, usage.percent))
        except:
            pass
    
    fobj.write(border+"\n\n")
    net = psutil.net_io_counters()
    fobj.write("Network Usage Report\n")
    fobj.write("Sent: %.2f MB\n" %(net.bytes_sent / (1024 * 1024)))
    fobj.write("Received: %.2f MB\n" %(net.bytes_recv / (1024 * 1024)))
    fobj.write(border+"\n\n")
    
    # Process Log
    data = process_scan()

    for info in data:
        fobj.write("Process Name: %s\n" %info.get("name"))
        fobj.write("PID: %s\n" %info.get("pid"))
        fobj.write("CPU %%: %.2f\n" %info.get("cpu_percent"))
        fobj.write("Memory %%: %.2f\n" %info.get("memory_percent"))
        fobj.write(f"Memory (RSS) : {info.get("rss")} \n")
        fobj.write(f"VMS (Virtual Memory Size) : {info.get("vms") / (1024 * 1024):.2f} MB\n")
        fobj.write(f"Thread Count : {info.get("no_of_threads")} \n")
        fobj.write(f"Open File Count : {info.get("open_files")} \n")
        fobj.write("User Name: %s\n" %info.get("username"))
        fobj.write("Status: %s\n" %info.get("status"))
        fobj.write("Start Time: %s\n" %info.get("create_time"))
        fobj.write(border+"\n")

    # Sort by RSS (Actual RAM usage)
    processes = sorted(data, key=lambda x: x['rss'], reverse=True)
    
    # Show Top 10
    fobj.write("\nTop 10 Memory Consuming Processes:\n")
    for proc in processes[:10]:
        fobj.write(f"PID: {proc['pid']} \n")
        fobj.write(f"Name: {proc['name']} \n")
        fobj.write(f"RSS: {proc['rss'] / (1024 * 1024):.2f} MB \n")
        fobj.write(f"VMS: {proc['vms'] / (1024 * 1024):.2f} MB \n")
        fobj.write(f"Memory %: {proc['memory_percent']:.2f}% \n")
        fobj.write(border+"\n")

    
    connected = is_connected()
    if connected:
        MailSender(file_name, time.ctime(), data)
    else:
        print("There is no internet connection")

    fobj.write(border+"\n")
    fobj.write("------------------ End of Log File ---------------\n")
    fobj.write(border+"\n")



def process_scan():
    list_process = []

    # Warm up for CPU percent
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass
    
    time.sleep(0.2)
    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid", "name", "username", "status", "create_time"])
            try:
                # Convert create_time
                info["create_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(info["create_time"]))
            except:
                info["create_time"] = "NA"
            
            info["no_of_threads"] = proc.num_threads()
            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()
            info["rss"] = (proc.memory_info()).rss
            info["vms"] = (proc.memory_info()).vms
            info["open_files"] = len(proc.open_files())

            list_process.append(info)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return list_process

def main():
    border = "-" * 50
    print(border)
    print("----- Marvellous Platform Surveillance System-----")
    print(border)

    if len(sys.argv) == 2:
        if (sys.argv[1] == "--H" or sys.argv[1] == "--h"):
            print("This script is use to")
            print("1: Create automatic logs")
            print("2: Executes priodically")
            print("3: Sends mail with the log")
            print("4: Store information about process")
            print("5: Store information about CPU")
            print("6: Store information about RAM Usage")
            print("7: Store information about Secondary storage")
        
        elif (sys.argv[1] == "--U" or sys.argv[1] == "--u"):
            print("Use the automation script as")
            print("Scriptname.py directoryname receiver-email timeinterval")
            print("Directory Name: Name of directory to create automatic logs")
            print("Receiver Email: The receiver email address")
            print("Time Interval: The time in minutes for periodic scheduling")
            
        else:
            print("Unable to procced as there is no such option")
            print("Please use --h or --u to get more details")
    
    # python scriptname.py marvellouslog patilganeshv@gmail.com 5
    elif len(sys.argv) == 4:
        print("Directory Name: ", sys.argv[1])
        print("Receiver Email: ", sys.argv[2])
        print("Time Interval: ", sys.argv[3])

        # Apply the schedular
        schedule.every(int(sys.argv[3])).minutes.do(create_log, sys.argv[1])

        print("Platform Surveillance System Started Successfully")
        print("Directory Created with name: ", sys.argv[1])
        print("Receiver's Email Address: ", sys.argv[2])
        print("Time Interval in Minutes: ", sys.argv[3])
        print("Press Ctrl + C to Stop the execution")
        # Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)
    
    else:
        print("Invalid number of command line arguments")
        print("Unable to procced as there is no such option")
        print("Please use --h or --u to get more details")

    print(border)
    print("---------- Thank you for using our script --------")
    print(border)

if __name__ == "__main__":
    main()