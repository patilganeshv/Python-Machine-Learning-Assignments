import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile
import smtplib
from email.message import EmailMessage

def send_email(zip_file, log_file):
    sender = "patilganeshv@gmail.com"
    password = "app_password"
    receiver = "receiver_email@gmail.com"

    msg = EmailMessage()
    msg["Subject"] = "Backup Completed Successfully"
    msg["From"] = sender
    msg["To"] = receiver

    msg.set_content("Backup completed successfully.\nLog and Zip files are attached.")

    # Attach ZIP file
    with open(zip_file, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="zip",
            filename=os.path.basename(zip_file)
        )

    # Attach LOG file
    with open(log_file, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="text",
            subtype="plain",
            filename=os.path.basename(log_file)
        )

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)

        print("Email sent successfully")

    except Exception as e:
        print("Unable to send email:", e)

def restore_backup(zip_file, destination):
    if not os.path.exists(zip_file):
        print("Zip file does not exist")
        sys.exit(1)

    if not os.path.exists(destination):
        os.makedirs(destination)

    with zipfile.ZipFile(zip_file, 'r') as zobj:
        zobj.extractall(destination)

    print("Backup restored successfully to:", destination)

def update_history(zip_file, num_files):

    history_file = "backup_history.txt"

    date = time.strftime("%Y-%m-%d %H:%M:%S")

    size = os.path.getsize(zip_file) / (1024 * 1024)
    size = round(size, 2)

    line = f"{date} | {num_files} | {size} MB | {zip_file}\n"

    with open(history_file, "a") as f:
        f.write(line)

def show_history():
    history_file = "backup_history.txt"

    if not os.path.exists(history_file):
        print("No backup history found.")
        return

    print("Backup History")
    print("-" * 50)

    with open(history_file, "r") as f:
        for line in f:
            date, files, size, name = line.strip().split("|")
            print(f"Date          : {date}")
            print(f"Total Files   : {files}")
            print(f"Size          : {size}")
            print(f"Zip File Name : {name}")
            print("-" * 50)

def make_zip(dir_name):
    os.makedirs("BackupZipFiles", exist_ok=True)
    time_stamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = os.path.join("BackupZipFiles", dir_name + "_" + time_stamp + ".zip")

    print("Creating ZIP archive...")

    # open the zip file
    zobj = zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(dir_name):
        for file in files:
            full_path = os.path.join(root, file)
            relative = os.path.relpath(full_path, dir_name)

            zobj.write(full_path, relative)

    zobj.close()
    print(f"ZIP created: {zip_name}")
    return zip_name

def calculate_hash(file_path):
    hobj = hashlib.md5()
    fobj = open(file_path, "rb")

    while True:
        data = fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)
    
    fobj.close()
    return hobj.hexdigest()

def backup_files(source, destination, exclude_ext):
    copied_files = []

    # Creating the Backup folder for backup process
        # exist_ok means If destination folder is already exists then go ahed without exception.
        # makedir() --> create folder only current folder
        # makedirs() --> create nested folder also
    os.makedirs(destination, exist_ok=True)

    print("Starting backup...")

    for root, dirs, files in os.walk(source):
        for file in files:
            # Skip excluded extensions
            if exclude_ext and any(file.endswith(ext) for ext in exclude_ext):
                continue
            
            # Instead of checking extension with endswith(), we can use:
            # ext = os.path.splitext(file)[1]
            # if ext in exclude_ext:
            #     continue

            src_path = os.path.join(root, file)
            relative = os.path.relpath(src_path, source)
            dest_path = os.path.join(destination, relative)

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            
            if ((not os.path.exists(dest_path)) or (calculate_hash(src_path) != calculate_hash(dest_path))):
                # copy the files if it's new/updated
                # copy2() --> copy the file with all metadata
                shutil.copy2(src_path, dest_path)
                copied_files.append(relative)
                # print(f"Copied: {relative}")
    
    print(f"Backup completed. {len(copied_files)} file(s) copied.")
    return copied_files

