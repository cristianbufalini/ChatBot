import openai

openai.api_key = "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"

conversation = ""

i = 1

while (i != 0):
    question = input("Humano")
    
    conversation += "/nHumano: " + question +"/nAI: "   
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=conversation,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Humano:", " AI:"]
)
    
    anwer = response.choices[0].text.strip()
    
    conversation += anwer
    
    print("AI: " + anwer + "/n")
    