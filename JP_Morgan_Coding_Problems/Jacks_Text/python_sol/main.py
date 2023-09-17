'''
Problem Statement: 

Jack is learning to type english from the beginning and he is
making the error of repeating the same words in his texts over 
whatsapp. Write a function that will take input for his text 
sent to you and then keep only the unique texts. 

Note that, the uniqueness is about being word specific not position, 
there are nothing but alphabets in the sentences and words are 
separated only with white space. 

Constraints: 
- words in the line <= 10^5
- alphabets in the word <= 20

Sample input:
- Send send the image send to to to me

Output: 
- Send the image to me
'''

def main():
    sentence = input().split()
    seen_words = set()
    new_sentence = ""

    seen_words.add(sentence[0].lower())
    new_sentence += f"{sentence[0]} "

    for i in range(1, len(sentence)):
        if sentence[i] in seen_words:
            continue
        else:
            seen_words.add(sentence[i])
            new_sentence += f"{sentence[i]} "

    print(new_sentence)

if __name__ == "__main__":
    main()