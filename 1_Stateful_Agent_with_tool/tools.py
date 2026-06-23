# 1. Define a list of callable tools for the model
tools = [
    {
        "type": "function",
        "name": "get_horoscope",
        "description": "Get today's horoscope for an astrological sign.",
        "parameters": {
            "type": "object",
            "properties": {
                "sign": {
                    "type": "string",
                    "description": "An astrological sign like Taurus or Aquarius",
                },
            },
            "required": ["sign"],
        },
    },
]



def get_horoscope(sign):
    sign = sign.lower()
    if sign == "aries":
        return f"{sign}: Today is a great day to start a new hobby. Maybe knitting? Just don't knit your fingers together!"
    elif sign == "taurus":
        return f"{sign}: You might find a surprise in your mailbox today. Hopefully, it's not a bill!"
    elif sign == "gemini":
        return f"{sign}: Your dual nature will shine today. Just don't argue with yourself too much!"
    elif sign == "cancer":
        return f"{sign}: Emotions may run high today. Remember, it's okay to cry... just not in the grocery store."
    elif sign == "leo":
        return f"{sign}: Your confidence will be contagious today. Just don't roar too loudly in the office!"
    elif sign == "virgo":
        return f"{sign}: Organization is key today. Just don't alphabetize your cereal boxes!"
    elif sign == "libra":
        return f"{sign}: Balance is important today. Just don't try to balance on one foot while making coffee!"
    elif sign == "scorpio":
        return f"{sign}: Your intensity will be felt today. Just don't stare too long at your reflection in the mirror!"
    elif sign == "sagittarius":
        return f"{sign}: Adventure awaits you today. Just don't try to ride a wild horse to work!"
    elif sign == "capricorn":
        return f"{sign}: Hard work pays off today. Just don't try to climb a mountain in your office chair!"
    elif sign == "aquarius":
        return f"{sign}: Innovation is your friend today. Just don't try to invent a new type of spaghetti!"
    elif sign == "pisces":
        return f"{sign}: Your creativity will flow today. Just don't try to paint with your toes!"
    else:
        return f"This sign is not recognized. Please enter a valid zodiac sign."