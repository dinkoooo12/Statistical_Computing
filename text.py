text = "Artificial intelligence is transforming many sectors around the world. It improves efficiency by automating repetitive tasks. Businesses use AI to analyze large amounts of data quickly. Healthcare professionals apply AI tools to support diagnosis and treatment decisions. Education also benefits through personalized learning systems. Transportation is becoming safer with AI-powered navigation. Communication has improved with smart assistants and chatbots. Researchers continue to discover new applications every year. Governments are creating policies to guide responsible AI use. Overall, AI is becoming an essential part of modern life."
text = text.replace(",", "").replace(".", "").lower()
word_list = text.split()
#unique_word =set(word_list)
word_count = {}
for word in word_list:
   # word = word.lower()
    if word in word_count:
        # word_count[word] =word_count[word] + 1
        word_count[word] += 1
    else:
        word_count[word] = 1
for word, num in word_count.items():
    print(f"'{word}': {num}")  

# for file
to_file = open("word-count.csv",'a',encoding="utf-8") # a-append to adding on existing
to_file.write("Words,Frequency")

# for stat in word_count:
#     print(stat,word_count[stat])

to_file.write(word+ ","+str(word_count)+"\n")
to_file.close()

reader =open("word-count.csv","r")
line_list =reader.read().split("\n")
print(line_list)
reader.close()


