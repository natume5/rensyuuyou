# 関数の引数の値をキーワード引数で渡す
def price(adult, child):
    return(adult * 1200) + (child * 500)

print(price(adult=1, child=2))
print(price(child=2, adult=1))    # 順番が違ってもいい
