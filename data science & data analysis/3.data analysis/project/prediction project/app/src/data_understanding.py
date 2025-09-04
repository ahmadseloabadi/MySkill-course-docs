import pandas as pd
import streamlit as st

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

            filtered_df.plot(x='Age',
            y=['Distribution by Age'],
            kind='bar',
            grid = True,
            xlabel = 'Age',
            ylabel = '# People',
            figsize=(12,7),
            rot = 0,
            title = 'Cust. Distribution by Age',
            table = False,
            secondary_y = False)





