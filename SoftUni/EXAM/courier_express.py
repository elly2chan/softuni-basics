shipment_weight_kg = float(input())
shipment_type = input()
shipment_distance_km = int(input())
price_per_km = 0

if shipment_type in ("standard", "express"):
    if shipment_weight_kg < 1:
        price_per_km = 0.03
        if shipment_type == "express":
            weight_price = shipment_weight_kg * (price_per_km * 80 / 100)
    elif 1 <= shipment_weight_kg < 10:
        price_per_km = 0.05
        if shipment_type == "express":
            weight_price = shipment_weight_kg * (price_per_km * 40 / 100)
    elif 10 <= shipment_weight_kg < 40:
        price_per_km = 0.1
        if shipment_type == "express":
            weight_price = shipment_weight_kg * (price_per_km * 5 / 100)
    elif 40 <= shipment_weight_kg < 90:
        price_per_km = 0.15
        if shipment_type == "express":
            weight_price = shipment_weight_kg * (price_per_km * 2 / 100)
    elif 90 <= shipment_weight_kg < 150:
        price_per_km = 0.2
        if shipment_type == "express":
            weight_price = shipment_weight_kg * (price_per_km / 100)

if shipment_type == "standard":
    total = shipment_distance_km * price_per_km
elif shipment_type == "express":
    total = (shipment_distance_km * weight_price) + (shipment_distance_km * price_per_km)


print(f'The delivery of your shipment with weight {shipment_weight_kg:.3f} kg. would cost {total:.2f} lv.')