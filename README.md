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

Some key observations from the graph:

There is a high correlation between overall ranking and academic scores.
However, some universities have academic scores above or below their overall rankings.
Larger universities are mostly top ranked in both overall ranking and academic indicators.

Usage
To generate the graph:

Install required libraries.
Download datas.xlsx file and add file path to the code.
Run main.py.
