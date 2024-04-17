text= "*"*300

q_size = 20
if len(text) > q_size:
    parts = list()
    start=0
    end = q_size
    while start < len(text):
        parts.append(text[start:end])
        start += q_size
        end += q_size
    text = "\n".join(parts)

print(text)