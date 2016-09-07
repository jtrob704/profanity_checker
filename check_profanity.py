import urllib


def read_text():
    quotes = open("/Users/jaittariusrobinson/Documents/profanity_checker/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=shot" + text_to_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print ("!Profanity Alert!")
    elif "false":
        print ("No profanity found!")
    else:
        print ("Unable to read document")

read_text()