import scrapy
import csv
from src.telegramlearning import path_to_csv
class CoursemetrySpider(scrapy.Spider):
    name = 'coursetreat'
    start_urls = ['https://coursetreat.com/udemy']
    data_to_write = []  # Define data_to_write in the class scope

    def parse(self, response):
        courses = response.css('div.col-12.col-md-6.col-lg-3.text-center')
        for course in courses:
            link = course.css('a::attr(href)')
            yield response.follow(link.get(), callback=self.detail_pass)

    def detail_pass(self, response):
        allinone = list(filter(lambda x: len(x) > 0, map(lambda x: x.strip().replace('\n', ''), response.css('div.col-12.col-md-6.col-lg-4.blogset p::text').getall())))
        if len(allinone) == 5:
            instructor = allinone[3]
            description = allinone[4]
            students = allinone[2].split()[0]
        elif len(allinone) == 4:
            instructor = allinone[2]
            description = allinone[3]
            students = 'Undefined'
        else:
            return  # Skip if data is not in the expected format

        language = allinone[1]
        A = ["English", "Turkish"]
        if language in A:
            mine = {
                'language': language,
                'name': response.css('div.col-12.mb-2 h3::text').get().strip(),
                'description': description,
                'category': allinone[0],
                'students': students,
                'instructor': instructor,
                'link': response.css('div.row.text-center.mt-5 a::attr(href)').get()
            }
            self.data_to_write.append(mine)  # Append to the class variable

    def closed(self, reason):
        # Write all data to the CSV file when the spider is closed
        with open(path_to_csv, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['language', 'name', 'description', 'category', 'students', 'instructor', 'link']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header
            writer.writeheader()

            # Write all data
            writer.writerows(self.data_to_write)
