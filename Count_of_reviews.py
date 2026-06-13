from mrjob.job import MRJob
import json
import re
class Reviewcountperproduct(MRJob):
     def mapper(self,_,line):
       try:
         reviews=json.loads(line)
         asin=reviews.get("asin")
         if asin:
               yield asin,1
       except:
        pass
     def reducer(self,asin,counts):
          yield asin,sum(counts)
if __name__== "__main__":
    Reviewcountperproduct.run()




