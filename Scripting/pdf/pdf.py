import pypdf

template = pypdf.PdfReader(open("Scripting/pdf/files/twopage.pdf", "rb"))
watermark = pypdf.PdfReader(
    open("Scripting/pdf/files/wtr.pdf", "rb")
)
output = pypdf.PdfWriter()

# for i in range(len(template.pages)):
#     page = template.pages[i]
#     page.merge_page(watermark.pages[0])
#     output.add_page(page)

# with open("Scripting/pdf/watermaked_output.pdf", "wb") as outputFile:
#     output.write(outputFile)

def merge_pdfs(template_path, watermark_path, output_path):
    template = pypdf.PdfReader(open(template_path, "rb"))
    watermark = pypdf.PdfReader(open(watermark_path, "rb"))
    output = pypdf.PdfWriter()

    for i in range(len(template.pages)):
        page = template.pages[i]
        page.merge_page(watermark.pages[0])
        output.add_page(page)

    with open(output_path, "wb") as outputFile:
        output.write(outputFile)
    

if __name__ == "__main__":
    pdf_path_1 = "Scripting/pdf/files/twopage.pdf"
    pdf_path_2 = "Scripting/pdf/files/wtr.pdf"
    output_path = "Scripting/pdf/watermaked_output.pdf"
    merge_pdfs(pdf_path_1, pdf_path_2, output_path)
