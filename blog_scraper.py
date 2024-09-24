import requests
from scrapy.http import HtmlResponse
import os
import json
output_dir = "output"
# Create output folder in the current directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def blog_scraper():
    url_list = [
        # "https://substack.thewebscraping.club/sitemap/2022",
        "https://substack.thewebscraping.club/sitemap/2023",
        # "https://substack.thewebscraping.club/sitemap/2024",
        ]
    output_list = []
    for url in url_list:
        response = requests.get(url=url)
        if response.status_code == 200:
            response = HtmlResponse(url="",body=response.content,encoding='utf-8')
            sitemap_urls =  response.xpath('//p//a/@href').getall()
            for blog_url in sitemap_urls:
                blog_response = requests.get(url=blog_url)
                if blog_response.status_code == 200:
                    blog_response = HtmlResponse(url="",body=blog_response.content,encoding='utf-8')
                    item = {}
                    title = blog_response.xpath('//div[@class="post-header"]//h1//text()').get()
                    subtitle = blog_response.xpath('//div[@class="post-header"]//h3//text()').get()
                    blog_content = blog_response.xpath('//div[@class="available-content"]//p/text()').getall()
                    full_content = "\n".join(blog_content)
                    post_date = blog_response.xpath('//div[@class="post-header"]//h3[@class="subtitle"]/./following::div//div//text()').getall()
                    if post_date:
                        post_date = post_date[1]
                    item["title"] = title
                    item["subtitle"] = subtitle
                    item["blog_content"] = full_content
                    item["post_date"] = post_date
                    item["blog_url"] = blog_url
                    print("here item..",item)
                    output_list.append(item)

                else:
                    print("blog page url not get response",blog_response.status_code)
        else:
            print("sitemap url not get response",response.status_code)
    # Save the output list as a JSON file
    file_path = os.path.join(output_dir, f"output_list.json")
    with open(file_path, "w", encoding='utf-8') as json_file:
        json.dump(output_list, json_file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    blog_scraper()
