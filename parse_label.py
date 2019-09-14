def parse_label(text):
    text = text.replace(" ","").split('"classes":[')[1]
    text = text[:text.find("]")].replace("\n","")
    classes = text.split("},{")
    scores = []
    for c in classes:
        d = get_depth(c)
        scores.append(float(reference(c,'score'))*(d/(d+1)))
    i = scores.index(max(scores))
    return reference(classes[i],'class')
    
def reference(dic, key):
    i = dic.find('"'+key+'":')+len(key)+3
    return dic[i:dic.find(',',i)]

def get_depth(dic):
    if 'type_hierarcy' in dic:
        return reference(dic, 'type_hierarcy').count('/')
    return 1

text = '''
{
    "images": [
        {
            "classifiers": [
                {
                    "classifier_id": "default",
                    "name": "default",
                    "classes": [
                        {
                            "class": "circuit board",
                            "score": 0.578,
                            "type_hierarchy": "/electrical device/computer circuit/circuit board"
                        },
                        {
                            "class": "computer circuit",
                            "score": 0.755
                        },
                        {
                            "class": "electrical device",
                            "score": 0.757
                        },
                        {
                            "class": "disk controller",
                            "score": 0.553,
                            "type_hierarchy": "/controller/disk controller"
                        },
                        {
                            "class": "controller",
                            "score": 0.558
                        },
                        {
                            "class": "central processing unit",
                            "score": 0.535
                        },
                        {
                            "class": "PC board",
                            "score": 0.501,
                            "type_hierarchy": "/electrical device/computer circuit/PC board"
                        },
                        {
                            "class": "CPU board",
                            "score": 0.5,
                            "type_hierarchy": "/electrical device/computer circuit/CPU board"
                        },
                        {
                            "class": "electronic equipment",
                            "score": 0.6
                        },
                        {
                            "class": "memory device",
                            "score": 0.599
                        },
                        {
                            "class": "microchip",
                            "score": 0.592
                        },
                        {
                            "class": "jade green color",
                            "score": 0.838
                        },
                        {
                            "class": "emerald color",
                            "score": 0.787
                        }
                    ]
                }
            ],
            "source_url": "https://watson-developer-cloud.github.io/doc-tutorial-downloads/visual-recognition/640px-IBM_VGA_90X8941_on_PS55.jpg",
            "resolved_url": "https://watson-developer-cloud.github.io/doc-tutorial-downloads/visual-recognition/640px-IBM_VGA_90X8941_on_PS55.jpg"
        }
    ],
    "images_processed": 1,
    "custom_classes": 0
}
'''
print parse_label(text)
