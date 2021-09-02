from PyPDF2 import PdfFileWriter, PdfFileReader
import tkinter as tk

def encryptPdf(file, password):
    parser = PdfFileWriter()
    pdf = PdfFileReader(file)
    for page in range(pdf.numPages):
        parser.addPage(pdf.getPage(page))
    parser.encrypt(password)
    with open(f"encrypted_{file}", "wb") as f:
        parser.write(f)
        f.close()
    print(f"encrypted_{file} Created...")

if __name__ == "__main__":
    file = "pdf_file_name.pdf"
    password = "password"
    
    window = tk.Tk()
    frame = tk.Frame(master=window, width=400, height=500, bg="white")
    frame.pack()
    window.mainloop()
    