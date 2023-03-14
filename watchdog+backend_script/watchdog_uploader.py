#!/home/arcgis/miniconda3/bin/python

import arcpy
import datetime
import sys
import time
import logging
# import yaml
import os
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler
from watchdog.observers.polling import PollingObserver
# from logAttachment_SPH import create_logAttachment #(ORIGINAL)

# monitor_folder = r'/datastore/Temp_Folder/SPH' #(ORIGINAL)
monitor_folder = r'C:\Users\jrsitompul\OneDrive - ESRI Indonesia\WORK_DATA_JOJO\PROJECT\2020-2022\PARAMOUNT_LAND\folder_sertifikat'

# class logProcess():
#     def logging_process_info(message):
#         time_obj = datetime.datetime.today()
#         time_str = datetime.datetime.strftime(time_obj, "%d-%m-%Y %H:%M")
#         concate_msg = "{} {}".format(time_str, message)
#         create_logAttachment.loginfo(concate_msg)
#         arcpy.AddMessage(concate_msg)

#     def logging_process_error(message):
#         create_logAttachment.logerror(message)
#         arcpy.AddMessage(message)
        
#     def logging_process_warning(message):
#         time_obj = datetime.datetime.today()
#         time_str = datetime.datetime.strftime(time_obj, "%d-%m-%Y %H:%M")
#         concate_msg = "{} {}".format(time_str, message)
#         create_logAttachment.logwarning(concate_msg)
#         arcpy.AddMessage(concate_msg)

class ExampleHandler(FileSystemEventHandler):
    def on_created(self, event): # when file is created
        fullstring =  event.src_path
        substring = '.pdf'
        # logProcess.logging_process_info("Current file: {}".format(fullstring)) #(ORIGINAL)
        print("Current file: {}".format(fullstring))
        namafile = os.path.basename(fullstring)
        
        if substring in os.path.basename(namafile):
            print('process data')
            try :
                python_path = r'C:\Users\jrsitompul\AppData\Local\Continuum\miniconda3\envs\arcgispro_ver3.0-py3-clone\python.exe' #r'/home/arcgis/miniconda3/bin/python'
                script_arcgis = r'D:\PROJECT\2020-2022\PARAMOUNT_LAND\backend_upload_file_paramount_dev_v2.py' #r'/home/arcgis/monitor_folder_SPH/update_attachment_SPH.py'
                arguments = ('%s %s'%(python_path, script_arcgis))
                os.system(arguments)
                print('Now processing data {}'.format(fullstring))
                print('Complete, waiting for next data')
            
            except Exception as e:
                print(e)
                sys.exit(1)

        else:
            print ('it is not the exact data')
            pass
        
        # os.remove(fullstring)
        
logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
# path = monitor_folder #(ORIGINAL)
path = sys.argv[1] if len(sys.argv) > 1 else '.'
observer = PollingObserver() #Observer()
event_handler = ExampleHandler() # create event handler (ORIGINAL)
# event_handler = LoggingEventHandler() # create event handler

# set observer to use created handler in 
print ('Start monitoring folder ...')
observer.schedule(event_handler, path, recursive=True)
observer.start()

# sleep until keyboard interrupt, then stop + rejoin the observer
try:
    while True:
        # time.sleep(0.00000001) #(ORIGINAL)
        time.sleep(5)
except KeyboardInterrupt:
    print ('Shutting down monitoring folder system')
    observer.stop()
observer.join()
