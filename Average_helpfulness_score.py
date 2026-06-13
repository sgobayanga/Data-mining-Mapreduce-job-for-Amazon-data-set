from mrjob.job import MRJob
import json
class Averagehelpfulnessscore(MRJob):
    def mapper(self,_,line):
        try:
            review=json.loads(line)
            helpful_votes=review.get("helpful_vote",0)
            total_votes= review.get("total_vote",0)
            if total_votes > 0:
                score=helpful_votes/total_votes
                yield "all",(score,1)
        except:
            pass
    def reducer(self,key,value):
        total_score = 0
        total_count= 0
        for score,count in value:
            total_score += score
            total_count += count
        if total_count > 0:
            yield "average_helpfulness",(total_score/total_count)

if __name__ == "__main__":
    Averagehelpfulnessscore.run()

