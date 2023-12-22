import scrapy
import os
import csv


class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["paper.people.com.cn"]
    
    start_urls = [
        "http://paper.people.com.cn/rmrb/html/2023-12/21/nbs.D110000renmrb_01.htm",
        "http://paper.people.com.cn/rmrb/html/2023-12/21/nbs.D110000renmrb_02.htm",
    ]

    def parse(self, response):
        base_url = 'http://paper.people.com.cn/rmrb/'

        i_url = response.css('div.paper img::attr(src)').get()
        image_url = base_url + i_url[9:]

        title = response.css('div.right p.title a::text').get()

        publish_date = response.css('div.right p.date.left::text').get().strip().split(',')[-1]

        body_items = response.css('ul.news-list a::text').getall()
        # body = '\n'.join(body_items)
        author = 'null'
        sub_title = 'null'

        add_data = {
            "Date": publish_date,
            "Title": title,
            "Image": image_url,
            "URL": response.url,
            "Body": body_items,
            "Author": author,
            "SubTitle": sub_title
        }

        
        # # Save the extracted data to a JSON file
        # with open("data.json", "w", encoding="utf-8") as jsonfile:
        #     json.dump(self.data, jsonfile, ensure_ascii=False, indent=4)


        # Save the extracted data to a CSV file
        self.save_to_csv(add_data)

    def save_to_csv(self, news_data):
        csv_file_path = 'news_data.csv'

        # Check if the CSV file exists
        is_file_empty = not os.path.isfile(csv_file_path) or os.stat(csv_file_path).st_size == 0

        with open(csv_file_path, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = news_data.keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write headers if the file is empty
            if is_file_empty:
                writer.writeheader()

            # Check if the data already exists in the CSV file
            with open(csv_file_path, 'r', newline='', encoding='utf-8') as check_file:
                reader = csv.DictReader(check_file)
                for row in reader:
                    if row["URL"] == news_data["URL"]:
                        # Data already exists, skip writing
                        return

            # Data doesn't exist, write to the CSV file
            writer.writerow(news_data)
