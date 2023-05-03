from LocalFunctions import *

if __name__ == '__main__':

    path = r'C:\Users\User\Desktop\ОМ-СМЭ\files\nfactorial incubator\names.txt'

    bg = open_and_read(path)
    print('The length of the names.txt file: ', len(bg))

    bg = extract_bigrams(bg)
    print('Now, bigrams from file are extracted and saved into list')

    bg = convert_bg_to_dict(bg)
    print('The list is now converted to dict with keys and probabilities as values and the length is: ', len(bg))

    df = dict_to_df(bg) #converting into dataFrame

    export_table(df, 'bigram table.xlsx') #exporting excel file of bigrams table
    print('The table of bigrams with probabilities is now exported.')
    print('Generating Attempt 1: ', generate())
    print('Generating Attempt 2: ', generate(min_len=5, max_len=6))
    print('Generating Attempt 3: ', generate(min_len=4, max_len=7))

    plot_word_cloud(bg, save_fig=True, path='Bigrams.png')
