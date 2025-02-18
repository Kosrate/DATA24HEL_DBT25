import streamlit as st
from database.fetch_products import get_products_to_reorder, get_all_products
from utils.qr_generator import generate_qr

st.title("Produkter att beställa")

# Välj vy
view_option = st.sidebar.radio("Välj vy", ("Produkter att beställa", "Alla produkter"))

if view_option == "Produkter att beställa":
    products = get_products_to_reorder()
    if products:
        for product in products:
            st.subheader(product["ProductName"])
            st.write(f"**Leverantör:** {product['CompanyName']}")
            st.write(f"**Kontaktperson:** {product['ContactName']}")
            st.write(f"**Telefon:** {product['Phone']}")
            qr_image = generate_qr(product['Phone'])
            st.image(qr_image, caption="Skanna för att ringa", use_column_width=False)
            st.write(f"📞 **Kontakta:** {product['ContactName']} på {product['Phone']}")
            st.markdown("---")
    else:
        st.write("Inga produkter behöver beställas just nu.")

elif view_option == "Alla produkter":
    all_products = get_all_products()
    if all_products:
        for product in all_products:
            st.subheader(product["ProductName"])
            st.write(f"**Leverantör:** {product['CompanyName']}")
            st.write(f"**Kontaktperson:** {product['ContactName']}")
            st.write(f"**Telefon:** {product['Phone']}")
            st.write(f"**Lagerstatus:** {product['UnitsInStock']} i lager, {product['UnitsOnOrder']} på väg")
            st.write(f"**Beställningsgräns:** {product['ReorderLevel']}")
            st.write(f"📞 **Kontakta:** {product['ContactName']} på {product['Phone']}")
            st.markdown("---")
    else:
        st.write("Inga produkter hittades i databasen.")
