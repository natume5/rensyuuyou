#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- パーセント点の求め方 ---")


"""
データ集合が特定の分布に従うとき、
そのデータの範囲を確率的に評価することが可能となります。
このページでは比較的わかりやすい正規分布でパーセント点の求め方を解説します。
"""


print("--- パーセント点 ---")


"""
冒頭で書いたとおり、正規分布は範囲を確率的に評価することが可能です。
例えば、農園Aのみかんの重量が以下の正規分布に従うことがわかっているとします。

    平均：100g
    標準偏差：5g

この場合、農園Aの適当なみかんはおおよそ95%の確率で92g以上、
108g以下に収まると推定することができます。なぜそんなことがわかるのでしょうか？
まず、この農園のデータ分布は以下のような正規分布のグラフで表すことができます。
横軸は重量gを表します。平均値を釣り鐘の中心として左右対称となっています。
以前説明しましたが、確率密度関数のグラフとX軸に囲まれた部分の面積は
全体の確率1となります。

この関数は積分可能なので任意の範囲の面積、
つまり任意の範囲の確率を求めることが可能です。
例えば、このグラフの面積が0.05となる左側の境界を求めるとおおよそ92gとなります。
（Pythonを利用した計算方法は後述します。）

つまり、92g以下となる確率は5%となります。
このような左側の確率を「下側5%点」と呼びます。
同様に右側の5%となる境界を求めると、108gとなります。
つまり、108g以下となる確率は5%となります。
このような左側の確率を「上側5%点」と呼びます。

上側5%、下側5%で挟まれた部分は残りの90%となるため、
先述の通り農園Aの適当なみかんはおおよそ95%の確率で92g以上、
108g以下に収まると推定することができます。
"""


print("--- パーセント点を求める ---")


"""
パーセント点を求める計算は積分を伴うため難しく、
通常筆算で解く場合はは標準化を行い
予め算出された標準正規分布表から導出することになるのですが、
Pythonを使用すると簡単に値を求めることが可能です。
前回グラフの描画に使用したscipy.statsのnormを使います。

パーセント点
norm.ppf(q=パーセント, loc=平均, scale=標準偏差)

例えば先程の例の平均：100、標準偏差：5の正規分布の左側5%点、
右側5%点を求める場合、以下のようになります。
"""

from scipy.stats import norm

# mean
loc = 100
# standard deviation
scale = 5

p1 = norm.ppf(q=0.05, loc=loc, scale=scale)
p2 = norm.ppf(q=0.95, loc=loc, scale=scale)

print(p1)    # 91.77573186524263
print(p2)    # 108.22426813475737


print("--- ある点が何％点かを求める ---")


"""
また逆に、正規分布を前提としてX軸のある点が何％点となるのか？
を求める場合もあります。例をみてみましょう。
ある工場では製品に品質管理用の製品評価指数を設けており、
この指数は以下の正規分布に従うことがわかっているとします。

    平均：100
    標準偏差：3

この製品評価指数が90を下回る製品は
不良品扱いとして出荷しないことにしました。
不良品が発生する確率は何％になるでしょうか？
前提条件より以下の正規分布グラフとなります。
90より左側の面積を求めることになります。

Pythonで求める場合、scipy.statsのcdfを利用します。

cdf
norm.cdf(x=確率変数, loc=平均, scale=標準偏差)

実際計算を実行してみると、以下のようになります。
"""

from scipy.stats import norm

# mean
loc = 100
# standrd deviation
scale = 3

p = norm.cdf(x=90, loc=loc, scale=scale)
print(p)     # 0.0004290603331968372

"""
計算結果より、不良品扱いとなる製品の割合は
1万個に4つ程度となることがわかりました。
"""


print("--- まとめ ---")


"""
このパーセント点を求める操作が統計学の入門部分の一つの肝で、
ここができれば今後説明する区間推定や帰無仮説検定の理解が
スムーズかと思います。
また、今回は正規分布を利用しましたが、
正規分布以外でもパーセント点を求められる場合が多々ありますので
様々に活用することができるようになるはずです。
"""


print("--- Qiitaより ---")
print("--- 1. Pythonで学ぶ統計学　2. 確率分布[scipy.stats徹底理解] ---")




"""

データから計算される確率分布のことを「経験分布」といいます。
これに対して、確率分布を生成してくれる関数は「理論分布」といいます。
まず、分布の形（確率分布の種類）を決める、
それから母数（確率分布のパラメータ）を決めてしまえば、
母集団分布の推定ができます。
そうした統計関数を集めたモジュールがscipy.statsです。
その基本的な使い方は、次のように記法が統一されています。


⑴ 確率分布の種類

    確率関数は「離散型」と「連続型」の２つに大別されます。
    離散型は、例えばサイコロの目のようにとびとびの値をとる変数です。
    また連続型は、重量や温度のように連続した値をとるものをいいます。
    以下に、scipy.statsに実装されている確率分布から、
    知っておきたい15種類を列挙しました。

確率分布         probability distribution            メソッド    データ
1   超幾何分布    Hypergeometric distribution     scipy.stats.hypergeom   離散型
2   ベルヌーイ分布     Bernoulli distribution        scipy.stats.bernoulli   離散型
3   二項分布      binomial distribution           scipy.stats.binom       離散型
4   ポアソン分布    Poisson distribution            scipy.stats.poisson     離散型
5   幾何分布      Geometric Distribution          scipy.stats.geom        離散型
6   負の二項分布   Negative Binomial Distribution  scipy.stats.nbinom      離散型
7   一様分布      uniform distribution            scipy.stats.uniform     離散型
8   正規分布      normal distribution             scipy.stats.norm        連続型
9   指数分布      exponential distribution        scipy.stats.expon       連続型
10  ガンマ分布     gamma distribution              scipy.stats.gamma       連続型
11  ベータ分布     beta distribution               scipy.stats.betabinom   連続型
12  コーシー分布    Cauchy distribution             scipy.stats.cauchy      連続型
13  対数正規分布  lognormal distribution          scipy.stats.lognorm     連続型
14  パレート分布    Pareto distribution             scipy.stats.pareto      連続型
15  ワイブル分布    Weibull distribution            scipy.stats.dweibull    連続型


これらの確率分布は、ほぼ共通のメソッドを実装しています。
従って、メソッドを理解すれば、いろいろな確率分布を操作することが可能となります。


⑵ 各種メソッドの機能

ここでは、もっとも使用頻度が高い正規分布scipy.stats.normを例として、
主要なメソッドを見ていきます。
引数となるのは、入力データx、パラメータである期待値
（平均値）locと標準偏差scaleのほか、
要素の数size、乱数生成のシードrandom_state=整数などです。

# 数値計算のためのライブラリ
import numpy as np
from scipy import stats

# グラフ描画のためのライブラリ
import matplotlib.pyplot as plt
%matplotlib inline

# matplotlibを日本語表示に対応させるモジュール
!pip install japanize-matplotlib
import japanize_matplotlib
"""

