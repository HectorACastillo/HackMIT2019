def parse_label(text):
    text = text.replace(" ","").split('"classes":[')[1]
    text = text[:text.find("]")].replace("\n","")
    classes = text.split("},{")
    scores = []
    for c in classes:
        scores.append(float(reference(c,'score')))
    i = scores.index(max(scores))
    return reference(classes[i],'class')
    
def reference(dic, key):
    i = dic.find('"'+key+'":')+len(key)+3
    return dic[i:dic.find(',',i)]
