import openai
openai.api_key="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"
while True:
       model_engine="text-davinci-003"
       prompt=input("bir şeyler giriniz:")
       if 'exit' in prompt or "quit" in prompt:
           break
       completion=openai.Completion.create(

           engine=model_engine,
           prompt=prompt,
           max_tokens=1024,
           n=1,
           stop=None,
       )
       response=completion.choices[0].text
       print(response)