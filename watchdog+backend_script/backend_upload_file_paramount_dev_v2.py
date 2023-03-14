import arcpy
import csv
import datetime
import glob
import os, sys
import os.path
import pandas as pd
import shutil

output_gdb = r'C:\Users\jrsitompul\OneDrive - ESRI Indonesia\WORK_DATA_JOJO\PROJECT\2020-2022\PARAMOUNT_LAND\Test\Test_Paramount\Test_Paramount.gdb'
shared_folder = r'C:\Users\jrsitompul\OneDrive - ESRI Indonesia\WORK_DATA_JOJO\PROJECT\2020-2022\PARAMOUNT_LAND\folder_sertifikat'
int_matchTable_SPH = r"C:\Users\jrsitompul\OneDrive - ESRI Indonesia\WORK_DATA_JOJO\PROJECT\2020-2022\PARAMOUNT_LAND\Test\Test_Paramount\Test_Paramount.gdb\Intermediate_match_table_SPH"
int_matchTable_HGB = r"C:\Users\jrsitompul\OneDrive - ESRI Indonesia\WORK_DATA_JOJO\PROJECT\2020-2022\PARAMOUNT_LAND\Test\Test_Paramount\Test_Paramount.gdb\Intermediate_match_table_HGB"
input_param = r'C:\Users\jrsitompul\OneDrive - ESRI Indonesia\WORK_DATA_JOJO\PROJECT\2020-2022\PARAMOUNT_LAND\folder_sertifikat\input_parameter_fix.csv'

csv_read = pd.read_csv(input_param)

input_file = csv_read.iloc[0]['certificate']
cert_type = csv_read.iloc[0]['cert_type']
idcert = csv_read.iloc[0]['cert_id']

class logProcess():
    def logging_process_info(message):
        time_obj = datetime.datetime.today()
        time_str = datetime.datetime.strftime(time_obj, "%d-%m-%Y %H:%M")
        concate_msg = "{} {}".format(time_str, message)
        arcpy.AddMessage(concate_msg)

    def logging_process_error(message):
        arcpy.AddMessage(message)
        
    def logging_process_warning(message):
        time_obj = datetime.datetime.today()
        time_str = datetime.datetime.strftime(time_obj, "%d-%m-%Y %H:%M")
        concate_msg = "{} {}".format(time_str, message)
        arcpy.AddMessage(concate_msg)

class uploadFile():
    def update_data():
        name = input_file.split(sep='.')[0]
        matchTable = os.path.join(output_gdb, 'match_table')
        try:
            logProcess.logging_process_info('Creating match table...')
            # overwrite existing match table
            try:
                arcpy.Delete_management(matchTable)
                logProcess.logging_process_info('Overwriting match table...')
            except:
                pass

            # copy match table to egdb
            arcpy.conversion.TableToTable(input_param, output_gdb, "match_table", '', r'cert_id "cert_id" true true false 8000 Text 0 0,First,#,input_param,cert_id,0,8000;certificate "certificate" true true false 8000 Text 0 0,First,#,input_param,certificate,0,8000', '')

            # revalue field certificate
            if idcert != name:
                match_table_calc = arcpy.management.CalculateField(in_table=matchTable, field="certificate", expression=f"Revalue(!certificate!, '{cert_type}')", expression_type="PYTHON3", code_block="""def Revalue(certificate, cert_type):
                if cert_type == 'SPH':
                    x = \"https://app.paramount-land.com/gis/sph/\" + str(certificate)
                    return x
                else:
                    y = \"https://app.paramount-land.com/gis/hgb/\" + str(certificate)
                    return y""", field_type="TEXT", enforce_domains="NO_ENFORCE_DOMAINS")[0]
            else:
                match_table_calc = arcpy.management.CalculateField(in_table=matchTable, field="certificate", expression=f"Revalue(!cert_id!, '{cert_type}')", expression_type="PYTHON3", code_block="""def Revalue(cert_id, cert_type):
                if cert_type == 'SPH':
                    x = \"https://app.paramount-land.com/gis/sph/\" + str(cert_id)
                    return x
                else:
                    y = \"https://app.paramount-land.com/gis/hgb/\" + str(cert_id)
                    return y""", field_type="TEXT", enforce_domains="NO_ENFORCE_DOMAINS")[0]

            logProcess.logging_process_info('Success to create match table.')

            # append to intermediate table (for historical data)
            logProcess.logging_process_info('Start checking intermediate table...')
            
            if cert_type == 'SPH':
                field = 'cert_id'
                sph_list = []
                
                with arcpy.da.SearchCursor(int_matchTable_SPH, field) as cursor:
                    for row in cursor:
                        extract_row = row[0]
                        sph_list.append(extract_row)
                    del cursor
                
                if idcert in sph_list:
                    if idcert != name:
                        Int_SPH_calc = arcpy.management.CalculateField(in_table=int_matchTable_SPH, field="certificate", expression=f"Concate(!certificate!, !cert_id!, '{idcert}', '{name}')", expression_type="PYTHON3", code_block="""def Concate(certificate, cert_id, idcert, name):
                        if cert_id == idcert:
                            x = str(certificate) + \"; \" + \"https://app.paramount-land.com/gis/sph/\" + str(name)
                            return x
                        else:
                            return certificate""", field_type="TEXT", enforce_domains="NO_ENFORCE_DOMAINS")[0]
                        
                        logProcess.logging_process_info('SPH File {} has been added to id cert {}'.format(name, idcert))
                    else:
                        pass
                else:
                    logProcess.logging_process_info('Start append new SPH file...')
                    arcpy.management.Append(matchTable, int_matchTable_SPH, "NO_TEST", r'cert_id "cert_id" true true false 8000 Text 0 0,First,#,matchTable,cert_id,0,8000;certificate "certificate" true true false 8000 Text 0 0,First,#,matchTable,certificate,0,8000', '', '')
                    
            else:
                field = 'cert_id'
                hgb_list = []
                
                with arcpy.da.SearchCursor(int_matchTable_HGB, field) as cursor:
                    for row in cursor:
                        extract_row = row[0]
                        hgb_list.append(extract_row)
                    del cursor
                
                if idcert in hgb_list:
                    if idcert != name:
                        Int_HGB_calc = arcpy.management.CalculateField(in_table=int_matchTable_HGB, field="certificate", expression=f"Concate(!certificate!, !cert_id!, '{idcert}', '{name}')", expression_type="PYTHON3", code_block="""def Concate(certificate, cert_id, idcert, name):
                        if cert_id == idcert:
                            x = str(certificate) + \"; \" + \"https://app.paramount-land.com/gis/hgb/\" + str(name)
                            return x
                        else:
                            return certificate""", field_type="TEXT", enforce_domains="NO_ENFORCE_DOMAINS")[0]
                        
                        logProcess.logging_process_info('HGB File {} has been added to id cert {}'.format(name, idcert))
                    else:
                        pass
                else:
                    logProcess.logging_process_info('Start append new HGB file...')
                    arcpy.management.Append(matchTable, int_matchTable_HGB, "NO_TEST", r'cert_id "cert_id" true true false 8000 Text 0 0,First,#,matchTable,cert_id,0,8000;certificate "certificate" true true false 8000 Text 0 0,First,#,matchTable,certificate,0,8000', '', '')

            logProcess.logging_process_info('Adding attachment finished successfully.')
        except Exception as e:
            logProcess.logging_process_error('Error encountered! Fail to update data.')
            raise(e)

try:
    uploadFile.update_data()
except Exception as e:
    raise(e)