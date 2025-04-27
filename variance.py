import math

# データのリスト
data = [70,80,90, 200, 20]

# 平均を計算
mean = sum(data) / len(data)

# 平均との差を2乗して合計
squared_diffs = [(x - mean) ** 2 for x in data]
sum_squared_diffs = sum(squared_diffs)

# 分散を計算
variance = sum_squared_diffs / len(data)

print(f"分散は {variance:.2f} です")

deviation = math.sqrt(variance)
print(deviation)