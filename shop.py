import streamlit as st
import random

if "cart" not in st.session_state:
    st.session_state.cart = []

def dairy_products():
    return {
        "milk": {"price":350, "stock":8},
        "yogurt": {"price":120, "stock":10},
        "butter": {"price":450, "stock":5}
    }

def electronics_products():
    return {
        "battery": {"price":40, "stock":20},
        "charger": {"price":150, "stock":6},
        "bulb": {"price":250, "stock":10}
    }

def personal_products():
    return {
        "soap": {"price":150, "stock":12},
        "shampoo": {"price":300, "stock":7},
        "facewash": {"price":220, "stock":9}
    }

products = {
    "Dairy": dairy_products(),
    "Electronics": electronics_products(),
    "Personal Care": personal_products()
}

def add_to_cart(cat, item, qty):
    if item not in products[cat]:
        return "Item nahi mila"
    if products[cat][item]["stock"] < qty:
        return "Stock kam hai"
    price = products[cat][item]["price"] * qty
    products[cat][item]["stock"] -= qty
    st.session_state.cart.append((item, qty, price))
    return "Added"

def show_cart():
    for i in st.session_state.cart:
        st.write(i[0], i[1], "Rs", i[2])

def cart_total():
    return sum(i[2] for i in st.session_state.cart)

def final_bill(discount, tax):
    total = cart_total()
    disc = total * discount / 100
    tax_amt = (total - disc) * tax / 100
    final = total - disc + tax_amt

    show_cart()
    st.write("Subtotal:", total)
    st.write("Discount:", disc)
    st.write("Tax:", tax_amt)
    st.write("Final Bill:", final)
    st.write("Bill No:", random.randint(1000,9999))

st.title("Abdullah Shop 🛒")

cat = st.selectbox("Category", products.keys())
item = st.selectbox("Item", products[cat].keys())
qty = st.number_input("Quantity", 1)

if st.button("Add to Cart"):
    st.write(add_to_cart(cat, item, qty))

st.subheader("Cart")
show_cart()

discount = st.slider("Discount %", 0, 30, 10)
tax = st.slider("Tax %", 0, 20, 5)

if st.button("Purchase"):
    final_bill(discount, tax)