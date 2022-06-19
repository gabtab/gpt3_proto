
import os
import openai


def gpt3_summary(complaints, myapi_keys):
    """pass in the complaint and api key to the model and GTP3 will be called on the script
        this current version does a summary letter of the input in professional language and 
        and returns an email
    Args:
        complaints text: the complaint that was input 
        myapi_keys text: the orangisation and open ai keys

    Returns:
      openai object  : the summarised complaint in letter format and professional language 
      with date creaed and model type
    """
    openai.api_key = myapi_keys['openai']
    openai.organization = myapi_keys['organisation'] 
    openai.Engine.list()
    #start_sequence = "I am acting as an agent for our client who has the following complaint for you: "
    response = openai.Completion.create(
    engine="davinci",
    prompt="A client sent me this complaint:\n\"\"\"\n " +  complaints + "\n\"\"\"\nI want an email in professional language to contact the company on behalf of the client :\n\"\"\"\n",
    
    temperature=0.5,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.2,
    presence_penalty=0,
    stop=["\"\"\""]
    )
    return response


#test= summarise_complaint(complaint, myapi_keys)