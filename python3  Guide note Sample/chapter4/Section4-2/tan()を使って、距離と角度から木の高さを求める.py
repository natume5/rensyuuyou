# tan()を使って、距離と角度から木の高さを求める
import math
kyori = 20
kakudo = math.radians(32)
takasa = kyori * math.tan(kakudo)
takasa = math.floor(takasa * 100) / 100
print(str(takasa) + "m")
