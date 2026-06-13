from mrjob.job import MRJob
import json
class AverageRatingPerProduct(MRJob):
    def mapper(self,_,line):
        try:
            reviews=json.loads(line)
            asin=reviews.get("asin")
            rating=reviews.get("rating")
            if asin and rating is not None:
                yield asin,(float(rating),1)
        except:
            pass
    def reducer(self,asin,values):
            total_rating=0
            total_count=0
            for rating, count in values:
                total_rating+= rating
                total_count+= count
            if total_count > 0:
                average_rating=total_rating/total_count
                yield asin,average_rating
if __name__=="__main__":
    AverageRatingPerProduct.run()







