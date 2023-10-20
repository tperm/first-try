import PyPDF2
inputloc = "/Users/troyperment/Documents/Troy/Career/1 Startup/Business Model Canvas-2023.pdf"
outputloc = "/Users/troyperment/Documents/Troy/Career/1 Startup/100 Business Model Canvases.pdf"
# Open the source PDF file
with open(inputloc, 'rb') as source_file:
    pdf_reader = PyPDF2.PdfReader(source_file)

    # Create a new PDF file to save the duplicated pages
    with open(outputloc, 'wb') as output_file:
        pdf_writer = PyPDF2.PdfWriter()

        # Get the first page (page 0) from the source PDF
        page = pdf_reader.pages[0]

        # Add the same page 100 times to the output PDF
        for _ in range(100):
            pdf_writer.add_page(page)

        # Write the modified PDF to the output file
        pdf_writer.write(output_file)

print("PDF duplication complete.")
