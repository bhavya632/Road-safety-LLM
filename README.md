# Road Safety Intelligence with Augmented LLM

Welcome to the **Road Safety Intelligence with Augmented LLM** project, developed as part of the Fall 2024 AI Studio program in collaboration with Michelin Mobility Intelligence.

## Project Overview
This project aims to make geospatial analysis more accessible by leveraging a natural language interface integrated with AI-powered tools. It enables users to analyze road safety data through interactive maps and a knowledgeable chatbot, enhancing insights into accident-prone areas, harsh driving behaviors, and road safety patterns.

## Objectives and Goals
1. Automate spatial data collection, analysis, and visualization.
2. Enable natural language queries to extract meaningful insights from geospatial datasets.
3. Showcase the potential of using generative AI models to enhance user experience and geospatial analysis.
4. Empower stakeholders such as public authorities and fleet managers to reduce crashes and fatalities.

## Methodology
The project follows a structured approach:

1. **Data Understanding & Preparation**:
   - Analyzed datasets, including crash data and harsh acceleration patterns.
   - Preprocessed data using pandas, handling missing values and removing irrelevant columns.
2. **Model Development**:
   - Tested various GPT models, starting from GPT-2 to Ollama's surveying and mapping model.
   - Employed LangChain for prompt engineering and dynamic query generation.
3. **Application Development**:
   - Created an interactive Streamlit application that integrates the Ollama LLM for real-time user queries.
4. **Evaluation**:
   - Compared model outputs to assess accuracy, relevance, and usability for geospatial tasks.

## Results and Key Findings
- The Ollama surveying and mapping model excelled in understanding dataset structures and generating code for advanced tasks like mapping.
- The application successfully converts user queries into actionable insights, such as identifying accident-prone areas or visualizing driving behavior patterns.
- Demonstrated the potential of LLMs in automating geospatial analysis.

### Visualizations
- Interactive maps for accident hotspots.
- Clustered visualizations of harsh driving behaviors.

## Potential Next Steps
1. Enhance prompt engineering to improve model accuracy and reduce variability in responses.
2. Integrate multi-dataset analysis capabilities.
3. Deploy the application to a cloud environment for better performance.
4. Implement direct code execution within the Streamlit interface for seamless user interaction.

## Installation Instructions

### Prerequisites
- Python 3.8+
- pip
- Streamlit
- pandas
- langchain
- Ollama

### Setup
1. Clone the repository:
   ```bash
   git clone git@github.com:Michelin-Mobility-BTTAI-Team-23/Road-Safety-LLM.git
   cd Road-Safety-LLM
   ```
2. Install dependencies:
   - Install Python: https://kinsta.com/knowledgebase/install-python/
   - Install pip: https://pip.pypa.io/en/stable/installation/
   - Install Streamlit: https://docs.streamlit.io/get-started/installation
   - Install Pandas: https://pandas.pydata.org/docs/getting_started/install.html
   - Install LangChain: https://python.langchain.com/v0.1/docs/get_started/installation/
   - Install LangChain's Ollama Package: https://python.langchain.com/docs/integrations/providers/ollama/
   - Install Ollama: https://ollama.com/
  
3. Install and run Ollama Surveying and Mapping
  ```bash
  ollama pull ALIENTELLIGENCE/surveyingandmapping
  ollama serve
  ```
5. Run the application:
   ```bash
   streamlit run streamlit_app.py
   ```

### Sample Dataset
Place the sample datasets in the `/datasets` folder. Example files:
- `Crash_data_LA_county.csv`
- `Harsh_Acceleration_Severity_Ranking.csv`
---
For any questions or contributions, please reach out to the project maintainers or open an issue in this repository.
