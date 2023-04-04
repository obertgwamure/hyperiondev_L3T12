import spacy
nlp = spacy.load('en_core_web_md')


word1 = nlp("wife")
word2 = nlp("honey")
word3 = nlp("bee")

print(f'{word1} and {word2}',word1.similarity(word2))
print(f'{word3} and {word2}',word3.similarity(word2))
print(f'{word3} and {word1}',word3.similarity(word1))


tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))



sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
    "Hello, there is my car",
    "I\'ve lost my car in my car",
    "I\'d like my boat back",
    "I will name my dog Diana"
    ]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
