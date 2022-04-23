import psycopg2

def test_database():
    conn = psycopg2.connect(dbname='tracking_stats', user='postgres', 
                            password=',jnhfzlj', host='82.146.40.163')
    cursor = conn.cursor()
    cursor.execute("select * from tracking_stats_table limit 1")
    assert conn != None
    assert cursor != None
    assert cursor.fetchall() != []