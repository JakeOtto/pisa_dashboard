from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook
from psycopg2.extras import execute_values


# --------SETUP DAG-----------
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'AA-total-submissions',
    default_args=default_args,
    description='Extract source RDS data, transform, and load into analytical RDS data',
    schedule_interval=timedelta(seconds=10),
    start_date=datetime(2024, 1, 8),
    catchup=False,
    max_active_runs = 1
)


db_list = ['alb','arg','aus','aut','bel','bgr','bih','blr','bra','brn','can','che','chl','col','cri','cze','deu','dnk','dom', 'esp']

def extract_and_load_data(**kwargs):
    count = 0
    for db in db_list:

        source_hook = PostgresHook(postgres_conn_id=f'group_proj_{db}')
        total_submissions_query = """
            SELECT COUNT(cnt) 
            FROM responses
        """
        cnt_count = source_hook.get_records(sql=total_submissions_query)
        print("count: ", count)
        print("cnt_count: ", cnt_count)
        count += cnt_count[0][0]
        print("updated cnt_count: ", cnt_count)

    print("final_count: ", count)
    # Load data into destination RDS table
    destination_hook = PostgresHook(postgres_conn_id='educational-insights-dest')

    # Insert new data
    update_data_query = """
    UPDATE total_submissions
    SET count = %s;
    """
    destination_hook.run(sql=update_data_query, parameters=[int(count)])
    print("inserted count")


# ----------DEFINE TASK----------
extract_and_load_data_task = PythonOperator(
    task_id='extract_and_load_data_task',
    python_callable=extract_and_load_data,
    provide_context=True,
    dag=dag,
)

# ----------SET THE TASK DEPENDENCIES----------
extract_and_load_data_task
