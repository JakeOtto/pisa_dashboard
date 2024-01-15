Group project for Abbas, Shirin, Joe and Jake

Developing pipelines and insights dashboard for the 2018 PISA survey results

- GEI - Global Education Insights - has recently acquired the PISA 2018 dataset, a comprehensive survey of student performance in various countries.

- This dataset contains a wealth of information that could help GEI understand the factors that contribute to student success and identify areas where education systems could be improved.

- However, the dataset is large and complex, making it difficult for GEI's team to extract meaningful insights from it.

- So Naturally they have sought our help, 

- Utilising great data engineering practices we have designed, developed and implemented a data pipeline and dashboard for GEI that will stream line analytical insights on the dataset.

- An initial investigation into the data showed us that even though the data sets were large, they were relatively clean with a low standard deviation, stemming from the discrete quantitative results of PISA’s survey 

- This allowed us to aggregate and utilise data directly without much transformation into 5 comparable metrics with a dashboard for their presentation 

- Deciding on a robust scaleable approach that could continue to handle new information as it arrived, a EC2 deployed Relational database provided a constant access point for the team whilst allowing the dashboard to be updated at anytime.

- Postgres, Apache Airflow and Flask were the tools that we utilised to develop this solution, 
