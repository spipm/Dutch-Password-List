
api_id = "" # insert app id
api_secret = "" # insert app secret

import os
import openai
openai.api_key = api_secret

# open saying comments from Reddit API
data = open('gezegden.txt','r').read().split("\n")

# empty file
open('gezegden_parsed.txt','w').write('')

for line in data:
  print("parsing: " + line)

  completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
      {"role": "system", "content": "Je bent een assistent die Reddit comments parsed om spreekwoorden en gezegden te herkennen. Vind de spreekwoorden en gezegden in een commentaar en geef deze terug. Geef de spreekwoorden en gezegden terug in losse zinnen op nieuwe regels. Bedenk zelf geen nieuwe spreekwoorden. Haal quotes weg en verdere uitleg is niet nodig. Nummer de zinnen niet en haal ook spelfouten uit de zinnen."},
      {"role": "user", "content": line}
    ]
  )
  parsed = completion.choices[0].message["content"]
  with open('gezegden_parsed.txt','a') as fout:
    print("\tparsed: " + parsed)
    fout.write(parsed + "\n")

print()