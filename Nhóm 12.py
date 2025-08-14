import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# ====== 1. Tạo biến đầu vào ======
delivery_time = ctrl.Antecedent(np.arange(0, 11, 1), 'delivery_time')
product_quality = ctrl.Antecedent(np.arange(0, 11, 1), 'product_quality')
cost = ctrl.Antecedent(np.arange(0, 11, 1), 'cost')
# THAY ĐỔI: Chuyển thang đo của customer_rating thành 0-5
customer_rating = ctrl.Antecedent(np.arange(0, 6, 1), 'customer_rating')

# ====== 2. Tạo biến đầu ra ======
supplier_suitability = ctrl.Consequent(np.arange(0, 11, 1), 'supplier_suitability')

# ====== 3. Định nghĩa các hàm thành viên (Membership Functions) ======

# -- HOÀN CHỈNH: Định nghĩa thủ công cho các biến đầu vào --

# Delivery Time (Thang đo 0-10)
delivery_time['fast'] = fuzz.trimf(delivery_time.universe, [0, 0, 5])
delivery_time['moderate'] = fuzz.trimf(delivery_time.universe, [0, 5, 10])
delivery_time['slow'] = fuzz.trimf(delivery_time.universe, [5, 10, 10])

# Product Quality (Thang đo 0-10)
product_quality['poor'] = fuzz.trimf(product_quality.universe, [0, 0, 5])
product_quality['average'] = fuzz.trimf(product_quality.universe, [0, 5, 10])
product_quality['good'] = fuzz.trimf(product_quality.universe, [5, 10, 10])

# Cost (Thang đo 0-10)
cost['low'] = fuzz.trimf(cost.universe, [0, 0, 5])
cost['medium'] = fuzz.trimf(cost.universe, [0, 5, 10])
cost['high'] = fuzz.trimf(cost.universe, [5, 10, 10])

# Customer Rating (Thang đo mới 0-5)
customer_rating['low'] = fuzz.trimf(customer_rating.universe, [0, 0, 2.5])
customer_rating['medium'] = fuzz.trimf(customer_rating.universe, [0, 2.5, 5])
customer_rating['high'] = fuzz.trimf(customer_rating.universe, [2.5, 5, 5])


# Hàm thành viên cho biến đầu ra
supplier_suitability['low'] = fuzz.trimf(supplier_suitability.universe, [0, 0, 5])
supplier_suitability['medium'] = fuzz.trimf(supplier_suitability.universe, [0, 5, 10])
supplier_suitability['high'] = fuzz.trimf(supplier_suitability.universe, [5, 10, 10])


