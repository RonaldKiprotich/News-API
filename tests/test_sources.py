import unittest
from app.models import Sources

class SourcesTest(unittest.TestCase):
    '''
    Class to test the behaviour of the source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources("Find the latest breaking news and information on the top stories, weather, business, entertainment, politics, and more" , "https://edition.cnn.com/")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))


if __name__ == '__main__':
    unittest.main()