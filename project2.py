import telebot
import random
from telebot import types
import requests
print("salam")
bot = telebot.TeleBot("6203741928:AAEQ9FykRyvZyEdJBAAnml8JAwXZfkVV4Mg")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Greeting")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Hello! I am your bot assistant!🤗", reply_markup=markup)
  
@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Hello':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Do you want to pay for your electricity?')
        btn2 = types.KeyboardButton('')
        btn3 = types.KeyboardButton('')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Ask your question', reply_markup=markup) #ответ бота


    elif message.text == 'Do you want to pay for your electricity?':
        for i in range(5):
            rnum = randrange(1001)
            l.append(rnum)
        bot.send_message(message.from_user.id, 'Okay,please enter your full name\n Please, enter your address\n' + 'You have an outstanding balance = )' + l, parse_mode='Markdown')

        bot.send_message(message.from_user.id, 'Are in a position to make that payment today\n',reply_markup=markup)

        bot.send_message(message.from_user.id, 'Do you want to pay by card or in a bank?',reply_markup=markup) 
 
    if message.text == 'card':
    # define payment function
        def make_payment(amount, card_number, card_expiry, cvv):
    # create payment data payload
            payment_data = {
        "amount": amount,
        "card_number": card_number,
        "card_expiry": card_expiry,
        "cvv": cvv
    }
    
    # send payment request to payment gateway API
    response = requests.post(PAYMENT_API_ENDPOINT, data=payment_data)
    
    # check payment status
    if response.status_code == 200 and response.json()["status"] == "success":
        return True
    else:
        return False

# run the payment bot
def payment_bot():
    while True:
        # get payment details from user
        amount = input("Enter payment amount: ")
        card_number = input("Enter card number: ")
        card_expiry = input("Enter card expiry (MM/YY): ")
        cvv = input("Enter CVV: ")
        
        # process payment
        if make_payment(amount, card_number, card_expiry, cvv):
            bot.send_message(message.from_user.id,'Payment successful!')
        else:
            bot.send_message(message.from_user.id,'Payment failed. Please try again.')
        
        # ask if user wants to make another payment
    again = input("Do you want to make another payment? (Y/N): ")
    if again.lower() != "y": break
    bot.send_message(message.from_user.id,'Thank you for your payment,goodbye!')
   
    
    
    if message.text == 'bank':
        bot.send_message(message.from_user.id,'Okay,remember that you should pay the full payment before the next billing.Thank you for using our application,goodbye!',reply_markup=markup)
    
    elif message.text == 'No':
        bot.send_message(message.from_user.id,'Sorry this system all about communal,goodbye!🤗',reply_markup=markup)
  
    if user_input.lower() == 'goodbye' or  user_input.lower() == 'bye':
         bot.send_message(message.from_user.id,'Goodbye!🤗')
        
    bot.polling(none_stop=True, interval=0)