# ====== 4. Viết tay đầy đủ 81 luật mờ ======
# 1.1: Quality = poor (-1 điểm)
rule1 = ctrl.Rule(delivery_time['fast'] & product_quality['poor'] & cost['low'] & customer_rating['low'], supplier_suitability['medium'])
rule2 = ctrl.Rule(delivery_time['fast'] & product_quality['poor'] & cost['low'] & customer_rating['medium'], supplier_suitability['medium'])
rule3 = ctrl.Rule(delivery_time['fast'] & product_quality['poor'] & cost['low'] & customer_rating['high'], supplier_suitability['high'])
rule4 = ctrl.Rule(delivery_time['fast'] & product_quality['poor'] & cost['medium'] & customer_rating['low'], supplier_suitability['medium'])
rule5 = ctrl.Rule(delivery_time['fast'] & product_quality['poor'] & cost['medium'] & customer_rating['medium'], supplier_suitability['medium'])
rule6 = ctrl.Rule(delivery_time['fast'] & product_quality['poor'] & cost['medium'] & customer_rating['high'], supplier_suitability['medium'])
rule7 = ctrl.Rule(delivery_time['fast'] & product_quality['poor'] & cost['high'] & customer_rating['low'], supplier_suitability['low'])
rule8 = ctrl.Rule(delivery_time['fast'] & product_quality['poor'] & cost['high'] & customer_rating['medium'], supplier_suitability['medium'])
rule9 = ctrl.Rule(delivery_time['fast'] & product_quality['poor'] & cost['high'] & customer_rating['high'], supplier_suitability['medium'])
# 1.2: Quality = average (0 điểm)
rule10 = ctrl.Rule(delivery_time['fast'] & product_quality['average'] & cost['low'] & customer_rating['low'], supplier_suitability['medium'])
rule11 = ctrl.Rule(delivery_time['fast'] & product_quality['average'] & cost['low'] & customer_rating['medium'], supplier_suitability['high'])
rule12 = ctrl.Rule(delivery_time['fast'] & product_quality['average'] & cost['low'] & customer_rating['high'], supplier_suitability['high'])
rule13 = ctrl.Rule(delivery_time['fast'] & product_quality['average'] & cost['medium'] & customer_rating['low'], supplier_suitability['medium'])
rule14 = ctrl.Rule(delivery_time['fast'] & product_quality['average'] & cost['medium'] & customer_rating['medium'], supplier_suitability['medium'])
rule15 = ctrl.Rule(delivery_time['fast'] & product_quality['average'] & cost['medium'] & customer_rating['high'], supplier_suitability['high'])
rule16 = ctrl.Rule(delivery_time['fast'] & product_quality['average'] & cost['high'] & customer_rating['low'], supplier_suitability['medium'])
rule17 = ctrl.Rule(delivery_time['fast'] & product_quality['average'] & cost['high'] & customer_rating['medium'], supplier_suitability['medium'])
rule18 = ctrl.Rule(delivery_time['fast'] & product_quality['average'] & cost['high'] & customer_rating['high'], supplier_suitability['medium'])
# 1.3: Quality = good (+1 điểm)
rule19 = ctrl.Rule(delivery_time['fast'] & product_quality['good'] & cost['low'] & customer_rating['low'], supplier_suitability['high'])
rule20 = ctrl.Rule(delivery_time['fast'] & product_quality['good'] & cost['low'] & customer_rating['medium'], supplier_suitability['high'])
rule21 = ctrl.Rule(delivery_time['fast'] & product_quality['good'] & cost['low'] & customer_rating['high'], supplier_suitability['high'])
rule22 = ctrl.Rule(delivery_time['fast'] & product_quality['good'] & cost['medium'] & customer_rating['low'], supplier_suitability['medium'])
rule23 = ctrl.Rule(delivery_time['fast'] & product_quality['good'] & cost['medium'] & customer_rating['medium'], supplier_suitability['high'])
rule24 = ctrl.Rule(delivery_time['fast'] & product_quality['good'] & cost['medium'] & customer_rating['high'], supplier_suitability['high'])
rule25 = ctrl.Rule(delivery_time['fast'] & product_quality['good'] & cost['high'] & customer_rating['low'], supplier_suitability['medium'])
rule26 = ctrl.Rule(delivery_time['fast'] & product_quality['good'] & cost['high'] & customer_rating['medium'], supplier_suitability['medium'])
rule27 = ctrl.Rule(delivery_time['fast'] & product_quality['good'] & cost['high'] & customer_rating['high'], supplier_suitability['high'])
# Nhóm 2: Delivery Time = moderate (0 điểm)
rule28 = ctrl.Rule(delivery_time['moderate'] & product_quality['poor'] & cost['low'] & customer_rating['low'], supplier_suitability['medium'])
rule29 = ctrl.Rule(delivery_time['moderate'] & product_quality['poor'] & cost['low'] & customer_rating['medium'], supplier_suitability['medium'])
rule30 = ctrl.Rule(delivery_time['moderate'] & product_quality['poor'] & cost['low'] & customer_rating['high'], supplier_suitability['medium'])
rule31 = ctrl.Rule(delivery_time['moderate'] & product_quality['poor'] & cost['medium'] & customer_rating['low'], supplier_suitability['low'])
rule32 = ctrl.Rule(delivery_time['moderate'] & product_quality['poor'] & cost['medium'] & customer_rating['medium'], supplier_suitability['medium'])
rule33 = ctrl.Rule(delivery_time['moderate'] & product_quality['poor'] & cost['medium'] & customer_rating['high'], supplier_suitability['medium'])
rule34 = ctrl.Rule(delivery_time['moderate'] & product_quality['poor'] & cost['high'] & customer_rating['low'], supplier_suitability['low'])
rule35 = ctrl.Rule(delivery_time['moderate'] & product_quality['poor'] & cost['high'] & customer_rating['medium'], supplier_suitability['low'])
rule36 = ctrl.Rule(delivery_time['moderate'] & product_quality['poor'] & cost['high'] & customer_rating['high'], supplier_suitability['medium'])
rule37 = ctrl.Rule(delivery_time['moderate'] & product_quality['average'] & cost['low'] & customer_rating['low'], supplier_suitability['medium'])
rule38 = ctrl.Rule(delivery_time['moderate'] & product_quality['average'] & cost['low'] & customer_rating['medium'], supplier_suitability['medium'])
rule39 = ctrl.Rule(delivery_time['moderate'] & product_quality['average'] & cost['low'] & customer_rating['high'], supplier_suitability['high'])
rule40 = ctrl.Rule(delivery_time['moderate'] & product_quality['average'] & cost['medium'] & customer_rating['low'], supplier_suitability['medium'])
rule41 = ctrl.Rule(delivery_time['moderate'] & product_quality['average'] & cost['medium'] & customer_rating['medium'], supplier_suitability['medium'])
rule42 = ctrl.Rule(delivery_time['moderate'] & product_quality['average'] & cost['medium'] & customer_rating['high'], supplier_suitability['medium'])
rule43 = ctrl.Rule(delivery_time['moderate'] & product_quality['average'] & cost['high'] & customer_rating['low'], supplier_suitability['medium'])
rule44 = ctrl.Rule(delivery_time['moderate'] & product_quality['average'] & cost['high'] & customer_rating['medium'], supplier_suitability['medium'])
rule45 = ctrl.Rule(delivery_time['moderate'] & product_quality['average'] & cost['high'] & customer_rating['high'], supplier_suitability['medium'])
rule46 = ctrl.Rule(delivery_time['moderate'] & product_quality['good'] & cost['low'] & customer_rating['low'], supplier_suitability['high'])
rule47 = ctrl.Rule(delivery_time['moderate'] & product_quality['good'] & cost['low'] & customer_rating['medium'], supplier_suitability['high'])
rule48 = ctrl.Rule(delivery_time['moderate'] & product_quality['good'] & cost['low'] & customer_rating['high'], supplier_suitability['high'])
rule49 = ctrl.Rule(delivery_time['moderate'] & product_quality['good'] & cost['medium'] & customer_rating['low'], supplier_suitability['medium'])
rule50 = ctrl.Rule(delivery_time['moderate'] & product_quality['good'] & cost['medium'] & customer_rating['medium'], supplier_suitability['high'])
rule51 = ctrl.Rule(delivery_time['moderate'] & product_quality['good'] & cost['medium'] & customer_rating['high'], supplier_suitability['high'])
rule52 = ctrl.Rule(delivery_time['moderate'] & product_quality['good'] & cost['high'] & customer_rating['low'], supplier_suitability['medium'])
rule53 = ctrl.Rule(delivery_time['moderate'] & product_quality['good'] & cost['high'] & customer_rating['medium'], supplier_suitability['medium'])
rule54 = ctrl.Rule(delivery_time['moderate'] & product_quality['good'] & cost['high'] & customer_rating['high'], supplier_suitability['high'])
# Nhóm 3: Delivery Time = slow (-1 điểm)
rule55 = ctrl.Rule(delivery_time['slow'] & product_quality['poor'] & cost['low'] & customer_rating['low'], supplier_suitability['low'])
rule56 = ctrl.Rule(delivery_time['slow'] & product_quality['poor'] & cost['low'] & customer_rating['medium'], supplier_suitability['medium'])
rule57 = ctrl.Rule(delivery_time['slow'] & product_quality['poor'] & cost['low'] & customer_rating['high'], supplier_suitability['medium'])
rule58 = ctrl.Rule(delivery_time['slow'] & product_quality['poor'] & cost['medium'] & customer_rating['low'], supplier_suitability['low'])
rule59 = ctrl.Rule(delivery_time['slow'] & product_quality['poor'] & cost['medium'] & customer_rating['medium'], supplier_suitability['low'])
rule60 = ctrl.Rule(delivery_time['slow'] & product_quality['poor'] & cost['medium'] & customer_rating['high'], supplier_suitability['medium'])
rule61 = ctrl.Rule(delivery_time['slow'] & product_quality['poor'] & cost['high'] & customer_rating['low'], supplier_suitability['low'])
rule62 = ctrl.Rule(delivery_time['slow'] & product_quality['poor'] & cost['high'] & customer_rating['medium'], supplier_suitability['low'])
rule63 = ctrl.Rule(delivery_time['slow'] & product_quality['poor'] & cost['high'] & customer_rating['high'], supplier_suitability['low'])
rule64 = ctrl.Rule(delivery_time['slow'] & product_quality['average'] & cost['low'] & customer_rating['low'], supplier_suitability['medium'])
rule65 = ctrl.Rule(delivery_time['slow'] & product_quality['average'] & cost['low'] & customer_rating['medium'], supplier_suitability['medium'])
rule66 = ctrl.Rule(delivery_time['slow'] & product_quality['average'] & cost['low'] & customer_rating['high'], supplier_suitability['medium'])
rule67 = ctrl.Rule(delivery_time['slow'] & product_quality['average'] & cost['medium'] & customer_rating['low'], supplier_suitability['medium'])
rule68 = ctrl.Rule(delivery_time['slow'] & product_quality['average'] & cost['medium'] & customer_rating['medium'], supplier_suitability['medium'])
rule69 = ctrl.Rule(delivery_time['slow'] & product_quality['average'] & cost['medium'] & customer_rating['high'], supplier_suitability['medium'])
rule70 = ctrl.Rule(delivery_time['slow'] & product_quality['average'] & cost['high'] & customer_rating['low'], supplier_suitability['low'])
rule71 = ctrl.Rule(delivery_time['slow'] & product_quality['average'] & cost['high'] & customer_rating['medium'], supplier_suitability['medium'])
rule72 = ctrl.Rule(delivery_time['slow'] & product_quality['average'] & cost['high'] & customer_rating['high'], supplier_suitability['medium'])
rule73 = ctrl.Rule(delivery_time['slow'] & product_quality['good'] & cost['low'] & customer_rating['low'], supplier_suitability['medium'])
rule74 = ctrl.Rule(delivery_time['slow'] & product_quality['good'] & cost['low'] & customer_rating['medium'], supplier_suitability['high'])
rule75 = ctrl.Rule(delivery_time['slow'] & product_quality['good'] & cost['low'] & customer_rating['high'], supplier_suitability['high'])
rule76 = ctrl.Rule(delivery_time['slow'] & product_quality['good'] & cost['medium'] & customer_rating['low'], supplier_suitability['medium'])
rule77 = ctrl.Rule(delivery_time['slow'] & product_quality['good'] & cost['medium'] & customer_rating['medium'], supplier_suitability['medium'])
rule78 = ctrl.Rule(delivery_time['slow'] & product_quality['good'] & cost['medium'] & customer_rating['high'], supplier_suitability['high'])
rule79 = ctrl.Rule(delivery_time['slow'] & product_quality['good'] & cost['high'] & customer_rating['low'], supplier_suitability['medium'])
rule80 = ctrl.Rule(delivery_time['slow'] & product_quality['good'] & cost['high'] & customer_rating['medium'], supplier_suitability['medium'])
rule81 = ctrl.Rule(delivery_time['slow'] & product_quality['good'] & cost['high'] & customer_rating['high'], supplier_suitability['medium'])

