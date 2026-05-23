from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def semantic_score(reference, learner_answer):

    reference_embedding = model.encode([reference])

    learner_embedding = model.encode([learner_answer])

    similarity = cosine_similarity(
        reference_embedding,
        learner_embedding
    )[0][0]

    return float(similarity)