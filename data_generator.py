import pandas as pd
import numpy as np
import streamlit as st
import os


def related_people():
    # Check if data file already exists
    if os.path.exists('people_data.csv'):
        # If it does, load the data from the file
        df = pd.read_csv('people_data.csv')
    else:
        # List of business associates of Bernard Arnault
        names = ["François-Henri Pinault", "Sidney Toledano", "Jean-Paul Agon", "Rupert Murdoch",
                 "Mel Gibson", "Elon Musk", "Jeff Bezos"]

        # Let's create 20 more random names
        more_names = ["Person_" + str(i) for i in range(1, 21)]

        # Add the new names to the original list
        names.extend(more_names)

        # Generate a list of random numbers between 0 and 100
        numbers = [np.random.uniform(0, 100) for _ in range(len(names))]

        # Round the numbers to the nearest significant figure
        numbers = [round(num, -int(pd.np.floor(pd.np.log10(abs(num))))) for num in numbers]

        # Generate a list of random news sources
        news_sources = ["NewsSource_" + str(i) for i in range(1, len(names) + 1)]

        # Generate random time periods
        time_frames = ['Last week', 'Last month', 'Last 2 months']
        period = np.random.choice(time_frames, len(names))


        # Create a dataframe
        df = pd.DataFrame(list(zip(names, numbers, news_sources, period)),
                          columns=['Name', 'Hits', 'News Source', 'Period'])

        df.to_csv('people_data.csv', index=False)

    return df

@st.cache(allow_output_mutation=True)
def related_entities():

    if os.path.exists('entities_data.csv'):
        # If it does, load the data from the file
        df = pd.read_csv('entities_data.csv')
    else:

        related_entities_list = [
            "Kering",
            "Gucci",
            "Saint Laurent",
            "Bottega Veneta",
            "Balenciaga",
            "Alexander McQueen",
            "Puma",
            "Volcom",
            "Boucheron",
            "Ulysse Nardin",
            "Girard-Perregaux",
            "Brioni",
            "Sowind Group",
            "La Redoute",
            "Fnac",
            "Conforama",
            "CFAO",
            "Christie's",
            "Stella McCartney",
            "Qeelin",
            "Yves Saint Laurent Beauté",
            "Sergio Rossi",
            "Château Latour",
            "Château Grillet",
            "Château-Brane-Cantenac",
            "Château-Latour-Martillac",
            "Château-Bellevue",
            "Groupe Artémis",
            "Teleperformance",
            "Le Point",
            "Le Monde"
        ]

        # Generate skewed numbers between 1 and 100
        skewed_numbers = np.random.gamma(2, 10, len(related_entities_list))
        skewed_numbers = skewed_numbers / np.max(skewed_numbers) * 100
        skewed_numbers = np.round(skewed_numbers).astype(int)

        # Generate random time periods
        time_frames = ['Last week', 'Last month', 'Last 2 months']
        period = np.random.choice(time_frames, len(related_entities_list))

        # Generate list of made-up sources
        sources = ["Source_" + str(i) for i in range(1, len(related_entities_list) + 1)]

        # Create DataFrame
        df = pd.DataFrame({
            'Entities': related_entities_list,
            'Hits': skewed_numbers,
            'Sources': sources,
            'Period': period,
        })

        df.to_csv('entities_data.csv', index=False)

    return df

@st.cache(allow_output_mutation=True)
def related_leaders():

    if os.path.exists('leaders_data.csv'):
        # If it does, load the data from the file
        df = pd.read_csv('leaders_data.csv')
    else:

        # List of random famous business figures
        people = [
            "Elon Musk",
            "Warren Buffett",
            "Jeff Bezos",
            "Bill Gates",
            "Mark Zuckerberg",
            "Larry Page",
            "Tim Cook",
            "Satya Nadella",
            "Jack Ma",
            "Richard Branson"
        ]

        # Link to an organization
        links = [
            "CEO",
            "CFO",
            "President",
            "Chairman",
            "Founder",
            "Director",
            "Board Member",
            "Executive",
            "Investor",
            "Advisor"
        ]

        # Entities they're related to
        entities = [
            "Tesla",
            "Berkshire Hathaway",
            "Amazon",
            "Microsoft",
            "Facebook",
            "Alphabet",
            "Apple",
            "Microsoft",
            "Alibaba",
            "Virgin Group"
        ]

        # Generate random numbers between 1 and 50
        hits = np.random.randint(1, 51, len(people))

        # Generate list of made-up sources
        sources = ["Source_" + str(i) for i in range(1, len(people) + 1)]

        # Generate random time periods
        time_frames = ['Last week', 'Last month', 'Last 2 months']
        period = np.random.choice(time_frames, len(people))

        # Create DataFrame
        df = pd.DataFrame({
            'People': people,
            'Link': links,
            'Entity': entities,
            'Hits': hits,
            'Source': sources,
            'Period': period,
        })

        df.to_csv('leaders_data.csv', index=False)

    return df