# SỬA LỖI: Sửa các ký tự khoảng trắng không hợp lệ
all_rules = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
             rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20,
             rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30,
             rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40,
             rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49, rule50,
             rule51, rule52, rule53, rule54, rule55, rule56, rule57, rule58, rule59, rule60,
             rule61, rule62, rule63, rule64, rule65, rule66, rule67, rule68, rule69, rule70,
             rule71, rule72, rule73, rule74, rule75, rule76, rule77, rule78, rule79, rule80,
             rule81]

# ====== 5. Tạo và mô phỏng hệ thống điều khiển ======
supply_ctrl = ctrl.ControlSystem(all_rules)
supply_sim = ctrl.ControlSystemSimulation(supply_ctrl)

# ====== 6. Nhập dữ liệu mẫu ======
supply_sim.input['delivery_time'] = 2      # Rất nhanh
supply_sim.input['product_quality'] = 6  # Chất lượng tốt
supply_sim.input['cost'] = 9              # Chi phí thấp
supply_sim.input['customer_rating'] = 3  # Đánh giá cao (trên thang 0-5)

# ====== 7. Tính toán ======
supply_sim.compute()

# ====== 8. In kết quả ======
print("Supplier Suitability Score:", round(supply_sim.output['supplier_suitability'], 2))

# ====== 9. Vẽ đồ thị ======

delivery_time.view()
product_quality.view()
cost.view()
customer_rating.view()

# Hiển thị kết quả cuối cùng
supplier_suitability.view(sim=supply_sim)
