# PDF classifier with Python

## Table of Contents
+ [About](#about)
+ [Dependencies](#dependencies)
+ [Usage](#usage)
+ [References](#references)

## About <a name = "about"></a>
This is a simple Python program for classifying PDF files according to their content. Texts are extracted from pdf files with PyPDF2 library, checked with given keywords and if they are a match the Pdf files are moved to destination folders using move method from shutil module.

## Dependencies <a name = "dependencies"></a>
* PyPDF2 (https://github.com/py-pdf/PyPDF2)  
```
pip install PyPDF2
```


## Usage <a name = "usage"></a>

1. Assign path to the folder containing pdf file to **source** variable :
```
source = 'C:\\Users\\example\\pdfSource'
```
2. Assign path to destination folder to **destination** variable:

```
destination = 'C:\\Users\\example\\destination'
```
3. Change if else ladder in function **file_manager** with your requirements:

```
if 'Banking' in pageObj.extract_text():
                    pdfFileObject.close()
                    shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'Banking//'+ file_name))
                    print(file_name + ' moved successfully to folder "Banking" ')
                    break
```
Here **Banking** after 'if' is the keyword given to the program for classifying pdf file. In shutil.move() method, replace **Banking** before **+ file_name** with your folder name in destination folder.

4. Call file_manager method
```
file_manager(source, destination)
```

## References <a name = "references"></a>
* PyPDF2 Library for Working with PDF Files in Python - https://www.analyticsvidhya.com/blog/2021/09/pypdf2-library-for-working-with-pdf-files-in-python/