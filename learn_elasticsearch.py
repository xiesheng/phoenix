# -*- coding: utf-8 -*-
from datetime import datetime
from elasticsearch import Elasticsearch, NotFoundError, ConnectionTimeout
from timeit import default_timer as timer
from multiprocessing import Pool, cpu_count
import uuid
import json
import os


f = open("response.json")
data = json.load(f)
f.close()


def create_doc(num_of_doc):
    created_cnt = 0
    es = Elasticsearch(["http://localhost:9200", "http://localhost:9201", "http://localhost:9202"], http_compress=True)
    for i in range(num_of_doc):
        doc = {
            "session_id": uuid.uuid4(),
            "user_id": "seamus_xie",
            "text": "Elasticsearch: cool. bonsai cool.",
            "timestamp": datetime.now(),
            "data": data
        }
        try:
            res = es.index(index="chatbot01", body=doc)
            if res['result'] == "created":
                created_cnt += 1
        except ConnectionTimeout as err:
            print(f"{os.getpid()}:", err)
        finally:
            continue

    return created_cnt


def batch_create():
    ret_, cnt = [], 0
    num_of_process = cpu_count()
    docs = []
    for i in range(500):
        docs.append(200)

    with Pool(num_of_process) as pool:
        ret_ = pool.map(create_doc, docs)

    for n in ret_:
        cnt += n

    return len(ret_), cnt


if __name__ == "__main__":
    print(f"main process:{os.getpid()}, cpu_count:{cpu_count()}")
    start = timer()
    num_of_batch, num_of_doc = batch_create()
    end = timer()
    millisecond_per_doc = round((end - start)*1000/num_of_doc, 2)
    print(f"millisecond_per_doc: {millisecond_per_doc}ms, elapsed time:{round(end - start, 2)}s, num_of_batch:{num_of_batch}, num_of_doc:{num_of_doc}")
