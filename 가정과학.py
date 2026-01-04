import pandas as pd
import matplotlib.pyplot as plt


# 2. 가계 손익계산서 데이터 
data = {
    "항목": ["월급", "기타소득", "식비", "교통비", "통신비", "여가비", "저축"],
    "금액": [3000000, 200000, -600000, -150000, -100000, -300000, -800000]
}

df = pd.DataFrame(data)


# 3. 가계 손익계산서 출력
print("📌 가계 손익계산서")
print(df)
print("-" * 40)


# 4. 총소득, 총지출, 순이익 계산
total_income = df[df["금액"] > 0]["금액"].sum()
total_expense = df[df["금액"] < 0]["금액"].sum()
net_income = total_income + total_expense

print(f"총소득: {total_income:,}원")
print(f"총지출: {abs(total_expense):,}원")
print(f"순이익(잔액): {net_income:,}원")
print("-" * 40)



# 5. 지출 데이터 분리
expense_df = df[df["금액"] < 0].copy()
expense_df["금액"] = expense_df["금액"].abs()



# 6. 저축률 계산
saving = expense_df[expense_df["항목"] == "저축"]["금액"].values[0]
saving_rate = saving / total_income * 100

print(f"저축률: {saving_rate:.1f}%")
print("-" * 40)


# 7. 지출 구조 시각화 (원형 그래프)
plt.figure(figsize=(6, 6))
plt.pie(
    expense_df["금액"],
    labels=expense_df["항목"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("월간 가계 지출 비율")
plt.show()
