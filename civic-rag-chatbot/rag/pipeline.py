from rag.retriever import get_docs
from rag.generator import generate_answer
import traceback

def run_pipeline(query):
    try:
        print("QUERY:", query)

        docs = get_docs(query)
        print("DOCS:", docs)

        if not docs:
            return "No relevant civic data found in the database."

        answer = generate_answer(query, docs)
        print("ANSWER:", answer)

        return answer

    except Exception as e:
        print("\n FULL PIPELINE ERROR:")
        traceback.print_exc()   # THIS IS KEY

        return "System error while processing your request."