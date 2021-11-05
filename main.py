from flask import Flask
from flask import request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from nltk.util import ngrams
nltk.download('punkt')
nltk.download('stopwords')


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def aws_flask_app():
    def service1(user_sentence):
        return "You have requested service one.\n"

    def service2(user_sentence):
        return "You have requested service two.\n"

    def service3(user_sentence):
        return "You have requested service three.\n"

    def service4(user_sentence):
        return "You have requested service four.\n"

    def service5(user_sentence):
        return "You have requested service five.\n"

    def service6(user_sentence):
        return "You have requested service six.\n"



    # Make a nice output that tells the user how to submit a POST reqest
    if request.method=='GET':
        return "Hello! I'm the AWS_FLASK_APP! \n"
    
    # user_sentence is the sentence the user inputted. user_service is a number or a list of comma 
    # separated numbers asking for a particular service
    elif request.method=='POST':
        user_sentence = request.form["Sentence"]
        user_services = request.form["Service"]
        
        
        # Split list into individual services
        services = str.split(user_services,",")

        
        res = {'status': '200'}
        
        # Calls correct service depending on user input
        methods = {service1:"1", service2:"2", service3:"3", service4:"4", service5:"5", service6:"6"}
        string = "The sentence you have entered is: {}.\n".format(user_sentence)
        for service in services:
            position = list(methods.values()).index(service)
            string = string + (list(methods.keys())[position](user_sentence))
        return string
          




@app.route("/n_grams/<num>/<text>/")
def run_ngrams(text, num):
    text_list = text.split()
    try:
        num = int(num)
    except ValueError:
        return "Num must be a number"
    if num <= 0:
        return "Num must greater than 0"
    n_grams = ngrams(text_list,num)
    return ' '.join([','.join(grams) for grams in n_grams])


@app.route("/tokenize/<text>/")
def get_tokens_and_tags(text):
   tokens = nltk.word_tokenize(text)
    tags = nltk.pos_tag(tokens)
    return ' '.join(['='.join(tag) for tag in tags])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


