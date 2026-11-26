# Advanced Pandas: GroupBy, Aggregation, Sorting & Merging
import pandas as pd

data = {
    "product": ["Laptop", "Phone", "Laptop", "Tablet",
                "Phone", "Tablet", "Laptop", "Phone"],
    "category": ["Electronics", "Electronics", "Electronics",
                 "Electronics", "Electronics", "Electronics",
                 "Electronics", "Electronics"],
    "city": ["Delhi", "Jaipur", "Mumbai", "Delhi",
             "Jaipur", "Mumbai", "Delhi", "Mumbai"],
    "quantity": [2, 5, 1, 3, 4, 2, 3, 6],
    "price": [50000, 20000, 50000, 15000,
              20000, 15000, 50000, 20000]
}
df=pd.DataFrame(data)
df["total"]=df["quantity"] * df["price"]

print(df)

sorted_df=df.sort_values("total",ascending=True)
print(sorted_df)
sorted_df=df.sort_values("total",ascending=False)
print(sorted_df)
sorted_df=df.sort_values(["quantity","price"],ascending=[True,True])
print(sorted_df)


product_category = df.groupby("product")["quantity"].sum()
print(product_category)

summary = df.groupby("category").agg({
    "product": ["Laptop", "Phone", "Laptop", "Tablet",
                "Phone", "Tablet", "Laptop", "Phone"],
    "category": ["Electronics", "Electronics", "Electronics",
                 "Electronics", "Electronics", "Electronics",
                 "Electronics", "Electronics"],
    "quantity": [2, 5, 1, 3, 4, 2, 3, 6],
    
})
print(summary)