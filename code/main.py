
import func
if __name__ == "__main__":
    url = "https://tgstat.ru/channels/search"
    q="" # по ключевому слову
    inAbout="0" # искать в описании
    categories="Блоги" # категория
    countries="Россия" # страна
    languages="" # язык
    channelType = "" # public/private
    isVerified = 0 # верефикация
    participantsCountFrom = "" # подписчики от
    participantsCountTo = "" # подписчики до
    avgReachFrom = "" # охват поста от
    avgReachTo = "" # охват поста до
    avgReach24From = "" # охват поста от (24часа)
    avgReach24To = "" # охват поста до (24часа)
    ciFrom = "" # индекс цитирование от
    ciTo = "" # индекс цитирования до 
    age = "36" # возраст в месяцах
    err = "0", # уровень вовлечённости
    noRedLabel = "1" # без красной таблички
    noScam = "1" # без метки scam
    noDead = "1" # скрывать мертвые
    func.pars_data(url,q,inAbout,categories,countries,languages,
                   channelType,
                   isVerified,
                   participantsCountFrom,
                   participantsCountTo,
                   avgReachFrom,
                   avgReachTo,
                   avgReach24From,
                   avgReach24To,
                   ciFrom,
                   ciTo,
                   age,
                   err,
                   noRedLabel,
                   noScam,
                   noDead,
                   )
