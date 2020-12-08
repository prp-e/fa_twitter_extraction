import twint

class Extractor:
    def __init__(keyword):
        self.keyword = keyword 
    
    def extract(self):
        config = twint.Config() 
        config.Search = self.keyword 
        config.Store_json = True 
        config.run.Search() 

if __name__ == '__main__':
    print("Working on it!")