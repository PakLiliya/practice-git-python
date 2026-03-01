import re
import json

with open("raw.txt", "r", encoding="utf-8") as file:
    data = file.read()

# 1. Extract product names
product_pattern = r"\d+\.\n(.+)"
products = re.findall(product_pattern, data)

# 2. Extract prices (example: 1 200,00 or 308,00)
price_pattern = r"\d[\d\s]*,\d{2}"
prices = re.findall(price_pattern, data)

# Convert prices to float
clean_prices = [float(p.replace(" ", "").replace(",", ".")) for p in prices]

# 3. Extract total
total_pattern = r"ИТОГО:\n([\d\s]+,\d{2})"
total_match = re.search(total_pattern, data)
total = total_match.group(1) if total_match else None

# 4. Extract date and time
datetime_pattern = r"Время:\s*(.+)"
datetime_match = re.search(datetime_pattern, data)
datetime_value = datetime_match.group(1) if datetime_match else None

# 5. Extract payment method
payment_pattern = r"(Банковская карта):"
payment_match = re.search(payment_pattern, data)
payment_method = payment_match.group(1) if payment_match else None

# Create JSON output
receipt_data = {
    "products": products,
    "prices": clean_prices,
    "total": total,
    "datetime": datetime_value,
    "payment_method": payment_method
}

print(json.dumps(receipt_data, indent=4, ensure_ascii=False))