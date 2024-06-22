questions = ["Q) Which planet is known as red planets?", "Q) What is the strongest muscle in human body?", "Q) How many bones are in adult human body?", "Q) What is the largest country in the world by area?", "Q) What is the loudest animal in the world?", "Q) What is the smallest country in the world?", "Q) Which fruit is most popular and consumed worldwide?", "Q) What is the capital of Australia?"]

answers = ["mars", "toungue", "206", "russia", "blue whale", "vatican city", "tomato", "canberra"]

price = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]
print(len(price))

total = 0

for i in range(len(questions)):
    print(questions[i])
    ans = input()
    if (ans == answers[i]):
        total = total + price[i]
    else:
        total = total + 0

if(total > 10000000):
    print("You became crorepati !!!!!!!")
else:
    print("You won",total,"money, thankyou for your participation")

