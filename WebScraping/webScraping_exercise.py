import requests
from bs4 import BeautifulSoup
import pprint


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k["votes"], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get("href", None)
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                hn.append({"title": title, "link": href, "votes": points})
    return sort_stories_by_votes(hn)


if __name__ == "__main__":
    base = "https://news.ycombinator.com/news"
    pages = [base]
    for i in range(2,4):
        pages.append(base + f"?p={i}")
    
    mega_links = []
    mega_subtext = []  
    for page in pages:
        res = requests.get(page)
        soup = BeautifulSoup(res.text, "html.parser")
        links = soup.select(".titleline > a")  # heads up! .storylink changed to .titleline
        subtext = soup.select(".subtext")
        
        mega_links += links
        mega_subtext += subtext
        

    pprint.pprint(create_custom_hn(mega_links, mega_subtext))
