from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def generate_answer(query, docs):
    try:
        print("🔵 GENERATOR INPUT:")
        print("QUERY:", query)

        context = "\n".join([d.page_content for d in docs])
        print("🟡 CONTEXT READY")

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful civic assistant for Pakistani citizens. Answer questions using only the provided context."
                },
                {
                    "role": "user",
                    "content": f"Context:\n{context}\n\nQuestion: {query}"
                }
            ],
            max_tokens=1024,
            temperature=0.7
        )

        answer = response.choices[0].message.content
        print("🟢 RESPONSE:", answer)
        return answer

    except Exception as e:
        import traceback
        print("\n🔥 GENERATOR ERROR:")
        traceback.print_exc()
        return "GENERATOR FAILED"