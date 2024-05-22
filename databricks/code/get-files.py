# get file directory and create directory and loop thru the fle

import os
import requests

# get diranme from the file path

# get directory only for the file path and show releative path
print(os.path.dirname(__file__))


print(os.path.dirname(__file__))


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
    for file in set(files_list):
        print(file)
    for dir in set(directory_list):
        print(dir)


async def call_databricks_api(directories: list, files: list):
    # set the databricks token
    token = os.getenv('DATABRICKS_TOKEN')
    # set the databricks host
    host = os.getenv('DATABRICKS_HOST')
    # set the databricks cluster id
    cluster_id = os.getenv('DATABRICKS_CLUSTER_ID')

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # set the databricks api url
    mkdir_url = f'https://{host}/api/2.0/workspace/mkdirs'

    for dir in directories:
        # set the databricks api url
        mkdir_url = f'https://{host}/api/2.0/workspace/mkdirs'
        # set the databricks headers

        # set the databricks payload
        payload = {
            'path': dir
        }
        # call the databricks api
        response = await requests.post(mkdir_url, headers=headers, json=payload)
        # print the response
        print(response.json())

    for file in files:
        # set the databricks api url
        import_url = f'https://{host}/api/2.0/workspace/import'
        # set the databricks headers
        headers = {
            'Authorization': f'Bearer {token}'
        }
        # set the databricks payload
        payload = {
            'path': file,
            'content': open(file, 'rb').read(),
            'overwrite': True
        }

        # call the databricks api
        response = await requests.post(import_url, headers=headers, json=payload)
        # print the response
        print(response.json())

    #
get_files('.')
