"""pythonのreモジュールを使って、何かの文字の後にoが２回登場する単語に一致する
正規表現を書く。そして、"The ghost that says boo haunts the loo"の文中にある
booやlooに一致するか試す。"""

import re

match = re.findall(".oo", "The ghost that says boo haunts the loo.")
print(match)