print('➀ rvs (Random variates) 確率変数')
"""
記法：rvs(loc=0, scale=1, size=1, random_state=None)
確率変数は、確率的な法則に従って変化する値のことです。
指定したパラメータに基づいて、正規分布に従う確率変数（取り得る値）を、
ランダムに指定した個数だけ生成します。
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


# rvsで正規分布に従う疑似乱数を生成
norm_rvs = stats.norm.rvs(loc=50, scale=20, size=1000, random_state=0)    # 期待値=50, 標準偏差=20, 個数=1000

# 可視化(ヒストグラムに表現)
plt.hist(norm_rvs, bins=10, alpha=0.3, ec='blue')
plt.xlabel('階級', fontsize=13, fontname="MS Gothic")
plt.ylabel('度数', fontsize=13, fontname="MS Gothic")

plt.show()


print('➁ pdf (Probability density function) 確率密度関数')
"""
記法：pdf(x, loc=0, scale=1)
確率密度は、定義された域内での確率変数Xの値の相対的な出やすさを表します。
平たく言えば、確率密度関数は、
連続型のデータを引数にとると確率密度が算出される関数のことです。
"""

# 等差数列を生成
X = np.arange(start=1, stop=7.1, step=0.1)

# pdfで確率密度関数を生成
norm_pdf = stats.norm.pdf(x=X, loc=4, scale=0.8)    # 期待値=4, 標準偏差=0.8

# 可視化
plt.plot(X, norm_pdf)
plt.xlabel('確率変数X', fontsize=13, fontname="MS Gothic")
plt.ylabel('確率密度pdf', fontsize=13, fontname="MS Gothic")
plt.show()

"""
試みに、確率変数 x=5 のときの確率密度を確認してみます。
"""

# 確率変数5の時の確率密度を計算
x = 5
y = stats.norm.pdf(x=x, loc=4, scale=0.8)    # 期待値=4, 標準偏差=0.8
print('確率変数x=5の時の確率密度:', y)    # 確率変数x=5の時の確率密度: 0.2283113567362774

# 確率密度関数のグラフにプロット
plt.plot(X, norm_pdf)
plt.plot(x, y, 'bo')    # 青色ドットを布置

plt.vlines(x, 0.0, y, lw=2, linestyles='dashed')    # 垂直線
plt.hlines(y, 1.0, x, lw=2, linestyles='dashed')    # 水平線

plt.xlabel('確率変数X', fontsize=13, fontname="MS Gothic")
plt.ylabel('確率密度pdf', fontsize=13, fontname="MS Gothic")

plt.show()

"""
確率密度関数pdfは連続型データのためのメソッドであり、
離散型データには次の確率質量関数pmfを使います。
"""

print('➂ pmf (Probability mass function) 確率質量関数')
"""
記法：pmf(k, n, p, loc=0)
確率質量は、確率変数Xのとびとびの要素ごとの相対的な出やすさを表します。
平たく言えば、確率質量関数は、離散型のデータを引数にとると
確率質量が算出される関数のことです。
ここでは２項分布を例として、
「成功確率40％の試行を５回行ったとき、そのうち成功する回数
（０～４回）ごとの確率」を示します。
"""

# 成功確率
p = 0.4
# 試行回数
n = 5
# 成功回数
k = np.arange(0, 5)    # array([0, 1, 2, 3, 4])

# pmfで成功回数ごとの確率を計算
binom_pmf = stats.binom.pmf(k, n, p)    # 成功回数=0~4, 試行回数=5, 成功確率=0.4

# 可視化
plt.plot(k, binom_pmf, "bo", ms=8)
plt.vlines(k, 0, binom_pmf, colors='b', lw=3, alpha=0.5)

plt.xticks(k)    # x軸目盛

plt.xlabel('確率変数X', fontsize=13, fontname="MS Gothic")
plt.ylabel('確率質量関数pmf', fontsize=13, fontname="MS Gothic")

plt.show()



print('➃ logpdf (Log of the probability density function) ログ確率密度関数')
"""
記法：logpdf(x, loc=0, scale=1)
ログ確率密度関数は、底をeとする確率密度の対数をとったものです。
ネイピア数 $e=2.7182818284 ...$ 
と続く超越数を$a$乗したら確率密度になるときの$a$の値ことです。
式に表すと $e^a=$pdf です。
"""

# 等差数列を生成
X = np.arange(start=1, stop=7.1, step=0.1)

# logpdfで確率密度関数の対数を生成
norm_logpdf = stats.norm.logpdf(x=X, loc=4, scale=0.8)    # 期待値=4, 標準偏差=0.8

# 可視化
plt.plot(X, norm_logpdf)
plt.xlabel('確率変数X', fontsize=13, fontname="MS Gothic")
plt.ylabel('確率質量関数pmf', fontsize=13, fontname="MS Gothic")
plt.show()

"""

