def sentence_maker(phrase):
    interrogatives = ("how", "why", "what")
    capitalize = phrase.capitalize()
    if phrase startswith(interrogatives):
        return "{}?".format(capitalize)
    else:
        return "{}.".format(capitalize)


results = []
while True:
    username = input("Say something: ")
    if username == "\end":
        break
    else:
        results.append(sentence_maker(username))

print(" ".join(results))
