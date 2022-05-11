# bostonデータセットの説明文を読む
from sklearn import datasets


boston = datasets.load_boston()
dir(boston)
print(boston.DESCR)
"""
属性　　　　説明
CRIM　　　　人口1人あたりの犯罪発生数
ZN　　　　　25,000平方フィート以上の居住区画の占める割合
INDUS　　　　小売業以外の商業が占める面積の割合
CHAS　　　　チャールズ川の周辺(1:川の周辺,0:それ以外)
NOX　　　　　NOx濃度
RM　　　　　平均部屋数
AGE　　　　　1940年度より前に建てられた物件の割合
DIS　　　　　5つのボストン市の雇用施設からの距離
RAD　　　　　環状高速道路へのアクセスのしやすさ
TAX　　　　　＄10,000ドル当たりの不動産税率の統計
PTRATIO　　　町毎の児童と教師の比率
B　　　　　　町毎の黒人(BK)の比率
LSTAT　　　　給与の低い職業に従事する人口の割合(%)
MEDV　　　　　住宅価格(単位:＄1000)
"""
