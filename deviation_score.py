import math

# テストの点数データ
scores = [70, 80, 90, 60, 50]

# 計算用の関数を作る
def calculate_deviation_score(score, scores):
    # 平均を求める
    mean = sum(scores) / len(scores)
    
    # 分散を求める
    squared_diffs = [(x - mean) ** 2 for x in scores]
    variance = sum(squared_diffs) / len(scores)
    
    # 標準偏差を求める
    std_dev = math.sqrt(variance)
    
    # 偏差値を計算
    deviation_score = 50 + (score - mean) / std_dev * 10
    return deviation_score

# 例えば80点の人の偏差値を出す
my_score = 80
my_deviation = calculate_deviation_score(my_score, scores)

print(f"あなたの偏差値は {my_deviation:.2f} です")
