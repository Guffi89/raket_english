# Задаю класс для моего приложения для изучения английских слов.

class RaketEnglish:

    USER_INFO = {
        'login': "user_name",
        'email': "example@same.com",
        'password': 'qwerty'
    }

    TOPIC_LIST = ("airport", "animals", "beginner", "berries", "body-parts", "clothes", "colors", "diseases",
                  "drug-names", "emotions-and-feelings", "english-words-drink", "englishwords-similer-torussian",
                  "family", "fish", "ferquently-used-verbs", "halloween", "hobby", "house",
                  "kitchen", "meal", "months", "new-year", "professions", "school-subjects", "seasons", "sport",
                  "summer", "tastes", "travel", "vegetables", "weather", "weekday", "words-city", "work")

    CAUNTER_WORD = 10

    def __init__(self, USER_INFO, TOPIC_LIST, CAUNTER_WORD):
        self.USER_INFO = USER_INFO
        self.TOPIC_LIST = TOPIC_LIST
        self.CAUNTER_WORD = CAUNTER_WORD
