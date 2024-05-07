import fpdf
import csv
import os

pdf_doc = fpdf.FPDF(unit='in', format='Letter')
pdf_doc.set_auto_page_break(auto=True, margin=0.5)

id_template_path = './id.png'

with open('Employee_data.csv', 'r') as emp_data_file:
    data_reader = csv.DictReader(emp_data_file)
    header_row = data_reader.fieldnames

    for emp_row in data_reader:
        emp_name = emp_row['Name']
        emp_position = emp_row['Position']
        emp_photo_path = emp_row['Photo']

        pdf_doc.add_page()

        pdf_doc.image(id_template_path, 0, 0, 6.5, 4)

        pdf_doc.set_font('times', 'B', 24)
        pdf_doc.text(1.2, 3.5, emp_name)

        pdf_doc.set_font('times', '', 16)
        pdf_doc.text(2.5, 3.8, emp_position)

        pdf_doc.image(emp_photo_path, 4, 0.6, 1.5, 2, type='JPG')

pdf_doc.output('ID.pdf')
