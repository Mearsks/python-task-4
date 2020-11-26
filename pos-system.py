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
        self.item_order_list = {
            '001': 1,
            '003': 5,
        }
        self.item_master = item_master

    def add_item_order(self, item_code, quantity):
        if item_code in self.item_order_list.keys():
            self.item_order_list[item_code] += quantity
        else:
            self.item_order_list[item_code] = quantity

    def view_item_list(self):
        for item_code, quantity in self.item_order_list.items():
            print("商品コード: {} 個数: {}".format(item_code, quantity))

    def show_all(self):
        total_amount = 0
        for item_master in self.item_master:
            for item_code, quantity in self.item_order_list.items():
                if item_code in item_master.item_code:
                    total_amount += (item_master.price * quantity)
                    print('商品名:{} 商品価格:{}'.format(item_master.item_name, item_master.price))
                    print('個数{}'.format(quantity))
        print('合計金額: {}'.format(total_amount))
        return total_amount


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
    # トータル金額
    total_amount = 0
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
    quantity = input('何個注文しますか: ')
    if not quantity:
        print('入力内容が間違っています', file=sys.stderr)
        sys.exit()
    else:
        # オーダー登録
        order = Order(item_master)
        order.add_item_order(item_code, int(quantity))
        # オーダー表示
        order.view_item_list()
        # オーダー登録した商品の一覧（商品名、価格）を表示し、かつ合計金額、個数を表示
        total_amount += order.show_all()

    # お釣り計算
    customer_payment = input('お金をお支払いください>> ')
    if not customer_payment:
        print('入力が間違っています')
        return
    elif total_amount > int(customer_payment):
        print('金額が足りていません')
        return
    return_change = int(customer_payment) - total_amount
    if return_change > 0:
        print('お釣りは{}円です'.format(return_change))
        print('ありがとうございました')
    else:
        print('ありがとうございました')


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
