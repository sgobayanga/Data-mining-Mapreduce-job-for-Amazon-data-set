import random
import json
from mrjob.job import MRJob
from nltk.sentiment import SentimentIntensityAnalyzer

class SentimentAnalyzer(MRJob):

    def mapper_init(self):
        self.sia = SentimentIntensityAnalyzer()

    def mapper(self, _, line):
        try:
            # 🔥 SAMPLE FILTER (put it FIRST)
            if random.random() > 0.1:   # keeps only 10% of data
                return

            review = json.loads(line)
            text = review.get("text", "")

            if not text:
                return

            score = self.sia.polarity_scores(text)["compound"]

            if score >= 0.05:
                yield "positive", 1
            elif score <= -0.05:
                yield "negative", 1
            else:
                yield "neutral", 1

        except:
            pass

    def reducer(self, sentiment, counts):
        yield sentiment, sum(counts)

if __name__ == "__main__":
    SentimentAnalyzer.run()