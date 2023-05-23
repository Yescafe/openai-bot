import openai
import secret_tokens

openai.api_key = secret_tokens.OPENAI_API_KEY

def get_completion(prompt, model="gpt-3.5-turbo", temperature=1):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

if __name__ == '__main__':
    print(get_completion('请问我应该为猫咪生产做些什么'))

