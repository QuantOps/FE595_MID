from flask import Flask
from flask import request
from flask import render_template
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from nltk.util import ngrams
from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


# Simple list to string conversion method taken from https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
def listToString(s):
   str_one = ""
   for ele in s:
       str_one = str_one + " " + ele
   return str_one


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def aws_flask_app():
   def service1(user_sentence):
       analyzer = SentimentIntensityAnalyzer()
       output = analyzer.polarity_scores(user_sentence)
       return "You have requested a Vader sentiment analysis on your sentence: \"{}.\"".format(user_sentence) + " Here is your output: \n" + "Negative Score: {}\n".format(output['neg']) + "Neutral Score: {}\n".format(output['neu']) + "Positive Score: {}\n".format(output['pos']) + "Compound Score: {}\n".format(output['compound'])+ "\n"


   def service2(user_sentence):
       stopWords = set(stopwords.words('english'))
       tokens = word_tokenize(user_sentence)
       outputStops = []
       outputSentence = []

       for token in tokens:
           if token not in stopWords:
               outputSentence.append(token)
           else:
               outputStops.append(token)

       return "You have requested to remove stop words from your sentence: \"{}.\"".format(user_sentence) + " Here is your output: \n" + "The stop words in your sentence are:" + listToString(outputStops) + "\nYour sentence without stop words now reads:" + listToString(outputSentence) + "\n"+ "\n"

   #Neil
   def service3(user_sentence):
       text_list = user_sentence.split()
       n_grams = ngrams(text_list,2)
       return "You have requested to run n grams on your sentence: \"{}.\"".format(user_sentence) + " Here is your output:\n"+' '.join([','.join(grams) for grams in n_grams]) + "\n"+ "\n"

   #Neil
   def service4(user_sentence):
       tokens = nltk.word_tokenize(user_sentence)
       tags = nltk.pos_tag(tokens)
       return "You have requested to tokenize your sentence: \"{}.\"".format(user_sentence) + " Here is your output:\n"+' '.join(['='.join(tag) for tag in tags]) + "\n"+ "\n"


   #Luke
   def service5(user_sentence):
       stemmer = PorterStemmer()
       inputs=user_sentence.split()
       final=[]

       for word in inputs:
           final.append(stemmer.stem(word))

       return "You have requested to stem your sentence: \"{}.\"".format(user_sentence) + " Here is your output:\n" + listToString(final) + "\n"+ "\n"

   #Luke
   def service6(user_sentence):
       lemmatizer = WordNetLemmatizer()
       inputs=user_sentence.split()
       final=[]

       for word in inputs:
           final.append(lemmatizer.lemmatize(word,pos="v"))
       return "You have requested to lemmatize your sentence: \"{}.\"".format(user_sentence) + " Here is your output:\n" + listToString(final) + "\n"+ "\n"


   # Make a nice output that tells the user how to submit a POST request
   if request.method=='GET':
       return '''<body style="background-color:#DCDBDE"> Hello! Welcome to the AWS Flask App implementing Natural Language Processing! \n This flask app will run NLP services on any sentence you provide. These are the services we offer:<br><br><br> <table border="1">
               <tr style="background-color:#2CCAF4">
                   <th>Service Number</th>
                   <th>Service Name</th>
                   <th>Explanation</th>
               </tr>
               <tr>
                   <td>1.</td>
                   <td>Sentiment</td>
                   <td>This service uses the VaderSentiment package to provide a sentiment score on the entered text. This returns a positive, negative, neutral, and compound(combined) score on the text entered. </td>
               </tr>
               <tr>
                   <td>2.</td>
                   <td>Stop Words</td>
                   <td>This service removes stop words from the given text entry. Stop words are commonly used words in the English language that hold little information when completing a text analysis. This function will return the text without stop words and the stop words that were present.</td>
               </tr>
               <tr>
                   <td>3.</td>
                   <td>N-Grams</td>
                   <td>This service will run n-grams on the entered text. It returns each combination of two adjacent words in a sentence. All combinations are returned.</td>
               </tr>
               <tr>
                   <td>4.</td>
                   <td>Tokenize</td>
                   <td>This service will tokenize a given text entry. Tokenization is the process of splitting text into smaller units called tokens. Most of the time these tokens are individual words. This function returns each token and its corresponding part of speech. </td>
               </tr>
               <tr>
                   <td>5.</td>
                   <td>Stemmer</td>
                   <td>This function will stem every word in a given text entry. Stemming is the process of reducing words to their stem by removing prefixes and suffixes. This function returns a list of every stemmed word entered. </td>
               </tr>
               <tr>
                   <td>6.</td>
                   <td>Lemmatizer</td>
                   <td>This function will lemmatize every word in a given text entry. Lemmatizing is the process of reducing words to their lemma by removing the conjugation of a verb. This function returns a list of every lemmatized word entered. </td>
               </tr>
               </table>
               <br><br><br>

               This is how to access these services with any given text:
                   <table border="1">
               <tr style="background-color:#2CCAF4">
                   <th>Type of Call</th>
                   <th>How to execute the call</th>
               </tr>
               <tr>
                   <td>GET request using a browser</td>
                   <td>To execute this GET request, a specific URL address must be accessed within a web browser. The URL address is 18.218.9.163:8080/service/text <br> "Service" can be replaced by the keywords associated with each service: n_grams, tokenize, sentiment, stop_words, stem, lemma. <br> "Text" refers to the sentence or words that the NLP service will be run on. </td>
               </tr>
               <tr>
                   <td>CURL call using terminal</td>
                   <td>To execute this CURL call, open terminal and run the following code: <br><br> curl --location --request POST 'http://18.218.9.163:8080/' \--form 'Sentence="I am happy"' \--form 'Service="1,2,3"'<br><br> The "sentence" parameter can be changed to enter any text that an NLP service should be run on. This should be entered within the shown quotes. The "service" parameter is a list of the *NUMBER* of the service/services that want to be done. The corresponding numbers are listed below to show which service is paired with what number. If multiple services want to be run, a comma can be used to divide the numbers within the quotes.  </td>
               </tr>
               <tr>
                   <td>POST request using python</td>
                   <td>To run a post request within python, the following code should be entered: <br><br> import requests <br> url = "http://18.218.9.163:8080/" <br> payload={'Sentence': 'I am happy', 'Service': '1,2,3'} <br> files=[] <br> headers = {} <br> response = requests.request("POST", url, headers=headers, data=payload, files=files) <br> print(response.text)<br><br> The "sentence" and "service" parameters should be changed as explained above, with services being a list of numbers divided by commas.
               </tr>
               </table>
               <br><br><br><br>
               For the service entries that require numbers, follow the format listed below:
               <table border="1">
               <tr style="background-color:#2CCAF4">
                   <th>Number of Service</th>
                   <th>Service</th>
               </tr>
               <tr>
                   <td>1.</td>
                   <td>Sentiment</td>
               </tr>
               <tr>
                   <td>2.</td>
                   <td>Stop words</td>
               </tr>
               <tr>
                   <td>3.</td>
                   <td>N-grams</td>
               </tr>
               <tr>
                   <td>4.</td>
                   <td>Tokenize</td>
               </tr>
               <tr>
                   <td>5.</td>
                   <td>Stemmer</td>
               </tr>
               <tr>
                   <td>6.</td>
                   <td>Lemmatization</td>
               </tr>

               </table>

               </body>          '''

   # user_sentence is the sentence the user inputted. user_service is a number or a list of comma
   # separated numbers asking for a particular service
   elif request.method=='POST':
       try:
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
       except:
           return "The request entered is invalid. Please reference http://18.218.9.163:8080/ for an explanation on how to make a valid call."

