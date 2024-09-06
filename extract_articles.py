from newspaper import Article

urls = [
    "http://cnn.com/2023/03/29/entertainment/the-mandalorian-episode-5-recap/index.html",
    "https://www.cnn.com/2023/06/09/entertainment/jurassic-park-anniversary/index.html"
]

with open("articles.md", "w") as file:
    for url in urls:
        article = Article(url)
        article.download()
        article.parse()
        file.write(f"## Title: {article.title}\n\n")
        file.write(f"{article.text[:1000]}\n\n")  # Write the first 1000 characters
import inspect
from newspaper import Article

# Inspect newspaper Article function
print(inspect.getsource(Article))
