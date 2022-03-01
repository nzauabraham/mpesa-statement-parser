# importing required modules
import PyPDF2
import pikepdf

from PyPDF2 import PdfFileWriter, PdfFileReader

# creating a pdf file object
pdfFilename = 'mpesa_statement.pdf'
password = "pass"
pdf = pikepdf.open(pdfFilename, password=password, allow_overwriting_input=True)
pdf.save(pdfFilename)

# Create a PdfFileWriter object
out = PdfFileWriter()

pdfFileObj = open(pdfFilename, 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

file = PdfFileReader(pdfFilename)

# Check if the opened file is still Encrypted
if file.isEncrypted:

    # If encrypted, decrypt it with the password using PyPDF
    file.decrypt(password)

    # Now, the file has been unlocked.
    # Iterate through every page of the file
    # and add it to our new file.
    for idx in range(file.numPages):
        # Get the page at index idx
        page = file.getPage(idx)

        # Add it to the output file
        out.addPage(page)

    # Open a new file "myfile_decrypted.pdf"
    with open(pdfFilename, "wb") as f:

        # Write our decrypted PDF to this file
        out.write(f)

    # Print success message when Done
    print("File decrypted Successfully.")
else:
    # If pikepdf did her job well, the file wont be encrypted
    # If file is not encrypted, print the
    # message
    print("File already decrypted.")

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
print(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()
