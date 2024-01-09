# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Project 01 - YouTube Habits Analyser",
        page_icon="📹",
    )

    st.write("# Is my time on YouTube a waste or a learning experience?")

    st.sidebar.success("Select a demo above.")
    st.markdown(
        """
## 1. Project Brief

With the vast array of content on YouTube, understanding personal viewing habits can provide insightful revelations about interests and preferences. This project aims to conduct a personal analysis of the type of content consumed on YouTube, leveraging the capabilities of  YouTube API v3 and Python for data extraction and analysis.

## 2. Technology Stack

- **Language:** Python

- **API:** YouTube Data API v3

- **Libraries:** `Pandas` for data manipulation, `Matplotlib/Seaborn` for visualisation, `Requests` for API interaction

- **Dashboard Tool:** `Google Colab` Notebook or a web-based framework like Dash or `Streamlit` (v1.29.0, Release: Nov 30, 2023)


## 3. Objectives

1. **Data Collection:** Utilize YouTube API v3 to collect comprehensive data on videos watched, including titles, channels, categories, duration, and engagement metrics (likes, views, comments).
2. **Personal Viewing Profile:** Analyse the collected data to create a profile of personal YouTube consumption, identifying the most-watched categories, favourite channels, and prevalent themes.
3. **Trends and Patterns:** Investigate viewing patterns over time, such as preferred days for watching, average watch duration, and changes in content preferences.
4. **Interactive Dashboard:** Develop an interactive Python-based dashboard to visualise the analysis, allowing for dynamic filtering and exploration of the data.
5. **Insights and Recommendations:** Generate insights on personal content preferences and suggest potential new areas or channels of interest based on consumption patterns.

**Expected Outcomes:**

- A comprehensive understanding of personal YouTube content consumption patterns.

- Identification of potential new content areas based on existing preferences.

- Enhanced Python and data analysis skills through practical application.


## 4. Methodology
- **API Setup and Authentication**: Register the project in Google Cloud Console, enable YouTube Data API v3, and set up OAuth 2.0 credentials.
- **Data Extraction**: Write Python scripts using the Requests library to query the API and retrieve data on personal YouTube activity.
- **Data Processing**: Use Pandas for cleaning, transforming, and structuring the data into a suitable format for analysis.
- **Data Analysis**: Perform statistical and exploratory analysis to uncover patterns and trends in the viewing data.
- **Visualisation**: Create graphs, charts, and interactive elements to visually represent the findings.
- **Dashboard Development**: Assemble the visualizations into an interactive dashboard for easy exploration and analysis.
- **Insights Generation**: Interpret the data to offer insights into personal viewing habits and suggest new content areas.


## 5. Post (WhatsApp, LinkedIn)

**Project Selection Criteria**

- Take any area of your life you're "interested" in understanding more
- Get the data: personal, open source, fake (kaggle) or commercial
- Align the project to your area of work (consultancy/business/9-5)
- Write a project document (use a format relevant to your industry)
- Publish on platforms you intend to build your client base (Facebook, Twitter, LinkedIn, GitHub, etc.)

With more projects, you build a professional competence portfolio and proof of your skills/achievements; it's one thing to claim on your CV that you know something, and it's another to have a way to substantiate it.


## 6. Considerations/Appendix

- **GitHub Repo Naming Conventions:** https://github.com/bcgov/BC-Policy-Framework-For-GitHub/blob/master/BC-Gov-Org-HowTo/Naming-Repos.md
    """
    )


if __name__ == "__main__":
    run()
