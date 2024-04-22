# data-visualization-project
QS World University Rankings Sankey Diagram
In this project, a Sankey diagram is created using QS World University Rankings data.

Dataset
The QS World University Rankings data is obtained from the following link:

[(https://www.kaggle.com/datasets/jkanthony/world-university-rankings-202223)]

The dataset contains universities' overall rankings and rankings based on various academic indicators.

Libraries Used
Pandas - For data analysis
Plotly - For data visualization

Creating the Sankey Diagram
The Excel dataset is read using Pandas and converted into a DataFrame.
Required columns are selected and data preprocessing is done.
Source, intermediate and target nodes are identified.
Node labels are concatenated to make them unique.
Each node is assigned an index.
Node and link colors are determined.
Dictionary in Plotly link format is created for each link.
All links are collected in a list.
Sankey diagram is created using Plotly.
Resulting Diagram
The generated Sankey diagram visualizes the relationship between universities' overall rankings and their rankings based on academic indicators. The left side of the graph shows the overall rankings and the right side shows the academic scores.

This project aims to visualize the relationships between different variables affecting university rankings using a Sankey diagram. The data used in this project is obtained from the "datacut.xlsx" or "data.xlsx" file, which contains information about universities' world rankings, academic reputation, faculty-student ratio, citations per faculty, international faculty, and international students. The Sankey diagram shows the flow of universities from the source (unnamed: 3) to the target (SCORE.8) through different intermediate ranks (RANK, RANK.1). The diagram also highlights the unique features of each university, such as academic reputation rank, faculty-student rank, citations per faculty rank, international faculty rank, and international students rank, using hovertemplates. The project is created using Python libraries such as pandas, plotly.graph_objects, and plotly.colors.You can view the project by visiting the link provided.

Usage
To generate the graph:

Install required libraries.
Download datas.xlsx file and add file path to the code.
Run main.py.
