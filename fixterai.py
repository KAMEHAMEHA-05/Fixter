# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 22:19:59 2024

@author: hp5cd
"""

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import tensorflow as tf
from transformers import RobertaTokenizer, TFRobertaForSequenceClassification

# # Download necessary resources (comment out if already downloaded)
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

def issue_tag(description):

    def lemmatize_word(word, pos): 
    # Initialize the WordNetLemmatizer
        lemmatizer = WordNetLemmatizer()

        # Example words with their POS tags
        words_pos = [(word, pos)]

        # Lemmatize each word
        lemmatized_words = [lemmatizer.lemmatize(word, pos=pos) for word, pos in words_pos]

        # Print the original words and their lemmatized forms
        for (word, _), lemma in zip(words_pos, lemmatized_words):
            return lemma

    def segregate_words(text):
        # Tokenize the sentence (split into words)
        tokens = nltk.word_tokenize(text)

        # Use NLTK's part-of-speech tagger
        tags = nltk.pos_tag(tokens)
        # Define empty lists for each category
        nouns = []
        verbs = []
        adjectives = []

        # Loop through tokens and tags, assigning words to categories based on tags
        for token, tag in tags:
            if tag.startswith('NN'): # Common noun tags (NN, NNS)
                token = lemmatize_word(token, wordnet.NOUN)
                nouns.append(token)
            elif tag.startswith('VB'):  # Common verb tags (VB, VBD, VBG, VBP, VBZ)
                token = lemmatize_word(token, wordnet.VERB)
                verbs.append(token)
            elif tag.startswith('JJ'):  # Common adjective tags (JJ, JJR, JJS)
                token = lemmatize_word(token, wordnet.ADJ)
                adjectives.append(token)

        # Return the segregated words
        return {"nouns": nouns, "verbs": verbs, "adjectives": adjectives}

    # Download NLTK resources (if not already downloaded)
    # nltk.download('punkt')
    # nltk.download('stopwords')

    def remove_auxiliary_stopwords(sentence):
        # Tokenize the sentence into words
        words = word_tokenize(sentence)

        # Get English stopwords
        stop_words = set(stopwords.words('english'))

        # List of auxiliary verbs (to be, to have, to do)
        auxiliary_verbs = ['am', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
                           'have', 'has', 'had', 'do', 'does', 'did', 'shall', 'will',
                           'should', 'would', 'may', 'might', 'must', 'can', 'could']

        # Remove auxiliary verbs and stopwords
        filtered_words = [word for word in words if word.lower() not in auxiliary_verbs and word.lower() not in stop_words]

        # Join the filtered words back into a sentence
        filtered_sentence = ' '.join(filtered_words)

        return filtered_sentence

    filt = remove_auxiliary_stopwords(description)
    segregation = segregate_words(filt)['nouns']

    def predict_class(sentence, tokenizer, model, classes):
        # Tokenize the input sentence
        inputs = tokenizer(sentence, return_tensors="tf", truncation=True, padding=True)

        # Make predictions
        outputs = model(inputs)
        predicted_class_index = tf.argmax(outputs.logits, axis=1).numpy()[0]
        predicted_class = classes[predicted_class_index]

        return predicted_class

    # Load the tokenizer and model
    tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
    model = TFRobertaForSequenceClassification.from_pretrained(r"C:\Users\hp5cd\Downloads\sentence_classification_model_v2")

    # Load the classes
    classes = [
        "hygiene_cleanliness",
        "safety_security",
        "maintenance_upkeep",
        "facilities_amenities",
        "internet_connectivity",
        "plumbing",
        "bathroom_supplies",
        "bathroom_hardware",
        "electrical",
        "lighting",
        "furniture"
    ]
    tags = []
    for keyword in segregation:
        word_class = predict_class(keyword, tokenizer, model, classes)
        if word_class not in tags:
            tags.append(word_class)
    dept = predict_class(segregation, tokenizer, model, classes)
    return tags, dept

def priority(tags1, tags2):
    def equalize_length(list1, list2):
        len1 = len(list1)
        len2 = len(list2)
        if len1 == len2:
            return list1, list2
        # If list1 is shorter, extend it with None values to match the length of list2
        if len1 < len2:
            list1 += [None] * (len2 - len1)
        # If list2 is shorter, extend it with None values to match the length of list1
        else:
            list2 += [None] * (len1 - len2)
        return list1, list2

    # Sample keywords and their weights
    keywords = {
        "hygiene_cleanliness": 4,
        "safety_security": 5,
        "maintenance_upkeep": 3,
        "facilities_amenities": 1,
        "internet_connectivity": 2,
        "plumbing": 4,
        "bathroom_supplies": 3,
        "bathroom_hardware": 3,
        "electrical": 5,
        "lighting": 2,
        "furniture": 0
    }
    tag_len = len(keywords)  # Assuming all issues have the same number of tags

    # Assuming these functions are defined elsewhere
    issue1 = []
    issue2 = []

    # Equalize the length of tags lists
    tags1, tags2 = equalize_length(tags1, tags2)

    # Compute scores for each tag based on their keywords and weights
    for x, y in zip(tags1, tags2):
        diff = keywords.get(x, 0) - keywords.get(y, 0)  # If tag not found, default weight is 0
        issue1.append(1 + diff / 2)
        issue2.append(1 - diff / 2)

    # Compute overall scores for both issues
    issue1_score = sum(issue1) / tag_len
    issue2_score = sum(issue2) / tag_len

    # Compare scores to determine priority
    if issue1_score > issue2_score:
        return True
    else:
        return False