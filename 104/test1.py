from prefect import flow

@flow()
def hello_world():
    print("Hello World of Prefect!")

hello_world()
