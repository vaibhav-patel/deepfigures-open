import json
filename = 'simdoc--topic-sequence-alignment-based-document-similarity-framework.pdf'
dir1 = '0ed03a6b9501b938a80ff2bc59bae3e6ea0a75c7/'
pages_path = dir1 + 'ghostscript/dpi200/'
pdffigures = dir1 + 'pdffigures/' + filename[:-4] + '.json'


with open(pdffigures, 'r') as f:
    imagesObjects = json.loads(f.read())
'''
"figType": "Table",
    "imageText": ["SimDoc", "72.69%", "Document", "embedding", "with", "paragraph", "vectors", "70.88%", "Okapi", "BM25", "over", "Bag", "Of", "Words", "59.08%", "Lucene", "index", "over", "Bag", "Of", "Word", "59.86%", "Jaccard", "index", "over", "Bag", "Of", "Word", "66.02%", "System", "Accuracy"],
    "name": "1",
    "page": 5,
    "regionBoundary": {
      "x1": 328.0,
      "x2": 549.0,
      "y1": 106.0,
      "y2": 193.0
    }
'''
x1 = int( 328.0 *100/72)
x2 = int( 549.0*100/72)
y3 = int( 106.0*100/72)
y4 = int( 193.0*100/72)
# x1 = int(328.0)
# x2 = int(549.0)
# y3 = int(106.0)
# y4 = int(193.0)
from PIL import Image
x = Image.open('/Users/vaibhav/Rax/deepfigures-open/0ed03a6b9501b938a80ff2bc59bae3e6ea0a75c7/ghostscript/ghostscript/dpi100/simdoc--topic-sequence-alignment-based-document-similarity-framework.pdf-dpi100-page0006.png')
print(x.size)
box = (x1, y3, x2, y4)
print(box)
a = x.crop(box)
a.show()



