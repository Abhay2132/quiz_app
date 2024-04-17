text = "Abhay is Great"*2

def limit_line_length(text, limit):
    words = list(text.split(" "))
    para = list()
    line = ""
    for i,word in enumerate(words):
        if i < len(words)-1:
            word+=" "
        newline = line + word
        if len(newline) > limit:
            # line = line+"\n"+word
            para.append(line)
            line = word
        else:
            line = newline
    para.append(line)
    return "\n".join(para)
    

print(text)
print(limit_line_length(text, 20))



