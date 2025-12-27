#!/usr/bin/env python3
"""Demo: Product Order Form"""

import sys
sys.path.insert(0, '..')
from zenity_wrapper import Zenity, FormField, FormsOptions
from datetime import datetime

zenity = Zenity()

result = zenity.forms(
    [
        FormField(type='entry', label='Customer Name'),
        FormField(type='entry', label='Email'),
        FormField(type='entry', label='Phone'),
        FormField(
            type='combo',
            label='Product',
            values=[
                'MacBook Pro 16" - $2,499',
                'iPad Pro 12.9" - $1,099',
                'iPhone 15 Pro - $999',
                'Apple Watch Series 9 - $399',
                'AirPods Pro - $249'
            ]
        ),
        FormField(type='entry', label='Quantity'),
        FormField(
            type='combo',
            label='Color',
            values=['Space Black', 'Silver', 'Gold', 'Starlight', 'Midnight', 'Blue', 'Green']
        ),
        FormField(
            type='combo',
            label='Storage',
            values=['128GB', '256GB', '512GB', '1TB', '2TB']
        ),
        FormField(
            type='combo',
            label='Shipping Method',
            values=['Standard (5-7 days) - Free', 'Express (2-3 days) - $15', 'Overnight - $35']
        ),
        FormField(type='entry', label='Shipping Address'),
        FormField(type='entry', label='City, State, ZIP'),
        FormField(type='multiline', label='Special Instructions'),
        FormField(
            type='combo',
            label='Payment Method',
            values=['Credit Card', 'PayPal', 'Apple Pay', 'Bank Transfer']
        )
    ],
    FormsOptions(
        title="Product Order Form",
        text="Complete your order:",
        separator="|",
        show_header=True,
        width=650,
        height=800
    )
)

if result.button == 'ok' and result.values:
    name, email, phone, product, quantity, color, storage, shipping, address, city_state_zip, instructions, payment = result.values
    
    order_id = f"ORD-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    print("\n" + "="*70)
    print("ORDER CONFIRMATION")
    print("="*70)
    print(f"Order ID: {order_id}")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    print(f"\n📦 PRODUCT DETAILS")
    print(f"  {product}")
    print(f"  Color: {color}")
    print(f"  Storage: {storage}")
    print(f"  Quantity: {quantity}")
    
    print(f"\n👤 CUSTOMER INFORMATION")
    print(f"  Name: {name}")
    print(f"  Email: {email}")
    print(f"  Phone: {phone}")
    
    print(f"\n🚚 SHIPPING")
    print(f"  Method: {shipping}")
    print(f"  Address: {address}")
    print(f"  {city_state_zip}")
    
    if instructions:
        print(f"\n📝 Special Instructions:")
        print(f"  {instructions}")
    
    print(f"\n💳 PAYMENT")
    print(f"  Method: {payment}")
    
    print("\n" + "="*70)
    print("\n✓ Order placed successfully!")
    print(f"  You will receive a confirmation email at {email}")
elif result.button == 'cancel':
    print("Order cancelled")
