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
    hacker_news = "https://news.ycombinator.com/news"

    res = requests.get(hacker_news)
    res.text

    soup = BeautifulSoup(res.text, "html.parser")
    # print(soup)
    # print("-" * 20)
    # print(soup.body)
    # print("-" * 20)
    # print(soup.body.contents) # type: ignore
    links = soup.select(".titleline > a")
    subtext = soup.select(".subtext")
    posts = create_custom_hn(links, subtext)

    mega_links = links
    mega_subtext = subtext

    pprint.pprint(create_custom_hn(mega_links, mega_subtext))
