from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
# documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(common_texts)]
# print(documents)
print(common_texts)

model = Doc2Vec.load("../models/test.model")

x = model.infer_vector(['human', 'interface', 'computer'])

most_similar_texts = model.docvecs.most_similar([x])

for similar_text in most_similar_texts:
    print(similar_text)
