# -*- coding: utf-8 -*-
"""

In this script we are using the sarcasm dataset stored as a json as it is easy to read contents from a json.
We imported the json from the link given below. Then we used a loop to append the appropriate content into 
correct label. We have used out of vocab <OOV> tag for the contents that are not in our dataset. 
We have used padding for the missing words in the sentence label. Read more about pad_sequences in 
this link: https://keras.io/preprocessing/sequence/

"""

!wget --no-check-certificate \
    https://storage.googleapis.com/laurencemoroney-blog.appspot.com/sarcasm.json \
    -O /tmp/sarcasm.json
  
import json

with open("/tmp/sarcasm.json", 'r') as f:
    datastore = json.load(f)


sentences = [] 
labels = []
urls = []
for item in datastore:
    sentences.append(item['headline'])
    labels.append(item['is_sarcastic'])
    urls.append(item['article_link'])



from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
tokenizer = Tokenizer(oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)

word_index = tokenizer.word_index
print(len(word_index))
print(word_index)
sequences = tokenizer.texts_to_sequences(sentences)
padded = pad_sequences(sequences, padding='post')
print(padded[0])
print(padded.shape)
