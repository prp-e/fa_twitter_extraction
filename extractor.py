import argparse
import twint

class Extractor:
    """This class is the main extractor"""
    def __init__(keyword):
        self.keyword = keyword 
    
    def extract(self):
        """This module helps us extract what we need."""
        config = twint.Config() 
        config.Search = self.keyword 
        config.Store_json = True 
        config.Limit = 1000 
        config.run.Search() 

if __name__ == '__main__':
    print("Working on it!")