試みに、上図で確率密度の対数が最大値を示す確率変数
 x=4 について確認してみます。
手順としては、まず確率変数 x=4 のログ確率密度の値を取得し、
次いで x=4 の確率密度を計算してからその対数をとり、両方を比較します。
"""

# ログ確率密度の最大値を取得
logpdf_max = np.max(norm_logpdf)
print('x=4のログ確率密度:', logpdf_max)    # x=4のログ確率密度: -0.695794981890463

# 確率密度を計算
x = 4
v_pdf = stats.norm.pdf(x=x, loc=4, scale=0.8)    # 期待値=4, 標準偏差=0.8

# 確率密度の対数を計算
v_pdf_log = np.log(v_pdf)
print('x=4の確率密度の対数:', v_pdf_log)    # x=4の確率密度の対数: -0.695794981890463

# 可視化
plt.plot(X, norm_logpdf)
plt.plot(4, logpdf_max, "bo")    # 青色ドットを布置

logpdf_min = np.min(norm_logpdf)    # ログ確率密度の最小値(描画用)
plt.vlines(x, logpdf_max, logpdf_min, lw=2, linestyles='dashed')    # 垂直線
plt.hlines(logpdf_max, 1.0, x, lw=2, linestyles='dashed')    # 水平線

plt.xlabel('確率変数X', fontsize=13, fontname="MS Gothic")
plt.ylabel('ログ確率密度関数logpdf', fontsize=13, fontname="MS Gothic")
plt.show()


print("➄ cdf (Cumulative distribution function) 累積分布関数")
"""
記法：cdf(x, loc=0, scale=1)
累積分布関数は、確率変数$X$がある値$x$以下となる確率を計算します。
例えば、サイコロを投げたときに「出る目が３以下」となる確率は、
１から３までの確率密度をすべて足し合わせたものになります。
"""

# x軸の等差数列を生成
X = np.linspace(start=1, stop=7, num=100)

# cdfで累積分布関数を生成
norm_cdf = stats.norm.cdf(x=X, loc=4, scale=0.8)    # 期待値=4, 標準偏差=0.8

# cdfでx=5以下の累積確率を計算
under_5 = stats.norm.cdf(x=5, loc=4, scale=0.8)    # 期待値=4, 標準偏差=0.8
print('5以下になる確率:', under_5)    # 5以下になる確率: 0.8943502263331446

# 可視化
plt.plot(X, norm_cdf)
plt.plot(5, under_5, "bo")    # 青色ドットを布置

plt.vlines(5, 0.0, under_5, lw=2, linestyles='dashed')    # 垂直線
plt.hlines(under_5, 1.0, 5, lw=2, linestyles='dashed')    # 水平線

plt.xlabel('確率変数X', fontsize=13, fontname="MS Gothic")
plt.ylabel('累積確率密度cdf', fontsize=13, fontname="MS Gothic")
plt.show()



print('sf (Survival function) 生存関数')
"""

記法：sf(x, loc=0, scale=1)
生存関数は、累積分布関数cdfとは逆に、
確率変数$X$がある値$x$以上となる確率を計算します。
｢1-cdf｣ と定義されることもありますが、
sfの方がより正確な場合もあるとの指摘が
scipy.org https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html 
に見られます。
"""

# x軸の等差数列を生成
X = np.linspace(start=1, stop=7, num=100)

# sfで生存関数を生成
norm_sf = stats.norm.sf(x=X, loc=4, scale=0.8)    # 期待値=4, 標準偏差=0.8

# sfでx=5以上の累積確率を計算
upper_5 = stats.norm.sf(x=5, loc=4, scale=0.8)    # 期待値=4, 標準偏差=0.8
print('5以上になる確率:', upper_5)    # 5以上になる確率: 0.10564977366685535

# 可視化
plt.plot(X, norm_sf)
plt.plot(5, upper_5, 'bo')    # 青色ドットを布置

plt.xlabel('確率変数X', fontsize=13, fontname="MS Gothic")
plt.ylabel('生存関数sf', fontsize=13, fontname="MS Gothic")
plt.show()


print('➆ ppf (Percent point function) パーセント点関数')

"""

記法：ppf(q, loc=0, scale=1)
パーセント点関数は、累積分布関数cdfの逆関数で、
累積分布関数をq％と指定するとその値をとる変数を返します。
従って、ppf(0.25)は第１四分位点、
ppf(0.5)は中央値にあたる第２四分位点、
ppf(0.75)は第３四分位点に相当します。
"""

# x軸の等差数列を生成
X = np.arange(start=1, stop=7, step=0.1)

# pdfで確率密度関数を生成
norm_pdf = stats.norm.pdf(x=X, loc=4, scale=0.8)

# pdfで累積分布関数75%に当たる変数を取得
q_75 = stats.norm.ppf(q=0.75, loc=4, scale=0.8)
print('累積分布関数75%点の確率変数:', q_75)    # 累積分布関数75%点の確率変数: 4.539591800156865

# pdfで当該変数の確率密度を取得
v = stats.norm.pdf(x=q_75, loc=4, scale=0.8)
print('累積分布関数75%点の確率密度:', v)    # 累積分布関数75%点の確率密度: 0.39722071585513385

# 可視化
plt.plot(X, norm_pdf)
plt.plot(q_75, v, 'bo')    # 青色ドットを布置

plt.vlines(q_75, 0.0, v, lw=2, linestyles='dashed')    # 垂直線
plt.hlines(v, 1.0, q_75, lw=2, linestyles='dashed')    # 水平線

plt.xlabel('確率変数X', fontsize=13, fontname="MS Gothic")
plt.ylabel('確率密度関数pdf', fontsize=13, fontname="MS Gothic")
plt.show()


print('➇ isf (Inverse survival function) 逆生存関数')

"""

