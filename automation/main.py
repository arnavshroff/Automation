import pyttsx3
import PyPDF2
from googletrans import Translator

book = open('wonder.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(129)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
translater = Translator()
out = translater.translate(text,dest="hi")
output = out.text
print(output)