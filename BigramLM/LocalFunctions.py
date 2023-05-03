import pandas as pd
import random
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def open_and_read(file_name): #function for opening and reading file
    names = []
    with open(file_name, encoding='utf8') as f: #opening txt file
        for line in f:
            names.append(line.replace('\n', '')) #saving each line to list with replacing '\n'
    return names

def extract_bigrams(names): #function for extracting bigrams from txt file
    bigrams = []
    for n in names:
        for i in range(len(n)):
            if i == 0:
                bigrams.append('^' + n[i]) #adding to list first letters with '^' added before them
            else:
                bigrams.append(n[i - 1] + n[i]) #adding to list pair of letters
            if i == len(n) - 1:
                bigrams.append(n[i] + '$') #adding to list last letters with '$' added after them
    return bigrams

def convert_bg_to_dict(bigrams): #function for converting bigrams list to dict with key and count as value
    l = len(bigrams)
    bigrams = Counter(bigrams) #using Counter to count occurence of each bigram and export as dict

    for k in bigrams.keys():
        bigrams[k] = bigrams[k] / l #rewriting values with probability

    return bigrams

def dict_to_df(bg): #function for converting dict to dataframe
    global df
    df = pd.DataFrame(bg.items(), columns=['Bigram', 'Probability'])
    return df

def export_table(df, output_file): #function for exporting the df to excel
    df.to_excel(output_file, index=False)

def get_next(letter): #function for getting next letter for a new name
    global df #using random.choices for choosing one letter based on previous letter with weights as probability
    next_letter = random.choices(list(df[df['Bigram'].str.startswith(letter)]['Bigram']),
                                 weights=list(df[df['Bigram'].str.startswith(letter)]['Probability']))[0][1]
    return next_letter


def generate(min_len=3, max_len=10): #function for generating new name from existing bigrams, parameters for giving size of new name
    new_name = get_next('^')
    while len(new_name) <= max_len:
        new_name += get_next(new_name[-1])
        if new_name[-1] == '$':
            new_name = new_name[:-1]
            if len(new_name) >= min_len:
                break

    return new_name

def plot_word_cloud(bg, save_fig=False, path='WordCloud.png'): #function for plotting wordcloud for better visualization
    wordcloud = WordCloud(width=2000, height=1200, background_color="white").generate_from_frequencies(bg)
    plt.rcParams["figure.figsize"] = (20, 12)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.margins(x=0, y=0)
    if save_fig:
        plt.savefig(path, bbox_inches='tight')
    plt.show()
