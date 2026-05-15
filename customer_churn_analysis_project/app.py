
import pandas as pd

# Load customer dataset
df = pd.read_csv("customer_data.csv")

print("\nOriginal Customer Data:\n")
print(df)

# Churn Analysis
print("\n--- Customer Churn Summary ---")

# Total customers
total_customers = len(df)

# Churned customers
churned = len(df[df["Churn"] == "Yes"])

# Churn rate
churn_rate = (churned / total_customers) * 100

print(f"Total Customers: {total_customers}")
print(f"Churned Customers: {churned}")
print(f"Churn Rate: {churn_rate:.2f}%")

# Analyze engagement
low_activity = df[df["MonthlyUsageHours"] < 10]
print(f"\nCustomers with Low Activity: {len(low_activity)}")

# Analyze subscription type
print("\nChurn by Subscription Type:")
print(df.groupby("SubscriptionType")["Churn"].value_counts())

# Retention Suggestions
print("\n--- Suggestions for Retention ---")
print("1. Improve engagement for low activity users.")
print("2. Offer discounts for long-term subscriptions.")
print("3. Send personalized notifications and offers.")
print("4. Improve customer support response time.")