@app.errorhandler(404)
def page_not_found(e):
   return '''
<html lang="en">
<body>

<h1>Status: 404</h1>

</body>
</html>
<br> The request entered is invalid. Please reference http://18.218.9.163:8080/ for an explanation on how to make a valid call.
'''

@app.route("/n_grams/<text>/")
def run_ngrams(text):
   text_list = text.split()
   n_grams = ngrams(text_list,2)
   return "You have requested to run n grams on your sentence: \"{}.\"".format(text) + " Here is your output:<br>"+' '.join([','.join(grams) for grams in n_grams])


@app.route("/tokenize/<text>/")
def get_tokens_and_tags(text):
  tokens = nltk.word_tokenize(text)
  tags = nltk.pos_tag(tokens)
  return "You have requested to tokenize your sentence: \"{}.\"".format(text) + " Here is your output:<br>"+' '.join(['='.join(tag) for tag in tags])

@app.route("/sentiment/<text>/")
def vaderSent(text):
  analyzer = SentimentIntensityAnalyzer()
  output = analyzer.polarity_scores(text)
  return "You have requested a Vader sentiment analysis on your sentence: \"{}.\"".format(text) + " Here is you output: <br>" + "Negative Score: {}<br>".format(output['neg']) + "Neutral Score: {}<br>".format(output['neu']) + "Positive Score: {}<br>".format(output['pos']) + "Compound Score: {}<br>".format(output['compound'])

@app.route("/stop_words/<text>/")
def stopWords(text):
   stopWords = set(stopwords.words('english'))
   tokens = word_tokenize(text)
   outputStops = []
   outputSentence = []

   for token in tokens:
       if token not in stopWords:
           outputSentence.append(token)
       else:
           outputStops.append(token)

   return "You have requested to remove stop words from you sentence: \"{}.\"".format(text) + " Here is you output:<br>" + "The stop words in your sentence are:" + listToString(outputStops) + "<br>Your sentence without stop words now reads:" + listToString(outputSentence) + "<br>"

@app.route("/stem/<text>/")
def stem(text):
   stemmer = PorterStemmer()
   inputs=text.split()
   final=[]

   for word in inputs:
           final.append(stemmer.stem(word))

   return "You have requested to stem your sentence: \"{}.\"".format(text) + " Here is your output:<br>" + listToString(final)

@app.route("/lemma/<text>/")
def lem(text):
   lemmatizer = WordNetLemmatizer()
   inputs=text.split()
   final=[]

   for word in inputs:
           final.append(lemmatizer.lemmatize(word,pos="v"))
   return "You have requested to lemmatize your sentence: \"{}.\"".format(text) + " Here is your output:<br>" + listToString(final)


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080)