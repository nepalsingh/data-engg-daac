# added new folder to databasicks workspace using databricks api

# Path: lab/data-engineering/data-engg-daac/databricks/code/get-files.py
# Compare this snippet from lab/data-engineering/data-engg-daac/databricks/code/use-databricks-api.py:
#


from databricks_api import DatabricksAPI
import os

databrickshost = os.getenv('DATABRICKS_HOST')
databricks_token = os.getenv('DATABRICKS_TOKEN')
# databricks_cluster_id = os.getenv('DATABRICKS_CLUSTER_ID')

api = DatabricksAPI(host=databrickshost, token=databricks_token)

get_cluster = api.cluster_list()
print(get_cluster)

ws_root = '/Shared/auto'


def get_files(directory):
    directory_list = []
    files_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py' or '.ipynb' or '.sql'):
                dir_path = os.path.join(root, file).split('/')[1:-1]
                # print(os.path.join(root, file), dir_path)
                files_list.append(os.path.join(root, file))
                if dir_path:
                    directory_list.append('/'.join(dir_path))
    # print(set(directory_list))
    # print(set(files_list))

    for dir in set(directory_list):
        print(dir)
        api.workspace_mkdirs(ws_root + '/' + dir)
    for file in set(files_list):
        print(file)
        api.workspace_import(ws_root + '/' + file, file, overwrite=True)
