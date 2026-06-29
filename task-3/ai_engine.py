from openai import OpenAI

client = OpenAI(api_key="Your_Open_API_Key")

def ask_ai(question):

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": question}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI Error: {str(e)}"