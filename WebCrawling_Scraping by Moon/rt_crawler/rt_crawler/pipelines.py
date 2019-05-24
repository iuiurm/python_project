# pipelines.py

import pandas as pd


class RTPipeline(object):

    def __init__(self):
        self.df = pd.DataFrame(columns=["year", "title", "score"])

    def process_item(self, item, spider):
        self.df = self.df.append({"year": item["year"],
                                  "title": item["title"],
                                  "score": item["score"]
                                 }, ignore_index=True)
        print("year : {}".format(item["year"]))
        return item

    def close_spider(self, spider):
        self.df.to_csv("./df_new.csv", index=False)

