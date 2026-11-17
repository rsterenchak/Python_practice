import requests


def get_incomplete_task_ids(user_id):

    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params={"userId":user_id},
        timeout=10
    )

    response.raise_for_status() # lookup what this line does

    tasks = response.json()

    # print(tasks)

    incomplete_task_ids = []

    # Current: Collect the IDs of incomplete tasks for the userId:1 into a list, then print the list
    for task in tasks:

        if task['completed'] == False:
            incomplete_task_ids.append(task['id'])
        
    return incomplete_task_ids

# TEST API Call
result1 = get_incomplete_task_ids(1)

print(result1)


# for page in range(2, total_pages + 1):

#     response = requests.get(
#         url,
#         params={"page":page},
#         timeout=10

#     )

# response.raise_for_status()

# payload = response.json()





