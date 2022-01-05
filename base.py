
#Windowsの場合、下記リンクにアクセス、『Download Python』の黄色のボタンをクリックして、Windows64bit版をDL、実行ファイル形式なのでダブルクリックして実行する。
#https://www.python.org/downloads/



#PythonのHelloWorld
print("HelloWorld")

"""
実行する時は、Pythonを書いたファイルを保存し、Pycharmのターミナルから

python [ファイル名]

とする。

ちなみに、LinuxやMacOSの場合、python3 [ファイル名] とする場合もある。これはpython 2.x系を python コマンド、 python3.x系を python3 とする名残りがあるから。
教科書によってはpython3としている場合があるが、これは適宜pythonと解釈して実行する。
"""


#変数の定義

"""
変数はデータを保存する箱のようなもの。

変数を使って計算処理をすることで、何度もデータを書いたりする必要がなくなる。
計算結果を記録して、次の計算に使うこともできる

数学の方程式とは違って右辺のデータを左辺の変数に代入する。
"""

x = 10
y = 20

z = x + y

print(x)
print(y)
print(z)



# if 文

"""
条件式によって処理を分岐させる事ができる。これがif文

例えば、点数が60点以上であれば合格と出力するのであればこうする
"""

score = 60

if score >= 60:
    print("合格")


"""
上のif文は、60点未満のときは何も表示されない

そのため、条件式に当てはまらなかった場合の処理、elseを書き足す。
"""


if score >= 60:
    print("合格")
else:
    print("不合格")


# for 文

"""
同じ処理を何度も繰り返す場合はfor文が良い。

例えば、以下2つは同じ処理だが、for文で記述したほうが繰り返す回数を指定できるだけでなく、行数の節約もできてコードが見やすくなる。
"""

print("こんにちは")
print("こんにちは")
print("こんにちは")
print("こんにちは")


for i in range(4):
    print("こんにちは")


"""
上記の場合、iには繰り返すたびに0~3の値が入るようになる。

よって下記のような事ができる
"""

for i in range(4):
    print(i+1 , "回目のこんにちは")


"""
リスト型をひとつずつ取り出して表示させることができる
"""

students    = [ "Bob","Mike","Tom" ]

for student in students:
    print(student)


