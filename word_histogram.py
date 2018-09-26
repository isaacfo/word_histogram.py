histogram = {}

sentence= ""

while sentence ==  "":
    sentence = input('Please enter a sentence: ').split()
    if sentence == "":
        print('ok for reals enter a sentence... ', end='')



for word in sentence:
    if word.lower() in histogram:
        histogram[word.lower()] +=1
    else:
        histogram[word.lower()] = 1

print(histogram)