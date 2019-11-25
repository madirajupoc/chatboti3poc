from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()
res = es.search(index="_all", body={'size':1,'query':{'match':{'Question':" super that is it"}}})
List_length = len(res['hits']['hits'])
if List_length > 0:
    score = len(res['hits']['hits'][0]['_source'])
    resonse1=(res['hits']['hits'][0]['_source']['Answer'])
    if score > 6: 
        print(resonse1)
    else:
        print("Score for returned message is %s"%resonse1)
        print("Score for this is  %s"%score)
else:
    print("No result fetched, Please rephrase your Query. For support contact qnabotsupport@spglobal.com ")