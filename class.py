# クラスの定義
class Dog:
    # 属性（変数）を持つ
    def __init__(self, name, age):
        self.name = name  # 犬の名前
        self.age = age    # 犬の年齢
        self.gender = "male"

    # メソッド（関数）を持つ
    def bark(self):
        print(f"{self.name}はワンワンと鳴いています！")

    def get_older(self):
        self.age += 1
        print(f"{self.name}は今、{self.age}歳です。")

    def walk(self):
        print(f"{self.name}は歩いています")

# オブジェクトの作成
my_dog = Dog("ポチ", 3)
your_dog = Dog("タマ", 8)

# 属性（値）へのアクセス
print(my_dog.name)  # ポチ
print(my_dog.age)   # 3
print(my_dog.gender)

# メソッド（処理）の呼び出し
my_dog.bark()       # ポチはワンワンと鳴いています！
my_dog.get_older()  # ポチは今、4歳です。
my_dog.walk()

print(your_dog.name)