記法：isf(q, loc=0, scale=1)
逆生存関数は、生存関数sfの逆関数ですが、
やることはパーセント点関数ppfと逆のことです。
生存関数の残余をq％と指定するとその値をとる変数を返します。
従って、四分位点はパーセント点関数ppfとは逆になり、
isf(0.25)は第３四分位点、isf(0.5)は同じく第２四分位点、
isf(0.75)は第１四分位点に相当します。
"""

# x軸の等差数列を生成
X = np.arange(start=1, stop=7, step=0.1)

# pdfで確率密度関数を生成
norm_pdf = stats.norm.pdf(x=X, loc=4, scale=0.8)

# isfで逆生存関数25%に当たる変数を取得
q_25 = stats.norm.isf(q=0.25, loc=4, scale=0.8)
print('逆生存関数25%点の確率変動:', q_25)    # 逆生存関数25%点の確率変動: 4.539591800156865

# pdfで当該変数の確率密度を取得
v = stats.norm.pdf(x=q_25, loc=4, scale=0.8)
print('逆生存関数25%点の確率密度:', v)    # 逆生存関数25%点の確率密度: 0.39722071585513385

# 可視化
plt.plot(X, norm_pdf)
plt.plot(q_25, v, 'bo')

plt.vlines(q_25, 0.0, v, lw=2, linestyles='dashed')    # 垂直線
plt.hlines(v, 1.0, q_25, lw=2, linestyles='dashed')    # 水平線

plt.xlabel('確率変数X', fontsize=13, fontname="MS Gothic")
plt.ylabel('確率密度関数pdf', fontsize=13, fontname="MS Gothic")
plt.show()


print('➈ interval (Endpoints of the range that contains alpha percent of the distribution) 区間推定')

"""

記法：interval(alpha, loc=0, scale=1)
実際のデータから計算される経験分布では、
平均値も標準偏差も常に未知のものです。
標本から得られた平均値が、
母集団における真の母数$θ$に近似できているか本当はわかりません。
そこで、一定の確率のもとに母数$θ$を含む区間を求めることを区間推定といいます。
"""

# x軸の等差数列を生成
X = np.arange(start=1, stop=7, step=0.1)

# pdfで確率密度関数を生成
norm_pdf = stats.norm.pdf(x=X, loc=4, scale=0.8)

# intervalで信頼区間95%に当たる変数を取得
lower, upper = stats.norm.interval(alpha=0.95, loc=4, scale=0.8)
print('信頼区間95%点の下限:', lower)
print('信頼区間95%点の上限:', upper)

# pdfで各変数の確率密度を取得
v_lower = stats.norm.pdf(x=lower, loc=4, scale=0.8)
v_upper = stats.norm.pdf(x=upper, loc=4, scale=0.8)

# 可視化
plt.plot(X, norm_pdf)
plt.plot(lower, 0.0, 'k|')
plt.plot(upper, 0.0, 'k|')

plt.vlines(lower, 0.0, v_lower, lw=0.8)    # 下限の垂直線
plt.vlines(upper, 0.0, v_lower, lw=0.8)    # 上限の垂直線

plt.xlabel('確率変数X', fontsize=13, fontname="MS Gothic")
plt.ylabel('確率密度関数pdf', fontsize=13, fontname="MS Gothic")
plt.show()

"""

区間推定では、まず母数$θ$を含む区間の確率を指定します。
この例ではalpha=0.95がそれで、これを信頼係数と呼びます。
多くの場合、99％、95％、90％が使われますが、これは任意です。
その指定された確率のもとで母数$θ$を含む区間の下限と上限が求められます。
この例では95％の確率で、母数$θ$は確率変数が
2.43～5.57の間に含まれていることを示しています。


あとがき

ログ累積分布関数logcdf、ログ生存関数logsfなどは省きましたが、
およそ使用頻度の高そうなものは押さえられたと思います。
これらを利用して、先に掲げた15種類の確率分布を
一つずつ解きほぐしてみたいと思っています。
"""




print("--- 1. Pythonで学ぶ統計学　2-3. 正規分布の基本 ---")



print('1. 正規分布の公式')
"""
$$f(x) = \frac{1}{\sqrt{2\pi \sigma}} \exp \left(-\frac{(x - \mu)^2}
{2\sigma^2} \right) \hspace{20px} (-\infty < x < \infty)$$

正規分布は、上式で定義され、下図のようなベル型の確率密度関数になります
正規分布のパラメータは、期待値$μ$、分散$σ^2$、
そして分散の平方根は標準偏差です
（$標準偏差σ=\sqrt{分散} \hspace{5px}$）
$π$は円周率、$exp$は「ネイピア数（自然対数の底）」と呼ばれるもので、
2.71828（｢鮒一鉢二鉢｣）で近似されます


⑴ 確率密度関数

確率密度関数とは、連続型確率変数の分布を正確に表現したものです
連続型確率変数に対して、飛び飛びの値をとる離散型確率変数は、
確率分布表やヒストグラムに正確に表現できますが、値$x$が連続する場合、
たとえ一定の幅で階級に区切ったとしても階級幅の誤差が生じます
そうした誤差を解消した確率密度関数は、確率変数$X$の値$x$が、
例えば下図のように$a$と$b$の区間にくる確率（=淡黄色部分の面積）
を求める関数です


