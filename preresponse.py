import nltk
import numpy as np
import pandas as pd
from gensim import corpora,models,similarities
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

training_dataframe= pd.read_csv("/home/dm-admin/dmproject/bankhelpdesk/chatbot/QAC.csv", sep=',', encoding='ISO-8859-1')

def sentences_to_word_tokens(train):
    import re
    #Remove non-letters     
    letters_only = re.sub("[^a-zA-Z]", " ",train) 
    #Convert to lower case, split into individual words
    words = letters_only.lower().split()                             
    #In Python, searching a set is much faster than searching,a list, so convert the stop words to a set
    stops = set(stopwords.words("english"))                   
    #Remove stop words
    token_words= [w for w in words if not w in stops]   
    # Join the words back into one string separated by space,and return the result. 
    return token_words



#cleaning out tokens with only one appearence
def data_tokens_many_occurences(data):
    texts={}
    texts=[sentences_to_word_tokens(query) for query in data]
    from collections import defaultdict
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1

    texts = [[token for token in text if frequency[token] > 1]
         for text in texts]
    return texts

def corpus_creation(list_tokens):
    #creating Dictionary of tokens
    dictionary = corpora.Dictionary(list_tokens)
    token_id=dictionary.token2id
    dictionary.save('/tmp/banks.dict')
    #corpus
    corpus = [dictionary.doc2bow(text) for text in list_tokens]
    corpora.MmCorpus.serialize('/tmp/banks.mm', corpus)  # store to disk, for later use
    dictionary = corpora.Dictionary.load('/tmp/banks.dict')
    corpus = corpora.MmCorpus('/tmp/banks.mm')
    return corpus

def similarity_index(statement):
    test=[]
    test.append(statement)    
    words=data_tokens_many_occurences(training_dataframe['Question'][0:630])
    document_corpus=corpus_creation(words)
    dictionary = corpora.Dictionary.load('/tmp/banks.dict')
    lsi = models.LsiModel(document_corpus,id2word=dictionary,num_topics=70)
    vec_bow = [dictionary.doc2bow(w.lower().split()) for w in test]
    vec_lsi = lsi[vec_bow] # convert the query to LSI space
    index = similarities.MatrixSimilarity(lsi[document_corpus])
    index.save('/tmp/banks.index')
    index = similarities.MatrixSimilarity.load('/tmp/banks.index')
    sims = index[vec_lsi] # perform a similarity query against the corpus
    return list(enumerate(sims))
#cleaning sentences

def reply(sentence):
    a=similarity_index(sentence)
    arr=a[0][1].tolist()
    ind=arr.index(max(arr))
    return(training_dataframe['Answer'][ind])



