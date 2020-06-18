import urllib.request
def read_text():
    quotes = open("E:\Sehari-hari\Proyek\Python\ProfanityEditor\profane.txt")
    contentsOfFile = quotes.read()
    print(contentsOfFile)
    quotes.close()
    check_profanity(contentsOfFile)
def check_profanity(text_to_check):
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q"+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
read_text()

