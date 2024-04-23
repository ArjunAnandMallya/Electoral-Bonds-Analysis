import fitz
import csv

def pdf_to_csv(pdf_file, csv_file):
    doc = fitz.open(pdf_file)
    
    with open(csv_file, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text()
            csv_writer.writerow([text])

    doc.close()

if __name__ == "__main__":
    pdf_to_csv("input.pdf", "output.csv")

