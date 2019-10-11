# DEL 2 FRES

TEXT1 = ["The politician who holds the authority of all EU countries has just completely condemned a chunk of the British cabinet wondering aloud",
"What that special place in hell looks like for those who promoted Brexit without even a sketch of a plan how to carry it out safely",
"Sure for a long time the EU has been frustrated with how the UK has approached all of this",
"And sure plenty of voters in the UK are annoyed too at how politicians have been handling these negotiations",
"But it is quite something for Donald Tusk to have gone in like this studs up even though he sometimes reminisces about his time as a football hooligan in his youth"]

TEXT2 = ["An outbreak of the flu in Alabama has closed an elementary and middle school with school officials struggling to find enough healthy teachers to teach",
"The schools will be closed for the rest of the week because of the number of cases of flu among students and employees",
"Lawrence County Schools Superintendent Jon Bret Smith told news outlets that Moulton Elementary School and Moulton Middle School are closed Wednesday through Friday"]


vowels = ["A" , "E" , "I" , "O" , "U" , "a" , "e" , "i" , "o" , "u"]

# a loop that goes though each text and finds the total amount of words, "syllables" and sentences.
texts = [TEXT1, TEXT2]
text_no = 0
for text in texts:
    total_words = 0
    total_syllables = 0
    for sentence in text:
        for letter in sentence:
            # loop goes through every letter in all sentences to count the total amount of vowels.
            if letter in vowels:
                total_syllables += 1
        # total words is found by splitting each sentence by spaces and returning the length of this list.
        total_words += len(sentence.split(" "))
    # total sentences is simply the length of the text since each element is a new sentence.
    total_sentences = len(text)
    text_no += 1

    print("\nResult of text number ", text_no)
    print("total_words:", total_words)
    print("total_sentences:", total_sentences)
    print("total_syllables:", total_syllables)

    # calculation of the reading score
    flesch_reading_ease_score = 206.835-1.015*(total_words/total_sentences) - 84.0*(total_syllables/total_words)

    print("Flesch Reading Ease Score:", flesch_reading_ease_score)
