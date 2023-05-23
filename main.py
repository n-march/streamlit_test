import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from data_generator import related_people, related_entities, related_leaders

try:
    # Access the session state object, creating a new one if necessary
    session_state = st.session_state
except AttributeError:
    # Create a new session state object
    session_state = st._legacy_set_session_state()


def main():
    # import data from data_generator
    people_df = related_people()
    entities_df = related_entities()
    leader_df = related_leaders()

    period_options = ['All', 'Last week', 'Last month', 'Last 2 months']

    # Check if 'selected_period' is already in the session state
    if 'selected_period' not in st.session_state:
        # If not, initialize it
        st.session_state.selected_period = period_options[0]

    # Use the state in the selectbox
    st.session_state.selected_period = st.selectbox(
        "Select Period",
        period_options,
        index=period_options.index(st.session_state.selected_period)
    )

    # Update the session state with the new selected period
    selected_period = st.session_state.selected_period
    session_state.selected_period = selected_period

    if selected_period == 'All':
        filtered_people_df = people_df
        filtered_entities_df = entities_df
        filtered_leader_df = leader_df
    else:
        # Filter the data frame based on the selected period
        filtered_people_df = people_df[people_df['Period'] == selected_period]
        filtered_entities_df = entities_df[entities_df['Period'] == selected_period]
        filtered_leader_df = leader_df[leader_df['Period'] == selected_period]

    tab1, tab2 = st.tabs(["Insights", "Raw Data"])

    with tab1:

        options_people = st.multiselect(
            "Don't show me results for these people:",
            people_df['Name'].unique().tolist())

        options_entities = st.multiselect(
            "Don't show me results for these entities:",
            entities_df['Entities'].unique().tolist())

        # Filter out the selected options
        filtered_people_df = filtered_people_df[~filtered_people_df['Name'].isin(options_people)]
        filtered_entities_df = filtered_entities_df[~filtered_entities_df['Entities'].isin(options_entities)]


        # ###### Related people mentioned barchart ######
        st.write("Related people mentioned")

        # Sort the DataFrame by 'Hits' column in descending order
        df_sorted = filtered_people_df.sort_values('Hits', ascending=False)

        # Create a bar chart with the sorted data
        chart_data = pd.DataFrame({'Name': df_sorted['Name'], 'Hits': df_sorted['Hits']})
        st.bar_chart(chart_data.set_index('Name'))

        # Create the dropdown to select the person
        selected_person = st.selectbox("Select Person", filtered_people_df['Name'].unique())




        # TODO: this is not working. Ideally you'd be able to select one person of the above
        #  and see the evolution of "hits" in time
        if selected_person:
            # Filter the data for the selected person
            person_data = filtered_people_df[filtered_people_df['Name'] == selected_person]

            if not person_data.empty:
                # Group the data by period and calculate the sum of hits
                grouped_data = person_data.groupby('Period')['Hits'].sum().reset_index()

                # Create a line chart
                st.bar_chart(grouped_data.set_index('Period')['Hits'])
            else:
                st.write("No data available for the selected person.")

        # ###### Related Entities mentioned barchart ######

        st.write("Related Entities Mentioned")

        # Sort the DataFrame by 'Hits' column in descending order
        df_sorted = filtered_entities_df.sort_values('Hits', ascending=False)

        # Create a bar chart with the sorted data
        chart_data = pd.DataFrame({'Entities': df_sorted['Entities'], 'Hits': df_sorted['Hits']})
        st.bar_chart(chart_data.set_index('Entities'))

        # TODO: Similar to the above, ideally you'd be able to select one person of the above
        #  and see the evolution of "hits" in time

        st.write("Related Individuals and their positions")
        st.write(filtered_leader_df)

        # TODO: Lucy to add tables for themes.

        st.write("Theme tables")

    with tab2:

        st.subheader("Related people raw data")
        st.write(filtered_people_df)

        st.subheader("Related entities raw data")
        st.write(filtered_entities_df)

        st.subheader("Related leaders raw data")
        st.write(filtered_leader_df)


if __name__ == '__main__':
    main()

