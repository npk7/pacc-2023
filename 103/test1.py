from prefect import flow, task

@task
def task1():
	print("I am task1")

@task
def task2():
	task1.fn()
	print("I am task2")

@flow
def flow1():
	task1()
	task2()

if __name__ == "__main__":
	flow1()
