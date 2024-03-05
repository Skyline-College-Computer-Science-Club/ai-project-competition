import openai

# For more assistance, and the rest of the OpenAI documentation go to:
# https://platform.openai.com/docs/overview

# [REQUIRED] This is where the API key goes
# You can find it in the overview Google doc (go back into our announcements and scroll up)
# Make sure that the API key is still a string
openai.api_key = 'Replace this text with the API key'


# If you want to skip the documentation, a comment free version of this template is at the bottom


# completion is an OpenAI Chat Completions object, with the descriptors and attributes that
# you can change
completion = openai.chat.completions.create(
    model='gpt-3.5-turbo-0125', # This is the recommended (best and most cost efficient) 
                                # model to use. But if you do wish to change it, go to 
                                # https://openai.com/pricing to see the other models, with
                                # their pricing, and model codes (REMEMBER CREDITS ARE SHARED
                                # WITH THE ENTIRE CLUB)
                                # Note: the only model codes that work here look like the default
                                # one (with the dashes etc)
    messages=[
        # Messages constitutes the main input that you will be changing. It must be an array of
        # message object, denoted by {} and separated by commas. The message objects must always be
        # made up of a key-value pair of 'role', and 'content'. 'role' must always be 'system', 'user'
        # or 'assistant'. 'content' is what is associated/is input into those respective roles


        {'role': 'system', 'content': ''},
        # Content that goes into the system role sets the behavior of the generation. Basically it sets
        # the personality, or guidelines about what type of output it should be generating

        {'role': 'user', 'content': ''},
        # User will be variable input from you, or the user of your app/program. Someone was using ChatGPT
        # for something, that person is the user.

        {'role': 'assistant', 'content': ''}
        # This is the response in the history of the assistant. In ChatGPT, this would be like the previous
        # generated messages from the AI. It can be used to help determine how output is formatted. 
    ],
    #temperature = 1,
    # Temperature controls the randomness and how determined the output is. It is a range from 0-2, with
    # 0 being the least random and 2 the most. It is optional and defaulted to 1. Uncomment it and add a value
    # if you wish to use it

    #max_tokens = 100,
    # Sets the maximum amount of tokens allowed for generation. Remember 1000 tokens = ~750 words. This is
    # optional, but recommended
)

print(completion.choices[0].message.content)
# Getting the response from the above generation object. The format is: object_name.choices[0].message.content
# It returns a string type, so you don't just need to print it, and could do some other string stuff to it





completion = openai.chat.completions.create(
    model='gpt-3.5-turbo-0125',
    messages=[
        {'role': 'system', 'content': ''},
        {'role': 'assistant', 'content': ''},
        {'role': 'user', 'content': ''}
    ],
    temperature = 1,
    max_tokens = 75
)