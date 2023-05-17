#  https://pypi.org/project/pyttsx4/                      pyttsx3
#import pyttsx3

gap = pyttsx3.init()
gap.say(" asalomu alaykum! hammangizga ")
gap.say("meneg ismim jarvins 2..0")
gap.runAndWait()



gap = pyttsx3.init()
gap.say(input("kimligingiz haqida malumot bering"))
gap.runAndWait()
print(gap)



uz  # kiritilgan textlarni avudio tarzida o'qiydi 
ru  # читает ввод текста в аудиоформате
us  # reads the entered texts in audio format

uz  # muamolar bor yuq emas bu uzbek tilida, yaxshi ishlan magan ovozda kamchilik lar mavjud
ru  # В узбекском есть огрехи в голосе, который плохо проработан
us  # there are mistakes in the Uzbek language, there are defects in the poorly processed voice
