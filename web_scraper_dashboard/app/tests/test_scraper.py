import unittest
from app.scraper import scrape_website

class TestScraper(unittest.TestCase):
    def test_scrape_website(self):
        data = scrape_website()
        self.assertIsNotNone(data)
        self.assertIn('title', data)
        self.assertIn('description', data)
        self.assertIn('price', data)

if __name__ == '__main__':
    unittest.main()
