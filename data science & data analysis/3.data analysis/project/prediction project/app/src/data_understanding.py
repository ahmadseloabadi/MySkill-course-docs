import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def load_data(path_all,path_val):
    df_all=pd.read_csv(path_all)
    df_val=pd.read_csv(path_val)
    return df_all,df_val

def explore_data(df, groupby_list, paid_status_list):
    for groub in groupby_list:
        for status in paid_status_list:
            # Filter sesuai status
            if status == "Paid":
                filtered_df = df[df["Unpaid Tagging"] == 0]   # Paid = tidak unpaid
                col_name = f"Paid Cust Distribution by {groub}"
            elif status == "Unpaid":
                filtered_df = df[df["Unpaid Tagging"] == 1]
                col_name = f"Unpaid Cust Distribution by {groub}"
            else:  # All
                filtered_df = df
                col_name = f"Distribution by {groub}"

            # Buat hasil grouping
            explore_result = (
                filtered_df.groupby(by=[groub])["Customer ID"]
                .count()
                .sort_values(ascending=False)
                .reset_index(name=col_name)
            )

            # Tampilkan hasil
            st.markdown(f"### 📊 Distribusi berdasarkan **{groub}** | Status bayar: **{status}**")
            st.dataframe(explore_result,use_container_width=True)

            explore_result.sort_values(\
                  by=[groub], \
                  ascending=True,\
                  inplace=True)

            # ---- Tambahkan plot bar ----
            fig, ax = plt.subplots(figsize=(12, 7))
            explore_result.plot(
                x=groub,
                y=[col_name],
                kind="bar",
                grid=True,
                xlabel=groub,
                ylabel="# People",
                rot=0,
                title=f"Cust. Distribution by {groub} ({status})",
                ax=ax
            )
            st.pyplot(fig)

def avg_balance_product(df,profile_list):
    df['Total Balance'] = df['Balance Q1']+df['Balance Q2']+df['Balance Q3']+df['Balance Q4']
    df['Avg Balance'] = (df['Total Balance'])/4        
    df['Avg Product'] = (df['NumOfProducts Q1']+df['NumOfProducts Q2']+df['NumOfProducts Q3']+df['NumOfProducts Q4'])/4        

    if 'Total Balance' in profile_list:
        st.subheader('Total Balance')
        df_total = pd.DataFrame(\
                     df.groupby(by=["Unpaid Tagging"])["Total Balance"]\
                     .mean()\
                     .reset_index(name='Avg Annual Balance'))
        st.dataframe(df_total,use_container_width=True)
        fig, ax = plt.subplots(figsize=(12, 7))
        df_total.plot(
            x='Unpaid Tagging',
            y=['Avg Annual Balance'],
            kind="bar",
            grid=True,
            xlabel='Unpaid Tagging',
            ylabel='Avg Annual Balance',
            rot=90,
            title='Avg Annual Balance',
            ax=ax
        )
        st.pyplot(fig)

    if 'Avg Balance' in profile_list:
        st.subheader('Avg Balance')
        data_avg = pd.DataFrame(\
                     df.groupby(by=["Unpaid Tagging"])["Avg Balance"]\
                     .mean()\
                     .reset_index(name='Avg Quarterly Balance'))
        st.dataframe(data_avg,use_container_width=True)
        fig, ax = plt.subplots(figsize=(12, 7))
        data_avg.plot(
            x='Unpaid Tagging',
            y=['Avg Quarterly Balance'],
            kind="bar",
            grid=True,
            xlabel='Unpaid Tagging',
            ylabel='Avg Quarterly Balance',
            rot=90,
            title='Avg Quarterly Balance',
            ax=ax
        )
        st.pyplot(fig)

    if 'Avg Product' in profile_list:
        st.subheader('Avg Product')
        data_product = pd.DataFrame(\
                     df.groupby(by=["Unpaid Tagging"])["Avg Product"]\
                     .mean()\
                     .reset_index(name='Avg Product Owned'))
        st.dataframe(data_product,use_container_width=True)
        fig, ax = plt.subplots(figsize=(12, 7))
        data_product.plot(
            x='Unpaid Tagging',
            y=['Avg Product Owned'],
            kind="bar",
            grid=True,
            xlabel='Unpaid Tagging',
            ylabel='Avg Product Owned',
            rot=90,
            title='Avg Product Owned',
            ax=ax
        )
        st.pyplot(fig)






