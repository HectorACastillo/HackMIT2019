def parse_label(text):
    '''
    INPUT:  text - string containing output from classifier to be parsed
    OUTPUT: a label as a python string
    '''

    # format the string for parsing
    text = text.replace(" ","").split('"classes":[')[1]
    text = text[:text.find("]")].replace("\n","")
    labels = text.split("},{")

    # iterate through labels and determine label with the highest score
    scores = []
    for label in labels:
        d = get_depth(label)
        # reference the score provided by the classifier and apply hierarchy depth filter
        scores.append(float(reference(label,'score'))*(d/(d+1)))
    i = scores.index(max(scores))
    return reference(labels[i],'class')
    

def reference(dic, key):
    '''
    INPUT:  dic - string containing a "dictionary" with keys: label, score, and type hierarchy
            key - key for desired value
    OUTPUT: the value associated with key
    '''
    i = dic.find('"'+key+'":')+len(key)+3
    return dic[i:dic.find(',',i)].replace('"','')

def get_depth(dic):
    '''
    INPUT:  dic - string containing a "dictionary" with keys: label, score, and type hierarchy
    OUTPUT: the number of levels in the type hiearchy 
    '''
    if 'type_hierarcy' in dic:
        return reference(dic, 'type_hierarcy').count('/')
    return 1
