
import shutil, os
import PyPDF2

def file_manager(file_source_dir, file_destination_dir):
    source_dir = file_source_dir
    destination_dir = file_destination_dir


    files = os.listdir(source_dir)

    for file_name in files:
        if os.path.join(source_dir, file_name).endswith('.pdf'):
            pdfFileObject = open(os.path.join(source_dir, file_name), 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
            text=''
            for i in range(0,pdfReader.numPages):
                # creating a page object
                pageObj = pdfReader.getPage(i)
                # extracting text from page
                if 'Banking' in pageObj.extract_text():
                    pdfFileObject.close()
                    shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'Banking//'+ file_name))
                    print(file_name + ' moved successfully to folder "Banking" ')
                    break
                elif 'Technology' in pageObj.extract_text():
                    pdfFileObject.close()
                    shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'IT//'+ file_name))
                    print(file_name + ' moved successfully to folder "IT" ')
                    break
                elif 'Automobiles' in pageObj.extract_text():
                    pdfFileObject.close()
                    shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'Automobiles//'+ file_name))
                    print(file_name + ' moved successfully to folder "Automobiles" ')
                    break
        else:
            print('Not a pdf file')



source = 'C:\\Users\\mubar_dyaglyf\\OneDrive\\Documents\\Projects\\pdf_classifier\\source'
destination = 'C:\\Users\\mubar_dyaglyf\\OneDrive\\Documents\\Projects\\pdf_classifier\\result'

file_manager(source, destination)