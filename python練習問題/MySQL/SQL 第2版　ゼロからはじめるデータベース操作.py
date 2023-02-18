#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- SQL 第2版　ゼロからはじめるデータベース操作 ---")


"""
# 練習問題

mysql> create table jyushoroku(
    -> toroku_bango int NOT NULL,
    -> name VARCHAR(128) NOT NULL,
    -> jyusho VARCHAR(256) NOT NULL,
    -> tel_no char(10),
    -> mail_address char(20),
    -> PRIMARY KEY(toroku_bango));
Query OK, 0 rows affected (2.47 sec)

mysql> alter table jyushoroku ADD COLUMN yubin_bango CHAR(8) NOT NULL;
Query OK, 0 rows affected (0.35 sec)
Records: 0  Duplicates: 0  Warnings: 0

show tables;
+----------------+
| Tables_in_shop |
+----------------+
| jyushoroku     |
| shohin         |
+----------------+
2 rows in set (0.27 sec)

mysql> drop table jyushoroku;
Query OK, 0 rows affected (0.49 sec)

show tables;
+----------------+
| Tables_in_shop |
+----------------+
| shohin         |
+----------------+
1 row in set (0.01 sec)

mysql> create table jyushoroku(
    -> toroku_bango int NOT NULL,
    -> name VARCHAR(128) NOT NULL,
    -> jyusho VARCHAR(256) NOT NULL,
    -> tel_no char(10),
    -> mail_address char(20),
    -> yubin_bango char(8) NOT NULL,
    -> PRIMARY KEY(toroku_bango));
Query OK, 0 rows affected (0.31 sec)

mysql> SELECT shohin_id, shohin_mei, shiire_tanka FROM Shohin;
+-----------+----------------+--------------+
| shohin_id | shohin_mei     | shiire_tanka |
+-----------+----------------+--------------+
| 0001      | Tシャツ        |          500 |
| 0002      | 穴あけパンチ   |          320 |
| 0003      | カッターシャツ |         2800 |
| 0004      | 包丁           |         2800 |
| 0005      | 圧力鍋         |         5000 |
| 0006      | フォーク       |         NULL |
| 0007      | おろしがね     |          790 |
| 0008      | ボールペン     |         NULL |
+-----------+----------------+--------------+
8 rows in set (0.01 sec)

print('Shohinテーブルの全ての列を出力')
SELECT * FROM Shohin;
+-----------+----------------+---------------+--------------+--------------+------------+
| shohin_id | shohin_mei     | shohin_bunrui | hanbai_tanka | shiire_tanka | torokubi   |
+-----------+----------------+---------------+--------------+--------------+------------+
| 0001      | Tシャツ        | 衣服          |         1000 |          500 | 2009-09-20 |
| 0002      | 穴あけパンチ   | 事務用品      |          500 |          320 | 2009-09-11 |
| 0003      | カッターシャツ | 衣服          |         4000 |         2800 | NULL       |
| 0004      | 包丁           | キッチン用品  |         3000 |         2800 | 2009-09-20 |
| 0005      | 圧力鍋         | キッチン用品  |         6800 |         5000 | 2009-01-15 |
| 0006      | フォーク       | キッチン用品  |          500 |         NULL | 2009-09-20 |
| 0007      | おろしがね     | キッチン用品  |          880 |          790 | 2008-04-28 |
| 0008      | ボールペン     | 事務用品      |          100 |         NULL | 2009-11-11 |
+-----------+----------------+---------------+--------------+--------------+------------+
8 rows in set (0.04 sec)

print('列に別名をつける')
mysql> select shohin_id AS id,
    -> shohin_mei AS namae,
    -> shiire_tanka AS tanka
    -> FROM Shohin;
+------+----------------+-------+
| id   | namae          | tanka |
+------+----------------+-------+
| 0001 | Tシャツ        |   500 |
| 0002 | 穴あけパンチ   |   320 |
| 0003 | カッターシャツ |  2800 |
| 0004 | 包丁           |  2800 |
| 0005 | 圧力鍋         |  5000 |
| 0006 | フォーク       |  NULL |
| 0007 | おろしがね     |   790 |
| 0008 | ボールペン     |  NULL |
+------+----------------+-------+
8 rows in set (0.00 sec)

print('日本語で別名をつけた')
mysql> SELECT shohin_id AS '商品ID',
    -> shohin_mei AS '商品名',
    -> shiire_tanka AS '仕入単価'
    -> FROM Shohin;
+--------+----------------+----------+
| 商品ID | 商品名         | 仕入単価 |
+--------+----------------+----------+
| 0001   | Tシャツ        |      500 |
| 0002   | 穴あけパンチ   |      320 |
| 0003   | カッターシャツ |     2800 |
| 0004   | 包丁           |     2800 |
| 0005   | 圧力鍋         |     5000 |
| 0006   | フォーク       |     NULL |
| 0007   | おろしがね     |      790 |
| 0008   | ボールペン     |     NULL |
+--------+----------------+----------+
8 rows in set (0.00 sec)

print('定数を出力')
mysql> select '商品' AS mojiretsu, 38 AS kazu, '2009-02-24' AS hizuke,
    -> shohin_id, shohin_mei
    -> FROM Shohin;
+-----------+------+------------+-----------+----------------+
| mojiretsu | kazu | hizuke     | shohin_id | shohin_mei     |
+-----------+------+------------+-----------+----------------+
| 商品      |   38 | 2009-02-24 | 0001      | Tシャツ        |
| 商品      |   38 | 2009-02-24 | 0002      | 穴あけパンチ   |
| 商品      |   38 | 2009-02-24 | 0003      | カッターシャツ |
| 商品      |   38 | 2009-02-24 | 0004      | 包丁           |
| 商品      |   38 | 2009-02-24 | 0005      | 圧力鍋         |
| 商品      |   38 | 2009-02-24 | 0006      | フォーク       |
| 商品      |   38 | 2009-02-24 | 0007      | おろしがね     |
| 商品      |   38 | 2009-02-24 | 0008      | ボールペン     |
+-----------+------+------------+-----------+----------------+
8 rows in set (0.00 sec)

print('DISTINCTを使ってshohin_bunrui列を重複を省いた形で出力')
mysql> select DISTINCT shohin_bunrui
    -> FROM Shohin;
+---------------+
| shohin_bunrui |
+---------------+
| 衣服          |
| 事務用品      |
| キッチン用品  |
+---------------+
3 rows in set (0.10 sec)

print('NULLを含む列にDISTINCTキーワードを付けた場合')
mysql> select DISTINCT shiire_tanka
    -> FROM Shohin;
+--------------+
| shiire_tanka |
+--------------+
|          500 |
|          320 |
|         2800 |
|         5000 |
|         NULL |
|          790 |
+--------------+
6 rows in set (0.00 sec)

print('複数の列の前にDISTINCTを置いた場合')
mysql> select DISTINCT shohin_bunrui, torokubi
    -> FROM Shohin;
+---------------+------------+
| shohin_bunrui | torokubi   |
+---------------+------------+
| 衣服          | 2009-09-20 |
| 事務用品      | 2009-09-11 |
| 衣服          | NULL       |
| キッチン用品  | 2009-09-20 |
| キッチン用品  | 2009-01-15 |
| キッチン用品  | 2008-04-28 |
| 事務用品      | 2009-11-11 |
+---------------+------------+
7 rows in set (0.00 sec)

print('shohin_bunrui列が'衣服'の行を選択するSELECT文)
mysql> select shohin_mei, shohin_bunrui
    -> FROM Shohin
    -> WHERE shohin_bunrui = '衣服';
+----------------+---------------+
| shohin_mei     | shohin_bunrui |
+----------------+---------------+
| Tシャツ        | 衣服          |
| カッターシャツ | 衣服          |
+----------------+---------------+
2 rows in set (0.04 sec)

print('検索条件の列を出力しないことも可能')
mysql> select shohin_mei
    -> FROM Shohin
    -> WHERE shohin_bunrui = '衣服';
+----------------+
| shohin_mei     |
+----------------+
| Tシャツ        |
| カッターシャツ |
+----------------+
2 rows in set (0.01 sec)

print('1行コメントの使用例')
mysql> -- このSELECT文では、結果から重複をなくします。
mysql> select distinct shohin_id, shiire_tanka
    -> from Shohin;
+-----------+--------------+
| shohin_id | shiire_tanka |
+-----------+--------------+
| 0001      |          500 |
| 0002      |          320 |
| 0003      |         2800 |
| 0004      |         2800 |
| 0005      |         5000 |
| 0006      |         NULL |
| 0007      |          790 |
| 0008      |         NULL |
+-----------+--------------+
8 rows in set (0.00 sec)

print('複数行コメントの使用例')
mysql> /* このSELECT文は、
   /*> 結果から重複をなくします。*/
mysql> select distinct shohin_id, shiire_tanka
    -> from shohin;
+-----------+--------------+
| shohin_id | shiire_tanka |
+-----------+--------------+
| 0001      |          500 |
| 0002      |          320 |
| 0003      |         2800 |
| 0004      |         2800 |
| 0005      |         5000 |
| 0006      |         NULL |
| 0007      |          790 |
| 0008      |         NULL |
+-----------+--------------+
8 rows in set (0.00 sec)

mysql> select distinct shohin_id, shiire_tanka
    -> -- このSELECT文は、結果から重複をなくします。
    -> from Shohin;
+-----------+--------------+
| shohin_id | shiire_tanka |
+-----------+--------------+
| 0001      |          500 |
| 0002      |          320 |
| 0003      |         2800 |
| 0004      |         2800 |
| 0005      |         5000 |
| 0006      |         NULL |
| 0007      |          790 |
| 0008      |         NULL |
+-----------+--------------+
8 rows in set (0.00 sec)

print('複数行コメントをSQL文の途中に差し込む')
mysql> select distinct shohin_id, shiire_tanka
    -> /* このSELECT文は、
   /*> 結果から重複をなくします。*/
    -> from Shohin;
+-----------+--------------+
| shohin_id | shiire_tanka |
+-----------+--------------+
| 0001      |          500 |
| 0002      |          320 |
| 0003      |         2800 |
| 0004      |         2800 |
| 0005      |         5000 |
| 0006      |         NULL |
| 0007      |          790 |
| 0008      |         NULL |
+-----------+--------------+
8 rows in set (0.00 sec)


print('2-2')

print('SQL文には計算式も書ける')
mysql> select shohin_mei, hanbai_tanka,
    -> hanbai_tanka * 2 as 'hanbai_tanka_x2'
    -> from Shohin;
+----------------+--------------+-----------------+
| shohin_mei     | hanbai_tanka | hanbai_tanka_x2 |
+----------------+--------------+-----------------+
| Tシャツ        |         1000 |            2000 |
| 穴あけパンチ   |          500 |            1000 |
| カッターシャツ |         4000 |            8000 |
| 包丁           |         3000 |            6000 |
| 圧力鍋         |         6800 |           13600 |
| フォーク       |          500 |            1000 |
| おろしがね     |          880 |            1760 |
| ボールペン     |          100 |             200 |
+----------------+--------------+-----------------+
8 rows in set (0.10 sec)

print('SELECT句だけのSELECT文')
mysql> SELECT (100 + 200) * 3 as keisan;
+--------+
| keisan |
+--------+
|    900 |
+--------+
1 row in set (0.10 sec)

print('hanbai_tanka列が500の行を選択')
select shohin_mei, shohin_bunrui
    -> from Shohin
    -> where hanbai_tanka = 500;
+--------------+---------------+
| shohin_mei   | shohin_bunrui |
+--------------+---------------+
| 穴あけパンチ | 事務用品      |
| フォーク     | キッチン用品  |
+--------------+---------------+
2 rows in set (0.00 sec)

print('hanbai_tanka列が500ではない行を選択')
mysql> select shohin_mei, shohin_bunrui
    -> from shohin
    -> where hanbai_tanka <> 500;
+----------------+---------------+
| shohin_mei     | shohin_bunrui |
+----------------+---------------+
| Tシャツ        | 衣服          |
| カッターシャツ | 衣服          |
| 包丁           | キッチン用品  |
| 圧力鍋         | キッチン用品  |
| おろしがね     | キッチン用品  |
| ボールペン     | 事務用品      |
+----------------+---------------+
6 rows in set (0.00 sec)

print('販売単価が1000円以上の行を選択')
mysql> select shohin_mei, shohin_bunrui, hanbai_tanka
    -> from Shohin
    -> where hanbai_tanka >= 1000;
+----------------+---------------+--------------+
| shohin_mei     | shohin_bunrui | hanbai_tanka |
+----------------+---------------+--------------+
| Tシャツ        | 衣服          |         1000 |
| カッターシャツ | 衣服          |         4000 |
| 包丁           | キッチン用品  |         3000 |
| 圧力鍋         | キッチン用品  |         6800 |
+----------------+---------------+--------------+
4 rows in set (0.06 sec)
"""