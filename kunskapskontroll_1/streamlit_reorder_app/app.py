import streamlit as st
from database.fetch_products import get_products_to_reorder
from utils.qr_generator import generate_qr

st.title("Produkter att beställa")

# Hämta produkter frpn databasen
products = get_products_to_reorder()

if products:
    for product in products:
        st.subheader(product["ProductName"])
        st.write(f"**Leverantör:** {product['CompanyName']}")
        st.write(f"**Kontaktperson:** {product['ContactName']}")
        st.write(f"**Teleffon:** {product['Phone']}")

        # Generera QR-kod
        qr_image = generate_qr(product['Phone'])
        st.image(qr_image, caption="Skanna fför att ringa", use_column_width=False)
        st.markdown("---")
else:
    st.write("Inga produkter att beställa")