import urllib

def read_text():
    quotes = open("C:\Users\Nachiket\Google Drive\Python\Practice Problems\movie_quotes.txt")
    contents_of_file = quotes.read()
    print '\nOriginal talk -'
    print   contents_of_file +'\n'
    quotes.close()
    pirate_talk(contents_of_file)
    
def pirate_talk(text_to_check):
    connection = urllib.urlopen("http://isithackday.com/arrpi.php?text="+text_to_check)
    output = connection.read()
    print 'Pirate talk -\t'
    print output
    connection.close()
read_text()
    