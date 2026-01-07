from src.states.retrieval.reranker import RerankerIn, RerankerOut

def reranker(state : RerankerIn) -> RerankerOut:
    """
    Reranker Node
    This node Reranks the Retrieved Documents using some Deterministic approach
    """ 
    MAX_CHUNKS = 20

    reranked_documents : RerankerOut = {
        "reranked_documents" : []
    } 
    
    retrieved_documents = state["retrieved_documents"]
    query_label = state["query_label"]
    user_query = state["user_query"]
    translated_query = state["translated_query"]

    scored_docs = []

    for doc in retrieved_documents:
        score = 0

        financial_type = doc["financial_type"] 

        if financial_type == query_label:
            score += 40
        elif financial_type == "other":
            score -= 40

        if financial_type == "financial_fact":
            num_count = count_numbers(doc["content"])
            score += min(num_count * 4, 20)

        if 80 <= len(doc["content"]) <= 450:
            score += 10

        if token_match(user_query,translated_query,doc["content"]):
            score += 20

        scored_docs.append((score, doc))
    
    scored_docs.sort(reverse=True, key=lambda x : x[0])

    for doc in scored_docs[:MAX_CHUNKS]:
        reranked_documents["reranked_documents"].append(doc[1])

    return reranked_documents 

def count_numbers(text: str) -> int:
    count = 0

    tokens = text.replace(",", "").split()

    for tok in tokens:
        clean = tok.strip("₹$€£()%")

        clean = clean.replace("crore", "").replace("cr", "")
        clean = clean.replace("lakh", "").replace("mn", "")
        clean = clean.replace("million", "").replace("bn", "")
        clean = clean.replace("billion", "")

        try:
            float(clean)
            count += 1
        except:
            continue

    return count

STOPWORDS = {
    "what", "is", "are", "the", "of", "in", "for", "to", "and", "on",
    "show", "give", "tell", "me", "please", "how", "much"
}

def token_match(user_query: str, translated_query: str, text: str) -> bool:
    text_lower = text.lower()

    def important_tokens(q: str) -> set[str]:
        return {
            w for w in q.lower().split()
            if len(w) > 2 and w not in STOPWORDS
        }

    uq_tokens = important_tokens(user_query)
    tq_tokens = important_tokens(translated_query)

    all_tokens = uq_tokens | tq_tokens

    if not all_tokens:
        return False

    matched = sum(1 for t in all_tokens if t in text_lower)

    return (matched / len(all_tokens)) >= 0.5