⑵ 確率密度の計算

期待値$μ$、分散$σ^2$をパラメータとする正規分布（normal distribution）
は、記号で$N(μ, σ^2) \hspace{5px}$と表現されます
$N(0, 1^2) \hspace{5px}$の正規分布を仮定し、
確率変数$x=0$の確率密度を求めます
"""

import numpy as np

mu = 0
sigma = 1
x = 0

pd = (1 / np.sqrt(2 * np.pi * sigma)) * np.e ** (-(((x - mu) ** 2) / (2 * sigma ** 2)))

"""
scipy.statsを利用して同じく$f(0)$を取得し、突合します
"""

from scipy import stats

mu = 0
sigma = 1
x = 0

X = np.linspace(-5, 5, 100)
norm_pdf = stats.norm.pdf(x=X, loc=mu, scale=sigma)    # loc=期待値, scale=標準偏差
a = stats.norm.pdf(x=0, loc=mu, scale=sigma)    # x=確率変数
print(a)    # 0.3989422804014327

"""
いずれも$0.3989422804014327$となります
"""


print('2. 正規分布の意義')


"""

日本の40代男性の平均収入を調べるために、
全国の40代男性から無作為に100人を抽出する
と仮定して、0～800万円の範囲で100人分の乱数を生成したところ、
下図のような分布となりました


この「100人抽出して平均値を計算する」ということを10,000回くり返します
つまり10,000個の平均収入が得られることになりますが、
それをヒストグラムに表したのが下図です
つまり、標本毎に平均値はまちまちですが、
その確率密度関数は正規分布になります
"""


print('3. 正規分布の性質')


"""

正規分布のグラフは、期待値を中心として左右対称のベル型をしています

⑴ 現象が起こる確率

ある区間の現象が起こる確率は、
その区間で確率密度関数の曲線と横軸に囲まれた部分の面積で表されます
「期待値±標準偏差」の区間に68%以上の面積が入ります

「期待値±2×標準偏差」の区間に95%以上の面積が入ります


⑵ パーセント点

平均値を中心に95%を占める範囲を示す境界点、
$μ-1.96σ$と$μ+1.96σ$を両側5%点

同じく99%を占める範囲を示す境界点、
$μ-2.58σ$と$μ+2.58σ$を両側1%点と呼びます


⑶ 上側パーセント点

また上側のみ、すなわちx軸の左側から右側へ95%の範囲にあたる境界点、
$μ+1.64σ$は上側5%点

同じくx軸の左側から右側へ99%の範囲にあたる境界点、
$μ+2.33σ$が上側1%点になります
"""


print('4. 標準正規分布')


"""

期待値$μ$を$0$、標準偏差$σ$を$1$（分散$1^2$）
とする正規分布を標準正規分布といい、次式に定義されます

$$標準正規分布f(x) = \frac{1}{\sqrt{2\pi}} \exp \left(-\frac{x^2}
{2} \right) \hspace{20px}$$

先に計算した$N(0, 1^2) \hspace{5px}$の確率密度関数
$f(0)=0.3989422804014327$と一致しています



Appendix

# 数値計算ライブラリ
import numpy as np
from scipy import stats

# グラフ描画ライブラリ
import matplotlib.pyplot as plt
%matplotlib inline

# matplotlibの日本語表示対応モジュール
!pip install japanize-matplotlib
import japanize_matplotlib
"""
print('1．正規分布の公式')


# 期待値・標準偏差を指定
mu = 0
sigma = 1

# 等差数列を生成
X = np.linspace(-5, 5, 100)

# pdfで確率密度関数を生成
norm_pdf = stats.norm.pdf(x=X, loc=mu, scale=sigma)    # 期待値=0, 標準偏差=1
norm_pdf_max = np.max(norm_pdf)    # 確率密度の最大値

# グラフ描画
plt.plot(X, norm_pdf, lw=5, color='tab:cyan', alpha=0.5)

# 垂直線
plt.vlines(0, 0, norm_pdf_max + 0.02, color='black', lw=0.5)    # 期待値
plt.vlines(mu-sigma, 0, 0.01, color='black', lw=1.5)    # %点(μ-σ)
plt.vlines(mu+sigma, 0, 0.01, color='black', lw=1.5)    # %点(μ+σ)

# 軸目盛
plt.xticks(color='None')    # x軸目盛を消去
plt.yticks(color='None')    # y軸目盛を消去
plt.ylim(0, norm_pdf_max + 0.02)    # y軸目盛範囲

# テキスト
plt.text(-0.2, -0.03, 'μ', fontsize=12, fontname="MS Gothic")    # μ
plt.text(-1.5, -0.03, 'μ-σ', fontsize=12, fontname="MS Gothic")    # μ-σ
plt.text(0.5, -0.03, 'μ+σ', fontsize=12, fontname="MS Gothic")    # μ+σ

plt.show()


print('⑴ 確率密度関数')

"""
# 期待値・標準偏差を指定
mu = 30
sigma = 20

# 任意のx値
xa = 10
xb = 20

# 等差数列を生成
X = np.linspace(0, 100, int(0.1))

# pdfで確率密度関数を生成
norm_pdf = stats.norm.pdf(x=X, loc=mu, scale=sigma)    # 期待値=30, 標準偏差=20

# 確率密度を取得
norm_pdf_max = np.max(norm_pdf)    # 確率密度の最大値
ya = stats.norm.pdf(x=xa, loc=30, scale=20)    # 確率変数xa
yb = stats.norm.pdf(x=xb, loc=30, scale=20)    # 確率変数xb

