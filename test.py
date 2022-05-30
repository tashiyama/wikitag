import wikipedia

wikipedia.set_lang("ja")

result = wikipedia.page("銀魂")

print(result.summary)