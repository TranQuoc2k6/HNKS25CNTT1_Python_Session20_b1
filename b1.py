"""
* Phân tích lỗi:
    - Giải thích chi tiết tại sao chương trình lại in ra dòng chữ ZeroDivisionError: division by zero?
        + Vì không có biểu thức nào có thể chia được cho 0
    - Nếu chúng ta tạm xóa ShowMaker khỏi danh sách, thì khi xử lý đến Chovy, màn hình Console sẽ in ra thông báo lỗi (Exception) tên là gì? Vì sao?
        + ValueError: invalid literal for int() with base 10
        + Vì không thể ép kiểu dữ liệu string thành số nguyên
    - Đánh giá về cách đặt tên biến player_list, player, n, k, d, a. Theo chuẩn Clean Code, bạn nên đổi tên các biến này thành gì để code tự giải thích được ý nghĩa của nó (Self-documenting code)?
        + Cách đặt tên biến này được coi là mã code bẩn(code smell)
        + player_stats, name, kills, deaths, assists
    - Việc tách công thức tính KDA ra thành một hàm riêng biệt (ví dụ: calculate_kda(kills, deaths, assists)) mang lại lợi ích gì theo nguyên tắc DRY (Don't Repeat Yourself)?
        + tránh bị lặp lại ở nhiều nơi
        + dễ bảo trì
        + tăng tính nhất quán
        + code sạch hơn khi một hàm chỉ thực một thao tác
"""

# Dữ liệu thống kê: (Tên tuyển thủ, Kills, Deaths, Assists)
player_stats = [
    ("Faker", "10", "2", "8"),      # Tuyển thủ 1: Dữ liệu bình thường
    ("ShowMaker", "15", "0", "10"), # Tuyển thủ 2: Không chết mạng nào (Deaths = 0)
    ("Chovy", "12", "ba", "5")      # Tuyển thủ 3: Lỗi API trả về chữ 'ba' thay vì số 3
]

def calculate_kda(kills, deaths, assists):
    kda = (int(kills) + int(assists)) / int(deaths)
    return kda

# Hàm xử lý dồn cục, đặt tên biến kém
def tinh_toan(player_list):
    print("--- BẢNG XẾP HẠNG KDA ---")
    for player in player_list:
        name = player[0]
        kills = player[1]
        deaths = player[2]
        assists = player[3]
        
        try:
            # Ép kiểu và tính toán trực tiếp
            result_kda = calculate_kda(kills, deaths, assists)
            print("Tuyển thủ", name, "có chỉ số KDA là:", result_kda)

        except ZeroDivisionError:
            print(f"Tuyển thủ {player[0]}: KDA Hoàn hảo (Perfect Game)!")
            continue

        except ValueError:
            print(f"Tuyển thủ {player[0]}: Lỗi dữ liệu không hợp lệ!")
            continue

    print("--- HOÀN TẤT ---")

# Chạy hệ thống
tinh_toan(player_stats)