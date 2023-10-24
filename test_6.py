def message_lenght(text):
    if len(text) <= 160:
        return text
    return text[:160]

text = input()
print(message_lenght(text))

