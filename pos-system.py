import sys
import csv


### 商品クラス
class Item:
    def __init__(self, item_code, item_name, price):
        self.item_code = item_code
        self.item_name = item_name
        self.price = int(price)

    def get_price(self):
        return self.price


### オーダークラス
class Order:
    def __init__(self, item_master):
        self.item_order_list = []
        self.item_master = item_master

    def add_item_order(self, item_code, quantity):
        self.item_order_list.append([item_code, quantity])


    def view_item_list(self):
        for item in self.item_order_list:
            print("商品コード : {} 個数 : {}".format(item[0], item[1]))

    def show_all_items(self):
        for item_master in self.item_master:
            for item in self.item_order_list:
                if item in item_master.item_code:
                    print('商品名:{} 商品価格:{}'.format(item_master.item_name, item_master.price))


# 商品オーダー時にマスターに登録されている商品か調べる関数
def isvalid_order_code(master, order_item_code):
    for item in master:
        if order_item_code in item.item_code:
            return order_item_code

    print('入力内容が間違っています', file=sys.stderr)
    sys.exit()


### メイン処理
def main():
    # マスタ登録
    item_master = []
    # 商品マスターをcsvから登録
    with open('products_master.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            col = tuple(row)
            item_master.append(Item(col[0], col[1], int(col[2])))

    # ターミナルから商品をオーダー
    for item in item_master:
        print('商品コード : {}  商品名 : {}  価格 : {}'.format(item.item_code, item.item_name, item.price))
    order_item_code = input('商品コードを入力して下さい')
    # 入力内容をvalidate
    item_code = isvalid_order_code(item_master, order_item_code)
    # 注文個数を入力
    print('商品コード : {}'.format(item_code))
    quantity = input('何個注文しますか')
    if not quantity:
        print('入力内容が間違っています', file=sys.stderr)
        sys.exit()
    else:
        # オーダー登録
        order = Order(item_master)
        order.add_item_order(item_code, int(quantity))
        order.view_item_list()
        # order.show_all_items()
        """
        オーダー登録時に個数も登録できる様にする
         """
    # 個数を入力
    # オーダー登録

    # オーダー表示

    # オーダーの内容表示



# order = Order(item_master)
# order.add_item_order("001")
# order.add_item_order("002")
# order.add_item_order("003")
# order.view_item_detail()
# # オーダー表示
# order.view_item_list()


if __name__ == "__main__":
    main()
# Column = ['商品コード', '商品名', '価格']
# lista = ["001", "りんご", 100]
# listb = ["002", "なし", 120]
# listc = ["003", "みかん", 150]
# df = pd.DataFrame([lista, listb, listc], columns=Column)
# df.to_csv("products_master.csv", index=False)
