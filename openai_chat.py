# Imports the os module.
import os

# Imports the OpenAI library
import openai

# Sets the OpenAI API key via the environment variable, OPENAI_API_KEY (which I deleted).
openai.api_key = os.getenv("OPENAI_API_KEY")

# A while loop that runs until the user enters "exit."
while True:
  
  # Input from the user (blue text)
  question = input("\033[34mWhat is your question?\n\033[0m")
  
  # Checks to see if user entered exit"
  if question.lower() == "exit":
    
    # Breaks the loop, prints a goodbye (red text)
    print("\033[31mGoodbye for now!\033[0m")
    break
  
  # Uses the openai.ChatCompletion.create() method to generate a response to user question
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", # Uses the 'gpt-3.5-turbo' model
    messages=[
      {"role": "system", "content": "You are a helpful assistant. Answer the given question."}, # Instructs the AI with a system message
      {"role": "user", "content": question} # Uses the user's question as input
    ]
  )
  
  # Prints AI generated response (green text)
  print("\033[32m" + completion.choices[0].message.content + "\n")

