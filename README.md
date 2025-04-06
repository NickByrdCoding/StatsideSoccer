## Statside Soccer

Statside Soccer is a managerial tool providing soccer coaches with insights and trends from individual games.
The tool provides insights into three categories of play:

- General Play: This focuses overall trends of the game, specifically the expected threat and pass frequency in each zone (there are 15 zones, split by the five channels and thirds of the pitch).
- Under Pressure: This provides key information and insights about the team's performance when opponents are pressing them, along with visual animations of key moments where the team faced pressure.
- Threatening Plays: Similar to the under pressure tab, this tab provides key information, insights, and video simulation. The information on this tab tracks different combinations on the field that led to a high x_threat

For this project, we used Matplotlib, including mplsoccer, to visualize plots and the pitch. We also used Flask for integrating our visualizations into our web page, and the Google Gemini API for summarizing our insights. We decided to separate the analysis side of our backend from the frontend, which helped us to separate concerns and improve the scalability of our project. While our frontend is focused on one soccer match, our backend allows us to easily generate analysis of other matches.

## How to use

- Backend Setup:
  - Upload both "passing_options.csv" and "player_possession.csv" for a single match tracked by SkillCorner
  - Install the following dependencies: pandas, matplotlib, google-genai
  - Get a Google Gemini API key for free from https://aistudio.google.com/apikey and enter into last cell of the Jupyter notebook (collect_data.ipynb)
  - Change team_id in the notebook to the team being tracked
  - Run the Jupyter notebook
- Frontend Setup:
  - Ensure Flask is downloaded and make sure to open the directory that contains app.py. To run from flask, type python3 app.py / python app.py into the terminal and then wait for the terminal to prompt you with a link to a local host. Putting this into your browser will allow you to run the files locally.
