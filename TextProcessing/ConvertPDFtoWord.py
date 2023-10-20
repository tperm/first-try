import PyPDF2

FILE_PATH = '/Users/troyperment/Documents/Troy/Career/2 Acquisition Business/Brokers/Gateway/Terrys New Dimensions Millwork 2067.pdf'

with open(FILE_PATH, mode='rb') as f:

    reader = PyPDF2.PdfReader(f)

    page = reader.pages

    print(page)