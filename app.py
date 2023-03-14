import datetime
import glob
import os, sys
import os.path
import csv
import shutil
from flask import Flask, render_template, jsonify, request, redirect, url_for
     
app = Flask(__name__)
app.config['UPLOAD_SPH'] = r'C:\Users\jrsitompul\OneDrive - ESRI Indonesia\WORK_DATA_JOJO\PROJECT\2020-2022\PARAMOUNT_LAND\folder_sertifikat\SPH' #r'//172.31.255.201/datastore/Temp_Folder_Dev'
app.config['UPLOAD_HGB'] = r'C:\Users\jrsitompul\OneDrive - ESRI Indonesia\WORK_DATA_JOJO\PROJECT\2020-2022\PARAMOUNT_LAND\folder_sertifikat\HGB'
# app.config['UPLOAD_IMB'] = r'C:\Users\jrsitompul\OneDrive - ESRI Indonesia\WORK_DATA_JOJO\PROJECT\2020-2022\PARAMOUNT_LAND\folder_sertifikat\IMB'

@app.route('/')
def index():
    return render_template('index.html')
   
@app.route("/", methods=["POST"])
def upload_file():
    uploaded_file = request.files['file']
    cert_type = request.form['cert_type']
    cert_id = request.form['cert_id']
    csv_table = r'C:\Users\jrsitompul\OneDrive - ESRI Indonesia\WORK_DATA_JOJO\PROJECT\2020-2022\PARAMOUNT_LAND\folder_sertifikat\input_parameter.csv'
    csv_table_fix = r'C:\Users\jrsitompul\OneDrive - ESRI Indonesia\WORK_DATA_JOJO\PROJECT\2020-2022\PARAMOUNT_LAND\folder_sertifikat\input_parameter_fix.csv'
    if uploaded_file.filename != '' and cert_type == 'SPH':
        name = uploaded_file.filename.split(sep='.')[0]
        final_file = app.config['UPLOAD_SPH'] + '\{}'.format(uploaded_file.filename)
        if os.path.exists(final_file):
            file_time = datetime.datetime.today()
            file_time_str = datetime.datetime.strftime(file_time, "%d-%m-%Y_%H%M")
            file_time_name = name + '_{}'.format(file_time_str)
            final_file_time = '{}.pdf'.format(file_time_name)
            uploaded_file.save(os.path.join(app.config['UPLOAD_SPH'], final_file_time))
            print(final_file_time)
            print(cert_type)
            print(cert_id)

            writer = csv.writer(open(csv_table, "w"), delimiter=",")

            # write a header row (the table will have three columns: certificate, cert_type, and cert_id)
            writer.writerow(['certificate', 'cert_type', 'cert_id'])

            # checking latest file uploaded and write a row to the table
            writer.writerow([file_time_name, cert_type, cert_id.upper()])
            del writer

            # delete additional line/row in csv table
            with open(csv_table) as input, open(csv_table_fix, 'w', newline='') as output:
                writer = csv.writer(output)
                for row in csv.reader(input):
                    if any(field.strip() for field in row):
                        writer.writerow(row)
                input.close()
                output.close()
        else:
            print(final_file)
            uploaded_file.save(os.path.join(app.config['UPLOAD_SPH'], uploaded_file.filename))
            print(uploaded_file.filename)
            print(cert_type)
            print(cert_id)

            writer = csv.writer(open(csv_table, "w"), delimiter=",")

            # write a header row (the table will have three columns: certificate, cert_type, and cert_id)
            writer.writerow(['certificate', 'cert_type', 'cert_id'])

            # checking latest file uploaded and write a row to the table
            writer.writerow([name, cert_type, cert_id.upper()])
            del writer

            # delete additional line/row in csv table
            with open(csv_table) as input, open(csv_table_fix, 'w', newline='') as output:
                writer = csv.writer(output)
                for row in csv.reader(input):
                    if any(field.strip() for field in row):
                        writer.writerow(row)
                input.close()
                output.close()
        
        os.remove(csv_table)

    elif uploaded_file.filename != '' and cert_type == 'HGB':
        name = uploaded_file.filename.split(sep='.')[0]
        final_file = app.config['UPLOAD_HGB'] + '\{}'.format(uploaded_file.filename)
        if os.path.exists(final_file):
            file_time = datetime.datetime.today()
            file_time_str = datetime.datetime.strftime(file_time, "%d-%m-%Y_%H%M")
            file_time_name = name + '_{}'.format(file_time_str)
            final_file_time = '{}.pdf'.format(file_time_name)
            uploaded_file.save(os.path.join(app.config['UPLOAD_HGB'], final_file_time))
            print(final_file_time)
            print(cert_type)
            print(cert_id)

            writer = csv.writer(open(csv_table, "w"), delimiter=",")

            # write a header row (the table will have three columns: certificate, cert_type, and cert_id)
            writer.writerow(['certificate', 'cert_type', 'cert_id'])

            # checking latest file uploaded and write a row to the table
            writer.writerow([file_time_name, cert_type, cert_id.upper()])
            del writer

            # delete additional line/row in csv table
            with open(csv_table) as input, open(csv_table_fix, 'w', newline='') as output:
                writer = csv.writer(output)
                for row in csv.reader(input):
                    if any(field.strip() for field in row):
                        writer.writerow(row)
                input.close()
                output.close()
        else:
            print(final_file)
            uploaded_file.save(os.path.join(app.config['UPLOAD_HGB'], uploaded_file.filename))
            print(uploaded_file.filename)
            print(cert_type)
            print(cert_id)

            writer = csv.writer(open(csv_table, "w"), delimiter=",")

            # write a header row (the table will have three columns: certificate, cert_type, and cert_id)
            writer.writerow(['certificate', 'cert_type', 'cert_id'])

            # checking latest file uploaded and write a row to the table
            writer.writerow([name, cert_type, cert_id.upper()])
            del writer

            # delete additional line/row in csv table
            with open(csv_table) as input, open(csv_table_fix, 'w', newline='') as output:
                writer = csv.writer(output)
                for row in csv.reader(input):
                    if any(field.strip() for field in row):
                        writer.writerow(row)
                input.close()
                output.close()
        
        os.remove(csv_table)
    # elif uploaded_file.filename != '' and cert_type == 'Izin Mendirikan Bangunan (IMB)':
    #     uploaded_file.save(os.path.join(app.config['UPLOAD_IMB'], uploaded_file.filename))
    #     print(cert_type)
    #     print(uploaded_file.filename)
    else:
        print(cert_id)
    return redirect(url_for('index'))
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)