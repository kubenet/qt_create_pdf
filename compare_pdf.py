def compare_pdf():
    import os
    from PyPDF2 import PdfFileWriter, PdfFileReader
    import io
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont

    from reportlab.rl_config import defaultPageSize

    PAGE_WIDTH = defaultPageSize[0]
    pdfmetrics.registerFont(TTFont('times', 'times.ttf'))

    packet = io.BytesIO()
    # create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont("times", 12)
    can.drawCentredString((PAGE_WIDTH - 11) / 2.0, 30.0, "2021, Томск")
    can.save()
    pdf_path = os.getcwd() + "\\pdf"
    i = 0
    for file in os.listdir(pdf_path):
        packet.seek(0)
        new_pdf = PdfFileReader(packet)
        # read your existing PDF
        f = open("pdf\\" + file, "rb")
        text_pdf = PdfFileReader(f)
        template_pdf = PdfFileReader(open("template_0.pdf", "rb"))
        output = PdfFileWriter()

        # add the "watermark" (which is the new pdf) on the existing page
        page = template_pdf.getPage(0)
        page.mergePage(text_pdf.getPage(0))
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)
        # finally, write "output" to a real file
        outputStream = open("result\\" + file + "_" + str(i) + ".pdf", "wb")
        output.write(outputStream)
        outputStream.close()
        f.close()
    packet.close()
