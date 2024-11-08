import pandas as pd
import csv
import re
from collections import Counter

def read_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        text = ""
        for row in reader:
            text += ' '.join(row) + " "  
    return text
def tokenize_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    return words
def word_frequencies(words):
    return Counter(words)
def show_word_frequencies(frequencies):
    df = pd.DataFrame(frequencies.items(), columns=['Word', 'Frequency'])
    df = df.sort_values(by='Frequency', ascending=False).reset_index(drop=True)
    return df
def main(file_path):
    text = read_csv(file_path)               
    words = tokenize_text(text)             
    frequencies = word_frequencies(words)  
    df = show_word_frequencies(frequencies)  
    return df
file_path = 'C:/Users/Administrator/Desktop/Python_Labs/Python_Labs/Class_Codes\Assessment_1/CSV_File/Novel.csv.txt'
df = main(file_path)
print(df)
