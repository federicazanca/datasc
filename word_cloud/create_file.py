import json
from pathlib import Path

path = "/home/federica/data_for_words_cloud/result.json"
loaded_texts = json.load(open(path))

#create file with everything
text_list = []
for i in range(len(loaded_texts['messages'])):
    if isinstance(loaded_texts["messages"][i]["text"], list):
            for element in loaded_texts["messages"][i]["text"]:
                if isinstance(element, dict) and 'text' in element:
                    text_list.append(element["text"])
    else:
        text_list.append(loaded_texts["messages"][i]["text"])

if Path("/home/federica/data_for_words_cloud/word_file.txt").exists:
    print("file word_file already exists")
else:
    with open("/home/federica/data_for_words_cloud/word_file.txt", "a") as file:
        for line in text_list:
            file.write(line)
            file.write(" ")

federica_list = []
Angelo_list = []
for i in range(len(loaded_texts['messages'])):
    if 'from_id' in loaded_texts["messages"][i] and "user441702832" in loaded_texts["messages"][i]['from_id']:
            print(loaded_texts["messages"][i])
            if isinstance(loaded_texts["messages"][i]["text"], list):
                for element in loaded_texts["messages"][i]["text"]:
                    if isinstance(element, dict) and 'text' in element:
                        federica_list.append(element["text"])
            else:
                federica_list.append(loaded_texts["messages"][i]["text"])
                
    if 'from_id' in loaded_texts["messages"][i] and "user24274795" in loaded_texts["messages"][i]['from_id']:
        if isinstance(loaded_texts["messages"][i]["text"], list):
            for element in loaded_texts["messages"][i]["text"]:
                if isinstance(element, dict) and 'text' in element:
                    Angelo_list.append(element["text"])
        else:
            Angelo_list.append(loaded_texts["messages"][i]["text"])


    