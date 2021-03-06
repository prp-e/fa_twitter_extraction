import argparse
import twint

class Extractor:
    """This class is the main extractor"""
    def __init__(self, keyword):
        self.keyword = keyword 
    
    def extract(self):
        """This module helps us extract what we need."""
        config = twint.Config() 
        config.Search = self.keyword 
        config.Store_json = True 
        config.Limit = 1000 
        twint.run.Search(config)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--word', required=True, default="Trump")
    parser = parser.parse_args() 

    e = Extractor(parser.word)
    e.extract() 