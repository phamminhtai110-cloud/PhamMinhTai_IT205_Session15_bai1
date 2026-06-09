inventory_stock = 100
total_revenue = 0.0


def add_stock(amount):
    """Add stock into inventory (global update)"""
    global inventory_stock

    if amount <= 0:
        print("Dữ liệu nhập vào phải lớn hơn 0.")
        return

    inventory_stock += amount
    print(f"Đã nhập thành công {amount} sản phẩm.")
    print(f"Tồn kho hiện tại: {inventory_stock}")


def calculate_final_price(quantity, price):
    """
    Calculate final bill after discount and VAT
    return: float final total
    """
    subtotal = quantity * price

    discount = 0
    if subtotal >= 1000:
        discount = subtotal * 0.10

    after_discount = subtotal - discount
    vat = after_discount * 0.08

    return after_discount + vat, discount, vat


def process_sale(quantity, price):
    global inventory_stock, total_revenue

    if quantity <= 0 or price <= 0:
        print("Dữ liệu nhập vào phải lớn hơn 0.")
        return

    if quantity > inventory_stock:
        print(f"Lỗi: Không đủ hàng trong kho. Tồn kho hiện tại chỉ còn {inventory_stock}.")
        return

    final_total, discount, vat = calculate_final_price(quantity, price)

    inventory_stock -= quantity
    total_revenue += final_total

    print("--- HÓA ĐƠN CHI TIẾT ---")
    print(f"Số lượng: {quantity} | Đơn giá: ${price}")
    print(f"Tạm tính: ${quantity * price}")
    print(f"Giảm giá: ${discount}")
    print(f"Thuế VAT: ${vat}")
    print(f"Tổng thanh toán: ${final_total}")
    print("Đã bán thành công!")


def print_report():
    """Print inventory and revenue report"""
    print("--- BÁO CÁO KINH DOANH ---")
    print(f"Tồn kho hiện tại: {inventory_stock}")
    print(f"Tổng doanh thu: ${total_revenue}")


def main():
    while True:
        print("\n========== TECHSTORE MANAGEMENT SYSTEM ==========")
        print("1. Nhập thêm hàng vào kho")
        print("2. Bán hàng (Tính toán hóa đơn)")
        print("3. Xem báo cáo tổng quan")
        print("4. Thoát chương trình")

        choice = input("Chọn chức năng (1-4): ")

        if choice == "1":
            try:
                amount = int(input("--- NHẬP HÀNG ---\nNhập số lượng sản phẩm muốn thêm: "))
                add_stock(amount)
            except:
                print("Sai kiểu dữ liệu!")

        elif choice == "2":
            try:
                quantity = int(input("--- BÁN HÀNG ---\nNhập số lượng mua: "))
                price = float(input("Nhập đơn giá ($): "))
                process_sale(quantity, price)
            except:
                print("Sai kiểu dữ liệu!")

        elif choice == "3":
            print_report()

        elif choice == "4":
            print("Thoát chương trình...")
            break

        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()