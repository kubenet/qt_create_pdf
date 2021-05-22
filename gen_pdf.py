from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph, SimpleDocTemplate, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib import colors
from get_fio_excel import read_data_from_excel as data_excel

pdfmetrics.registerFont(TTFont('times', 'times.ttf'))

styles = getSampleStyleSheet()

styles.add(ParagraphStyle(name='fio_CENTER',
                          parent=styles['Normal'],
                          fontName='times',
                          wordWrap='LTR',
                          alignment=TA_CENTER,
                          fontSize=30,
                          leading=30,
                          textColor=colors.black,
                          borderPadding=0,
                          leftIndent=0,
                          rightIndent=0,
                          spaceAfter=0,
                          spaceBefore=10,
                          splitLongWords=True,
                          spaceShrinkage=0.05,
                          ))
styles.add(ParagraphStyle(name='text_CENTER',
                          alignment=TA_CENTER,
                          fontName='times',
                          fontSize=16,
                          textColor=colors.black,
                          leading=18,
                          spaceAfter=0,
                          spaceBefore=10,
                          # textTransform='uppercase',
                          wordWrap='LTR',
                          splitLongWords=True,
                          spaceShrinkage=0.05,
                          ))
styles.add(ParagraphStyle(name='text_min_LEFT',
                          alignment=TA_LEFT,
                          fontName='times',
                          fontSize=12,
                          textColor=colors.black,
                          leading=18,
                          spaceAfter=0,
                          spaceBefore=10,
                          # textTransform='uppercase',
                          wordWrap='LTR',
                          splitLongWords=True,
                          spaceShrinkage=0.05,
                          ))
styles.add(ParagraphStyle(name='year_CENTER',
                          alignment=TA_CENTER,
                          fontName='times',
                          fontSize=12,
                          textColor=colors.black,
                          leading=18,
                          spaceAfter=0,
                          spaceBefore=10,
                          # textTransform='uppercase',
                          wordWrap='LTR',
                          splitLongWords=True,
                          spaceShrinkage=0.05,
                          ))


# def string_guy(text):
#     return f'<font name="times">{text}</font>'
#
#
# def parag_guy(text, style=styles['Normal']):
#     return Paragraph(string_guy(text), styles['Normal'])


# im = Image("temp.png", 439, 685)

def generate_pdf(group_list, date1, date2, duration):
    header1 = "<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br " \
              "/>Настоящий сертификат подтверждает, что "
    header2 = "прошел(ла) обучение в АНО ДО Детский технопарк «Кванториум» <br /> по дополнительной общеразвивающей " \
              "программе "
    dates = f"c {date1} по {date2}"
    duration_text = f"в объеме {duration} академических часа"
    space = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp" \
            ";&nbsp;&nbsp; "
    footer = "Директор<br />АНО ДО «Детский технопарк<br />«Кванториум» " + space + space + space + space + "&nbsp;&nbsp;&nbsp; П.И. Мозгалева"

    fio_list = data_excel(group_list)
    kvant = fio_list[0]  # название учебной программы
    for fio in range(1, len(fio_list)):
        print(fio_list[fio])
        story = [Paragraph(header1, styles['text_CENTER']), Paragraph(fio_list[fio], styles['fio_CENTER']),
                 Paragraph(header2, styles['text_CENTER']), Paragraph(kvant, styles['text_CENTER']),
                 Paragraph(dates, styles['text_CENTER']), Paragraph(duration_text, styles['text_CENTER']),
                 Paragraph(footer, styles['text_min_LEFT'])]
        doc = SimpleDocTemplate("pdf\\" + fio_list[fio] + ".pdf", pagesize=A4)
        doc.build(story)
    return 0
