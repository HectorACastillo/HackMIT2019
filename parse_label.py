import json

def parse_label(text):
    '''
    INPUT:  text - string in json formatt containing output from classifier to be parsed
    OUTPUT: a label as a python string
    '''
    parsed_text = json.loads(text)
    classes = parsed_text["images"][0]["classifiers"][0]["classes"]

    # iterate through labels and determine label with the highest score
    scores = []
    for c in classes:
        d = get_depth(c)
        # reference the score provided by the classifier and apply hierarchy depth filter
        scores.append(float(c['score'])*(d/(d+1)))
    i = scores.index(max(scores))
    return classes[i]['class']

def get_depth(dic):
    '''
    INPUT:  dic - a json dictionary for a particular label class
    OUTPUT: the number of levels in the type hiearchy 
    '''
    if 'type_hierarcy' in dic:
        return dic['type_hierarcy'].count('/')
    return 1
