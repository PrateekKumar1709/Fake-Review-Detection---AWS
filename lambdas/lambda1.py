import json
import re
import pandas as pd


def lambda_handler(event, context):
    rev = event['text']
    print(rev)
    #print('In Lambda')
    df_inp = pd.DataFrame({ 'text': [rev] })
    clean_review = clean_desc(df_inp['text'])
    # TODO implement
    print(clean_review)
    return {
        'review':clean_review,
        }

def clean_desc(desc):
    clean_1 = re.compile("(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])")
    clean_2 = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")
    desc = [clean_1.sub("", line.lower()) for line in desc]
    desc = [clean_2.sub(" ", line) for line in desc]
    return desc
    