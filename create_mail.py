import sys
import os
from openai import OpenAI

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
)

# In the end I maybe won't use chatGPT as it is not free.
# Instead I will use a google link for the definition and translation.
def query_chatgpt(prompt):
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        model="gpt-3.5-turbo",
    )
    return response['choices'][0]['message']['content']

def word_mail(voc):
    content = "This mail stems from the [obsidian_vocabulary](https://github.com/artainmo/obsidian_vocabulary) project.\n\n"
    content += f"The word of the day is '[{voc}](https://www.google.com/search?q={voc}+definition+and+translation+french+english)'.\n\n"
    #content += query_chatgpt(f"The following word may be in French or English. The word is: '{voc}'. If in French provide its definition and an example use case in French, also give an English translation. If in English provide its definition and an example use case in English, also give a French translation.")
    return content

def expression_mail(voc):
    content = "This mail stems from the [obsidian_vocabulary](https://github.com/artainmo/obsidian_vocabulary) project.\n\n"
    content += f"The expression of the day is '[{voc}](https://www.google.com/search?q={voc.replace(' ', '+')}+definition+and+translation+fench+english)'.\n\n"
    return content


def is_word(voc):
    # Strip any leading/trailing whitespace and split the string by spaces
    words = voc.strip().split()
    # Check if the input contains more than one word
    if len(words) == 1:
        return True
    else:
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_string>")
        sys.exit(1)
    voc = sys.argv[1].lower()
    if is_word(voc):
        content = word_mail(voc)
    else:
        content = expression_mail(voc)
    with open("mail.md", "w") as fd:
        fd.write(content)
