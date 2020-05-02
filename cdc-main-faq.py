import unicodedata
import pandas as pd
import requests  

# Adds time stamp to output filename
import time
timestr = time.strftime("%Y%m%d-%H%M%S")

# The url to be scraped
r = requests.get('https://www.cdc.gov/coronavirus/2019-ncov/faq.html')

from bs4 import BeautifulSoup  
soup = BeautifulSoup(r.text, 'html.parser')

questions = soup.select('.card-header .card-title')
answers = soup.select('.accordion .card-body')

# Removes attributes from html output, except img and a attributes
def remove_attributes(answers):
    whitelist = ['a','img']
    for tag in soup.find_all(True):
        if tag.name not in whitelist:
            tag.attrs = {}
        else:
            attrs = dict(tag.attrs)
            for attr in attrs:
                if attr not in ['src','href']:
                    del tag.attrs[attr]
    return answers

answers = remove_attributes(answers)

question_list = []
for question in questions:
    question = question.find('span').text
    question_list.append(question)

answer_list = []
for answer in answers:
#    answer = answer.find('p')
    if answer is not None:
        answer_string = str(answer)
        answer_strip = answer_string.replace('external icon', '').replace('pdf icon', '')
        answer_list.append(answer_strip)

#print(question_list)
#print(answer_list)

# Merges questions and answers via zip
merged_qa = list(zip(question_list, answer_list))

# print(merged_qa)

df = pd.DataFrame(merged_qa, columns= ['Question', 'Answer'])

# print(df)

df.to_csv (r'csv/cdc-main-faq-' + timestr + '.csv', index = False, header=True)