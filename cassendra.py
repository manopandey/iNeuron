from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
        'secure_connect_bundle': './secure-connect-ineuron.zip'
}
auth_provider = PlainTextAuthProvider('MwvGmEOlZFejSOvRDcUtJksv', 'DRhIUyflGsl4KYE+bPxWTsMEcC6sOEUjJmE.suKzN,.au2rK.UPzPzoSyMtkQ4+LZ4HijD6Y-ouH5azI.X6ikEWa,4s5GFqZmOInJQKCtsxcywOLKBrwr58XQXQEkTXm')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

for i in range(10):

        session.execute("insert into test.emp (emp_id,emp_name,emp_city,emp_sal,emp_phone) values (00"+str(i)+",'mano','singapore',"+str(i)+"0000,65732569);").one()
        print("Executed",i)


