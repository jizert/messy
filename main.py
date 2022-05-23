from chatterbot import ChatBot
from chatterbot.conversation import Statement

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

bot = ChatBot(
    'mEssy',
    storage_adapter='chatterbot.storage.SQLStorageAdapter'
)


def get_feedback():

    text = input()

    if 'yes' in text.lower():
        return True
    elif 'no' in text.lower():
        return False
    else:
        print('Please type either "Yes" or "No"')
        return get_feedback()


print('Type something to begin...')

while True:
    try:
        input_statement = Statement(text=input())
        response = bot.generate_response(
            input_statement
        )

        print('\n Is "{}" a coherent response to "{}"? \n'.format(
            response.text,
            input_statement.text
        ))
        if get_feedback() is False:
            print('WHICH ONE TRUE!!?!?')
            correct_response = Statement(text=input())
            bot.learn_response(correct_response, input_statement)
            print('MESSY HAS LEARNED!')

    except (KeyboardInterrupt, EOFError, SystemExit):
        break
