import openai

# Ganti dengan API key-mu
openai.api_key = " masukkan API Key OpenAI nya "

def test_openai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # atau model lain yang kamu inginkan
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=255,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        
        return response['choices'][0]['message']['content'].strip()  # Mengembalikan respon
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    user_prompt = input("Masukkan prompt untuk diuji: ")
    result = test_openai(user_prompt)
    print("Respon dari OpenAI:")
    print(result)
