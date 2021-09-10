import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
import load_data

def __readfile__(__namefile__):
    file = open(__namefile__,'r')
    load_f = load_data.__dell__(file.read())
    dic_file = sent_tokenize(load_f)
    return dic_file

