# Дана строка, она состоит только из букв английского алфавита.
# Первый участник пишет сбор статистики - какие буквы сколько раз встречаются.
# Второй участник клонирует к себе репозиторий и пишет вывод на экран самой часто встречающейся буквы
#(без использования функций max, sorted и т.д.)
# Изменения производить в своей ветке!
# Загружать на github свою ветку!
# Первый участник скачивает к себе ветку с изменениями, проверяет код, соединяет ветки, снова кладет на github.

def getAllStatistic(str_data):
    """Собирает статистику по количеству букв в строке"""
    stat = {}
    for item in str_data:
        temp = item.upper()
        if(stat.get(temp)):
            stat[temp] += 1
        else:
            stat[temp] = 1
    return stat

def printStatistic(caption, stat):
    """Печатает список статистики"""
    print(caption)
    for item in stat:
        print(item + item.lower(), ":", stat[item], "шт")

def getFrequentChar(stat):
    """Создает список самых популярных букв"""
    res = {}
#Здесь надо дописать код:
#       из полной статистики выбрать самые популярные символы (может быть и не один) 
    return res

def excercise():
    """Основная функция"""
    str_data = "aPsldhgfApyupIIyRmkRrpo weryunRweLp"
    statistic = getAllStatistic(str_data)
    char_frequent = getFrequentChar(statistic)                
    print("Строка:", str_data)
    printStatistic("Статистика строки:", statistic)
    printStatistic("Самая популярная буква:", char_frequent)
    
excercise()