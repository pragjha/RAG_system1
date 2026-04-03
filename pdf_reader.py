import PyPDF2
import os 
from pathlib import Path


def extract_pdf_to_txt(pdf_path:str, output_dir:str):
    #create output directory if it does not exist
    Path(output_dir).mkdir(parents=True,exist_ok=True)

    #open and read the pdf
    with open(pdf_path,'rb'):
        pdf_reader=PyPDF2.PdfReader(pdf_file)
        num_pages=len(pdf_reader.pages)

        #extract text from each page
        for page_num in range(num_pages):
            page=pdf_reader.pages[page_num]
            text=page.extract_text()

            #save to individual text file
            output_file=os.path.join(output_dir,f"page_{page_num}")
            with open(output_file, 'w', encoding='utf-8') as txt_file:
                txt_file.write(text)

                print(f"Extracted page {page_num +1} to {output_file}")
            


if __name__=="__main__":
    pdf_file = r"C:\Users\rkjha\Downloads\RAG application-ref -insta_nilesh\Think-And-Grow-Rich_2011-06.pdf"
    extract_pdf_to_txt(pdf_file,"output")