# グラフ描画
plt.plot(X, norm_pdf, lw=5, color='tab:cyan', alpha=0.5)

plt.vlines(10, 0, ya, color='black', lw=1.2)
plt.vlines(20, 0, yb, color='black', lw=1.2)

# 軸目盛
plt.xticks(color='None')    # x軸目盛を消去
plt.yticks(color='None')    # y軸目盛を消去
plt.ylim(0, norm_pdf_max + 0.001)    # y軸目盛範囲を指定

plt.text(10-0.9, -0.0015, 'a', fontsize=12, fontname="MS Gothic")    # text(a)を配置
plt.text(20-0.9, -0.0015, 'b', fontsize=12, fontname="MS Gothic")    # text(b)を配置

plt.show()
"""


print('2．正規分布の意義')


import random


# 乱数を生成
random.seed(0)    # 乱数シードを固定
X = [random.randint(0, 800) for i in range(100)]

# 平均値を獲得
mu = sum(X) / len(X)

# ヒストグラム描画
plt.hist(X, color='tab:cyan', rwidth=0.9)
plt.text(0.02, 15.5, f'平均年収(万円) {mu:.2f}', fontname="MS Gothic")

plt.show()



# 標本平均を格納する変数
averages = []

# 100人抽出を10,000回試行
for i in range(10000):
    random.seed(i)
    X = [random.randint(0, 800) for i in range(100)]
    average = sum(X) / len(X)
    averages.append(average)

# 平均値を取得
mu = sum(averages) / len(averages)

# ヒストグラムを描画
plt.hist(averages, color='tab:cyan', bins=500)
plt.text(300, 78, f'平均年収(万円) {mu:.2f}', fontname="MS Gothic")

plt.show()


print('2．正規分布の性質')
print('⑴ 現象が起こる確率')


# 期待値・標準偏差を指定
mu = 0
sigma = 1

# 等差数列を生成
X = np.linspace(-5, 5, 100)

# pdfで確率密度関数を生成
norm_pdf = stats.norm.pdf(x=X, loc=mu, scale=sigma)    # 期待値=0, 標準偏差=1

# 確率密度を取得
norm_pdf_max = np.max(norm_pdf)    # 確率密度の最大値
lower = stats.norm.pdf(x=mu-sigma, loc=mu, scale=sigma)    # 確率変数μ-σ
upper = stats.norm.pdf(x=mu+sigma, loc=mu, scale=sigma)    # 確率変数μ+σ

# グラフ描画
plt.plot(X, norm_pdf, lw=5, color='tab:cyan')

# 垂直線
plt.vlines(0, 0, norm_pdf_max + 0.02, color='black', lw=1, linestyle='--')    # 期待値
plt.vlines(mu-sigma, 0, lower, color='black', lw=1)    # %点(μ-σ)
plt.vlines(mu+sigma, 0, upper, color='black', lw=1)    # %点(μ+σ)

# 軸目盛
plt.xticks(color='None')    # x軸目盛を消去
plt.yticks(color='None')    # y軸目盛を消去
plt.ylim(0, norm_pdf_max + 0.02)    # y軸目盛範囲を指定

# テキストを配置
plt.text(-0.2, -0.03, 'μ', fontsize=12, fontname="MS Gothic")    # μ
plt.text(-1.5, -0.03, 'μ-σ', fontsize=12, fontname="MS Gothic")    # μ-σ
plt.text(0.5, -0.03, 'μ+σ', fontsize=12, fontname="MS Gothic")    # μ+σ
plt.text(-0.65, 0.18, '68.3%', fontsize=12, fontname="MS Gothic")    # 68.3%

plt.show()


print('その２')


# 期待値・標準偏差を指定
mu = 0
sigma = 1

# 等差数列を生成
X = np.linspace(-5, 5, 100)

# pdfで確率密度関数を生成
norm_pdf = stats.norm.pdf(x=X, loc=mu, scale=sigma)    # 期待値=0, 標準偏差=1

# 確率密度を取得
norm_pdf_max = np.max(norm_pdf)    # 確率密度の最大値
lower = stats.norm.pdf(x=mu-2*sigma, loc=mu, scale=sigma)    # 確率変数μ-2σ
upper = stats.norm.pdf(x=mu+2*sigma, loc=mu, scale=sigma)    # 確率変数μ+2σ

# グラフ描画
plt.plot(X, norm_pdf, lw=5, color='tab:cyan')

# 垂直線
plt.vlines(0, 0, norm_pdf_max + 0.02, color='black', lw=1, linestyle='--')    # 期待値
plt.vlines(mu-2*sigma, 0, lower, color='black', lw=1)    # %点(μ-2σ)
plt.vlines(mu+2*sigma, 0, upper, color='black', lw=1)    # %点(μ+2σ)

# 軸目盛
plt.xticks(color='None')    # x軸目盛を消去
plt.yticks(color='None')    # y軸目盛を消去
plt.ylim(0, norm_pdf_max + 0.02)    # y軸目盛範囲を指定

# テキストを配置
plt.text(-0.2, -0.03, 'μ', fontsize=12, fontname="MS Gothic")    # μ
plt.text(-2.5, -0.03, 'μ-σ', fontsize=12, fontname="MS Gothic")    # μ-2σ
plt.text(1.5, -0.03, 'μ+σ', fontsize=12, fontname="MS Gothic")    # μ+2σ
plt.text(-0.65, 0.18, '95.5%', fontsize=14, fontname="MS Gothic")    # 95.5%

plt.show()


print('⑵ パーセント点')


# 期待値・標準偏差を指定
mu = 0
sigma = 1

# 等差数列を生成
X = np.linspace(-5, 5, 100)

# pdfで確率密度関数を生成
norm_pdf = stats.norm.pdf(x=X, loc=mu, scale=sigma)    # 期待値=0, 標準偏差=1

# 確率密度を取得
norm_pdf_max = np.max(norm_pdf)    # 確率密度の最大値
lower = stats.norm.pdf(x=mu-1.96*sigma, loc=mu, scale=sigma)    # 確率変数μ-1.96σ
upper = stats.norm.pdf(x=mu+1.96*sigma, loc=mu, scale=sigma)    # 確率変数μ+1.96σ

# グラフ描画
plt.plot(X, norm_pdf, lw=5, color='tab:cyan')

# 垂直線
plt.vlines(0, 0, norm_pdf_max + 0.02, color='black', lw=1, linestyle='--')    # 期待値
plt.vlines(mu-1.96*sigma, 0, lower, color='black', lw=1)    # %点(μ-1.96σ)
plt.vlines(mu+1.96*sigma, 0, upper, color='black', lw=1)    # %点(μ+1.96σ)

# 軸目盛
plt.xticks(color='None')    # x軸目盛を消去
plt.yticks(color='None')    # y軸目盛を消去
plt.ylim(0, norm_pdf_max + 0.02)    # y軸目盛範囲を指定

# テキストを配置
plt.text(-0.2, -0.03, 'μ', fontsize=12, fontname="MS Gothic")    # μ
plt.text(-1.95, -0.07, '↑\nμ-1.96σ', fontsize=13, horizontalalignment='center', color='darkcyan', fontname="MS Gothic")    # μ-1.96σ
plt.text(1.95, -0.07, '↑\nμ+1.96σ', fontsize=13, horizontalalignment='center', color='darkcyan', fontname="MS Gothic")    # μ+1.96σ
plt.text(-0.5, 0.18, '95%', fontsize=14, fontname="MS Gothic")    # 95%
plt.text(2.6, 0.04, '2.5%', fontsize=13, fontname="MS Gothic")    # 2.5%
plt.text(-3.6, 0.04, '2.5%', fontsize=13, fontname="MS Gothic")    # 2.5%
plt.text(-5.2, 0.38, '両側5%点', fontsize=14, fontname="MS Gothic")    # 両側5%点

plt.show()


print('⑵ パーセント点 その２')


# 期待値・標準偏差を指定
mu = 0
sigma = 1

# 等差数列を生成
X = np.linspace(-5, 5, 100)

# pdfで確率密度関数を生成
norm_pdf = stats.norm.pdf(x=X, loc=mu, scale=sigma)    # 期待値=0, 標準偏差=1

# 確率密度を取得
norm_pdf_max = np.max(norm_pdf)    # 確率密度の最大値
lower = stats.norm.pdf(x=mu-2.58*sigma, loc=mu, scale=sigma)    # 確率変数μ-2.58σ
upper = stats.norm.pdf(x=mu+2.58*sigma, loc=mu, scale=sigma)    # 確率変数μ+2.58σ

# グラフ描画
plt.plot(X, norm_pdf, lw=5, color='tab:cyan')

# 垂直線
plt.vlines(0, 0, norm_pdf_max + 0.02, color='black', lw=1, linestyle='--')    # 期待値
plt.vlines(mu-2.58*sigma, 0, lower, color='black', lw=1)    # %点(μ-2.58σ)
plt.vlines(mu+2.58*sigma, 0, upper, color='black', lw=1)    # %点(μ+2.58σ)

# 軸目盛
plt.xticks(color='None')    # x軸目盛を消去
plt.yticks(color='None')    # y軸目盛を消去
plt.ylim(0, norm_pdf_max + 0.02)    # y軸目盛範囲を指定

# テキストを配置
plt.text(-0.2, -0.03, 'μ', fontsize=12, fontname="MS Gothic")    # μ
plt.text(-2.55, -0.07, '↑\nμ-2.58σ', fontsize=13, horizontalalignment='center', color='darkcyan', fontname="MS Gothic")    # μ-2.58σ
plt.text(2.6, -0.07, '↑\nμ+2.58σ', fontsize=13, horizontalalignment='center', color='darkcyan', fontname="MS Gothic")    # μ+2.58σ
plt.text(-0.5, 0.18, '99%', fontsize=14, fontname="MS Gothic")    # 99%
plt.text(2.6, 0.04, '0.5%', fontsize=13, fontname="MS Gothic")    # 2.5%
plt.text(-3.6, 0.04, '0.5%', fontsize=13, fontname="MS Gothic")    # 2.5%
plt.text(-5.2, 0.38, '両側1%点', fontsize=14, fontname="MS Gothic")    # 両側5%点

plt.show()


print('⑶ 上側パーセント点')


# 期待値・標準偏差を指定
mu = 0
sigma = 1

# 等差数列を生成
X = np.linspace(-5, 5, 100)

# pdfで確率密度関数を生成
norm_pdf = stats.norm.pdf(x=X, loc=mu, scale=sigma)    # 期待値=0, 標準偏差=1

# 確率密度を取得
norm_pdf_max = np.max(norm_pdf)    # 確率密度の最大値
upper_1 = stats.norm.pdf(x=mu+1.64*sigma, loc=mu, scale=sigma)    # 確率変数μ+1.64σ
lower = stats.norm.pdf(x=mu-sigma, loc=mu, scale=sigma)    # 確率変数μ-σ
upper_2 = stats.norm.pdf(x=mu+sigma, loc=mu, scale=sigma)    # 確率変数μ+σ

# グラフ描画
plt.plot(X, norm_pdf, lw=5, color='tab:cyan')

# 垂直線
plt.vlines(0, 0, norm_pdf_max + 0.02, color='black', lw=0.8)    # μ
plt.vlines(mu+1.64*sigma, 0, upper_1, color='black', lw=1.2)    # 上側5%点(μ+1.64σ)
plt.vlines(mu-sigma, 0, lower, color='black', lw=1, linestyle='--')    # %点(μ-σ)
plt.vlines(mu+sigma, 0, upper_2, color='black', lw=1, linestyle='--')    # %点(μ+σ)

# 軸目盛
plt.xticks(color='None')    # x軸ラベルを消去
plt.yticks(color='None')    # y軸ラベルを消去
plt.ylim(0, norm_pdf_max + 0.02)    # y軸目盛範囲を指定

# テキストを配置
plt.text(-0.2, -0.03, 'μ', fontsize=12, fontname="MS Gothic")    # μ
plt.text(1.65, -0.07, '↑\nμ-1.64σ', fontsize=13, horizontalalignment='center', color='darkcyan', fontname="MS Gothic")    # μ+1.64σ
plt.text(-0.5, 0.18, '95%', fontsize=14, horizontalalignment='center', color='darkcyan', fontname="MS Gothic")    # 95%
plt.text(2.6, 0.04, '5%', fontsize=13, fontname="MS Gothic")    # 5%
plt.text(-5.2, 0.38, '上側5%点', fontsize=14, fontname="MS Gothic")    # 上側5%点
plt.text(-1.5, -0.03, 'μ-σ', fontsize=12, fontname="MS Gothic")    # μ-σ
plt.text(0.5, 0.03, 'μ+σ', fontsize=12, fontname="MS Gothic")    # μ+σ

plt.show()


print('⑶ 上側パーセント点 その２')


# 期待値・標準偏差を指定
mu = 0
sigma = 1

# 等差数列を生成
X = np.linspace(-5, 5, 100)

# pdfで確率密度関数を生成
norm_pdf = stats.norm.pdf(x=X, loc=mu, scale=sigma)    # 期待値=0, 標準偏差=1

# 確率密度を取得
norm_pdf_max = np.max(norm_pdf)    # 確率密度の最大値
upper_1 = stats.norm.pdf(x=mu+2.33*sigma, loc=mu, scale=sigma)    # 確率変数μ+2.33σ
lower = stats.norm.pdf(x=mu-sigma, loc=mu, scale=sigma)    # 確率変数μ-σ
upper_2 = stats.norm.pdf(x=mu+sigma, loc=mu, scale=sigma)    # 確率変数μ+σ

# グラフ描画
plt.plot(X, norm_pdf, lw=5, color='tab:cyan')

# 垂直線
plt.vlines(0, 0, norm_pdf_max + 0.02, color='black', lw=0.8)    # μ
plt.vlines(mu+2.33*sigma, 0, upper_1, color='black', lw=1.2)    # 上側1%点(μ+2.33σ)
plt.vlines(mu-sigma, 0, lower, color='black', lw=1, linestyle='--')    # %点(μ-σ)
plt.vlines(mu+sigma, 0, upper_2, color='black', lw=1, linestyle='--')    # %点(μ+σ)

# 軸目盛
plt.xticks(color='None')    # x軸ラベルを消去
plt.yticks(color='None')    # y軸ラベルを消去
plt.ylim(0, norm_pdf_max + 0.02)    # y軸目盛範囲を指定

# テキストを配置
plt.text(-0.2, -0.03, 'μ', fontsize=12, fontname="MS Gothic")    # μ
plt.text(2.35, -0.07, '↑\nμ+2.33σ', fontsize=13, horizontalalignment='center', color='darkcyan', fontname="MS Gothic")    # μ+2.33σ
plt.text(-0.5, 0.18, '99%', fontsize=14, horizontalalignment='center', color='darkcyan', fontname="MS Gothic")    # 99%
plt.text(2.6, 0.04, '1%', fontsize=13, fontname="MS Gothic")    # 1%
plt.text(-5.2, 0.38, '上側1%点', fontsize=14, fontname="MS Gothic")    # 上側1%点
plt.text(-1.5, -0.03, 'μ-σ', fontsize=12, fontname="MS Gothic")    # μ-σ
plt.text(0.5, 0.03, 'μ+σ', fontsize=12, fontname="MS Gothic")    # μ+σ

plt.show()


print('4．標準正規分布')


# 期待値・標準偏差を指定
mu = 0
sigma = 1

# 等差数列を生成
X = np.linspace(-5, 5, 100)

# pdfで確率密度関数を生成
norm_pdf = stats.norm.pdf(x=X, loc=mu, scale=sigma)    # 期待値=0, 標準偏差=1

# 確率密度を取得
norm_pdf_max = np.max(norm_pdf)    # 確率密度の最大値


# グラフ描画
plt.plot(X, norm_pdf, lw=5, color='tab:cyan')

# 垂直線
plt.vlines(0, 0, norm_pdf_max + 0.05, color='black', lw=0.8)    # 期待値
plt.hlines(0.2, -0.2, 0.2, color='black', lw=1.2)    # 水平線
plt.hlines(0.403, -0.2, 0.2, color='black', lw=1.2)    # 水平線

# 軸目盛
plt.yticks(color='None')    # y軸ラベルを消去
plt.xticks(fontsize=12)    # x軸ラベルのフォントサイズ
plt.ylim(0, norm_pdf_max + 0.05)    # y軸目盛範囲

# テキストを配置
plt.text(0.2, 0.21, '0.2', fontsize=12, fontname="MS Gothic")    # 0.2
plt.text(0.2, 0.41, '0.4', fontsize=12, fontname="MS Gothic")    # 0.4

plt.show()