def data_shield_start(source, exclude_ext):
    if os.path.exists(source):
        if not os.path.isdir(source):
            print(f"'{source}' is not directory")
            sys.exit(1)
    else:
        print(f"Source directory '{source}' does not exist")
        sys.exit(1)

    # Log files folder name
    folder_name = "Log"   
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
    log_file = os.path.join(folder_name, "DataShield_%s.log" %timestamp)
    print("Log file gets created with name: ", log_file)

    # fobj = open(file_name, "w")
    with open(log_file, "w") as fobj:
        border = "-" * 50 
        fobj.write(border+"\n")
        fobj.write("--------------- Data Shield System ---------------\n")
        fobj.write(border+"\n")

        fobj.write("Backup Process Started Successfully at :"+time.ctime()+"\n")
        # fobj.write(border+"\n")

        backup_folder = "TempBackup"
        files = backup_files(source, backup_folder, exclude_ext)

        zip_file = make_zip(backup_folder)
        
        fobj.write(f"Files copied: {len(files)} \n")

        fobj.write(f"Zip file gets created: {zip_file} \n")
        fobj.write(border+"\n")

        update_history(zip_file, len(files))
        
        fobj.write(border+"\n")
        fobj.write("------------------ End of Log File ---------------\n")
        fobj.write(border+"\n")

    send_email(zip_file, log_file)
    print("Backup process finished\n")

def print_usage():
    print("\n Usage Examples: ")
    print("--------------------------------------------------")
    print("1. Start Backup Scheduler in every 5 minutes")
    print("   python Script.py <minutes> <source_directory>")
    print("   Example: python Script.py 5 Data")

    print("\n2. Start Backup Scheduler excluding files")
    print("   python Script.py <minutes> <source_directory> <file_extension>")
    print("   Example: python Script.py 5 Data .tmp .log")

    print("\n3. Restore Backup")
    print("   python Script.py --restore <zipfile> <destination>")
    print("   Example: python Script.py --restore backup.zip Restore")

    print("\n4. View Backup History")
    print("   python Script.py --history")

    print("\n5. Help")
    print("   python Script.py --help")


def main():
    border = "-" * 50
    print(border)
    print("-------------- Data Shield System ----------------")
    print(border)

    # Backup History
    # python Script.py --history
    if len(sys.argv) == 2 and sys.argv[1] == "--history":
        show_history()
        return

    elif len(sys.argv) == 2:
        if sys.argv[1] in ("--H", "--h", "--help"):
                print("This automation script performs:")
                print("1. Automatic backup of directory at given time")
                print("2. Copies/Backup only new or modified files")
                print("3. Creates ZIP archive of backup periodically")
                print("4. Restores data from backup ZIP")
                print("5. Maintains backup history")
                print("6. Supports scheduled backup")
        
        elif sys.argv[1] in ("--U", "--u"):
            print_usage()
            
        else:
            print("Unable to procced as there is no such option")
            print("Please use --h or --u to get more details")
    
    # Restore Command
    # python Script.py --restore TempBackup_2026-03-06_10-20-10.zip RestoredData
    elif len(sys.argv) == 4 and sys.argv[1] == "--restore":
        zip_file = sys.argv[2]
        destination = sys.argv[3]
        restore_backup(zip_file, destination)
        return
    
    # python script.py 5 data
    elif len(sys.argv) >= 3:
        interval = sys.argv[1]
        source_dir = sys.argv[2]

        print("Time Interval in Minutes: ", interval)
        print("Source Directory: ", source_dir)
        
        exclude_ext = None
        
        # If user provides extra extensions
        if len(sys.argv) > 3:
            exclude_ext = sys.argv[3:]
            print("Excluded Extensions:", exclude_ext)
        
        # Apply the schedular
        schedule.every(int(interval)).minutes.do(data_shield_start, source_dir, exclude_ext)

        print(border)
        print("Data Shield System Started Successfully")
        print("Press Ctrl + C to Stop the Execution")
        print(border)

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