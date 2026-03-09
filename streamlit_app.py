"""
This module provides a web application for analyzing road safety data using AI-powered 
insights. It uses Streamlit for the user interface, pandas for data handling, and the 
Langchain library with Ollama LLM to process natural language queries about road safety 
datasets. The application allows users to input questions related to the datasets, with 
the LLM providing answers or executing code when necessary.

Key features:
- Loads two datasets: one with crash data and one with acceleration severity data.
- Preprocesses the crash data by removing rows with missing values and unnecessary columns.
- Allows users to input natural language questions about the data.
- Uses the Ollama LLM model to generate responses, with special handling for geospatial data 
  and code execution.
- Displays answers and, if applicable, executes any generated code and presents the result 
  in the app.

Dependencies:
- `streamlit`: For creating the interactive web interface.
- `pandas`: For data manipulation and handling.
- `langchain_ollama`: For integrating the Ollama LLM to process user queries.
- `langchain_core`: For prompt templates and managing callback handlers.
- `langchain.callbacks.streaming_stdout`: For streaming output in the console.

The user interface consists of:
- A title and description introducing the app.
- A text input for users to enter questions related to the datasets.
- Dynamic processing of the input question, where the app queries the relevant dataset and 
  returns answers, or dynamically executes code if requested.

The app handles potential errors gracefully, providing feedback to the user in case of issues 
during query processing or code execution.

File paths for the test datasets:
- Crash data: `/home/mfox/Road-Safety-LLM/Datasets/Crash data_LA_county.csv`
- Harsh acceleration severity data: `/home/mfox/Road-Safety-LLM/Datasets/Harsh 
  Acceleration_Severity_Ranking_Clustering_LA_COUNTY_H10.csv`
"""

import streamlit as st
import pandas as pd
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# Load datasets
crash_df = pd.read_csv("/home/mfox/Road-Safety-LLM/Datasets/Crash data_LA_county.csv")
acceleration_df = pd.read_csv(
    "/home/mfox/Road-Safety-LLM/Datasets/Harsh Acceleration_Severity_Ranking_Clustering_"
    "LA_COUNTY_H10.csv"
)

# Preprocess the crash dataset
null_row = crash_df[crash_df.isnull().any(axis=1)]
crash_df.drop(null_row.index, inplace=True)
crash_df.drop(columns="ARC_ID", inplace=True)

# Set pandas options to avoid truncated output
pd.set_option("display.max_columns", None)

# Initialize constants
DATAFRAME_NAME = "crash_df"

# Initialize LLM for geospatial data
geospatial_llm = OllamaLLM(
    model="ALIENTELLIGENCE/surveyingandmapping",
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
)

# Streamlit UI setup
st.title("Road Safety Insights with AI")
st.write(
    "Ask questions about the datasets and receive answers powered by the Ollama LLM."
)

# User input
user_question = st.text_input("Enter your question about the dataset:")

if user_question:
    TEMPLATE = """Question: Using the dataframe {dataframe}, answer this question: {question}

    Answer: The dataframe is a pandas dataframe called {name}.
    If addresses are asked for, generate code using Nominatim to find them.
    If a map is asked for, use plotly to generate it."""

    prompt = ChatPromptTemplate.from_template(TEMPLATE)
    chain = prompt | geospatial_llm

    with st.spinner("Processing your question..."):
        try:
            result = chain.invoke(
                {
                    "dataframe": crash_df,
                    "name": DATAFRAME_NAME,
                    "question": user_question,
                }
            )
            # Code used to attempt running code in the website below
            # We were never able to get it working

            # if "```python" in result and result.strip().endswith("```"):
            #     start_index = result.find("```python") + len("```python")
            #     end_index = result.rfind("```")
            #     code = result[start_index:end_index].strip()

            #     try:
            #         # Save code to a temporary file
            #         with open("temp_script.py", "w") as f:
            #             f.write(code)

            #         # Run the script using subprocess and the current Python executable
            #         process = subprocess.run(
            #             [sys.executable, "temp_script.py"],
            #             capture_output=True,
            #             text=True,
            #             check=True,
            #         )

            #         if process.returncode == 0:
            #             st.write("Executed Code Output:")
            #             st.write(process.stdout)
            #         else:
            #             st.error(f"Error in script execution: {process.stderr}")
            #     except Exception as e:
            #         st.error(f"Error executing the code: {e}")
            # else:
            st.success("Here's the result:")
            st.write(result)
        except Exception as e:  # pylint: disable=broad-exception-caught
            st.error(f"Error: {e}")

# # Calculate accident-prone locations
# if st.button("Find High Pedestrian Accident Areas"):
#     st.write("### Identifying Accident-Prone Areas")

#     accidents_by_location = crash_df.groupby(['LATITUDE', 'LONGITUDE']).sum()
#     locations_with_ped_accidents = accidents_by_location[accidents_by_location['PED'] > 3]
#     top_10_locations = locations_with_ped_accidents.sort_values(by='PED', ascending=False).head(10)

#     addresses = top_10_locations.index.tolist()
#     st.write("Top 10 Locations with High Pedestrian Accidents:", addresses)

#     if addresses:
#         geoloc = Nominatim(user_agent='GetLoc')
#         add_list = []

#         for address in addresses:
#             try:
#                 lat, lon = address
#                 locname = geoloc.reverse((lat, lon), language='en', timeout=10)
#                 add_list.append(locname.address if locname else "Address not found")
#             except Exception as e:
#                 add_list.append(f"Error: {e}")
#             time.sleep(1)

#         st.write("Addresses for Top Locations:")
#         for location, addr in zip(addresses, add_list):
#             st.write(f"Location: {location} => Address: {addr}")
#     else:
#         st.error("No locations found with more than 3 pedestrian accidents.")
