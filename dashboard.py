# dashboard.py
import plotly.express as px
import pandas as pd
import streamlit as st



# Sidebar for navigation
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Home', 'Product Performance', 'Customer Insights', 'Loyal Customers'])

if page == 'Home':
    st.title('Welcome to the Sales Dashboard')
    st.write('Use the sidebar to navigate to different insights.')

elif page == 'Product Performance':
    st.title('Product Performance Analysis')
    # You can place your product analysis code here and use Streamlit commands to display results.
    # Example:
    top_products = df.groupby('Description')['Total Sales'].sum().sort_values(ascending=False).head(10)
    st.bar_chart(top_products)

elif page == 'Customer Insights':
    st.title('Customer Purchase Patterns')
    # Your customer pattern analysis here
    sales_by_hour = df.groupby(df['InvoiceDate'].dt.hour)['Total Sales'].sum()
    st.line_chart(sales_by_hour)

elif page == 'Loyal Customers':
    st.title('Revenue from Loyal Customers')
    # Your loyal customers analysis here
    customer_stats = df.groupby('Customer ID').agg({'Invoice': 'nunique', 'Total Sales': 'sum'})
    loyal_threshold = customer_stats['Invoice'].quantile(0.80)
    loyal_customers = customer_stats[customer_stats['Invoice'] >= loyal_threshold]
    st.write(loyal_customers.sort_values(by='Total Sales', ascending=False).head(10))

# Run this in your terminal: streamlit run dashboard.py