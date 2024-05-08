from openai import OpenAI

client = OpenAI("my key")

def roep_openai_aan(temp, tekst, taal):
    maximaal_tokens = 1000

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Je bent een taaldeskundige"},
            {"role": "user", "content": "Vertaal de tekts: " + tekst + " naar het " + taal}
        ],
    max_tokens=maximaal_tokens,
    temperature=temp
    )

    return completion.choices[0].message.content.strip()

vertaal = input("Wat wil je vertalen? ")

welkeTaal = input("Naar welke taal? ")

vertaling = roep_openai_aan(0.0, vertaal, welkeTaal)

print (vertaling)
