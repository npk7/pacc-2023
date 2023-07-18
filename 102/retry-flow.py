import httpx
from prefect import flow, task
from prefect.tasks import task_input_hash

@task(cache_key_fn=task_input_hash)
def fetchtask():
    cat_fact = httpx.get("https://httpstat.us/Random/200,500")
    cat_fact.raise_for_status()
    #if cat_fact.status_code >= 400:
    #    raise Exception()
    print(cat_fact.text)

@flow
def fetch():
    fetchtask()


if __name__ == "__main__":
    fetch()
