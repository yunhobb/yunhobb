import feedparser

blog_url = "https://yunhobb.github.io/feed.xml"
rss_feed = feedparser.parse(blog_url)

MAX_NUM = 3

latest_posts = ""

for idx, entrie in enumerate(rss_feed['entries']):
  if idx > MAX_NUM:
     break;
  feed_date = entrie['published_parsed']
  latest_posts += f" - [{feed_date.tm_mon}/{feed_date.tm_mday} - {entrie['title']}]({entrie['link']})\n"

print(latest_posts)

preREADME = """
<div align=center>
	<img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=header&text=Jung,%20%Yunho&fontSize=90" />	
</div>

<h3 align="center">🛠️ Now I'm learning 🛠️ </h3>

<p align="center">
    <img src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=OpenJDK&logoColor=white"/>
    <img src="https://img.shields.io/badge/Spring-6DB33F?style=for-the-badge&logo=Spring&logoColor=white"/>
    <img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white"/> 

<br>
<br>
</p>

<div align=center>
<img src="https://github-readme-stats.vercel.app/api?username=yunhobb&show_icons=true">

<div>




[![Resume](https://img.shields.io/badge/Notion-%23000000.svg?style=flat-square&logo=notion&logoColor=white)](https://pouncing-beluga-df8.notion.site/Jung-Yunho-a3c5c3554522401ea8f4c5ce1251d58b)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:a01049048063@gmail.com)
[![GitHub](https://img.shields.io/badge/Tech--blog-%23121011.svg?style=flat-square&logo=github&logoColor=white)](https://yunhobb.github.io)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=flat-square&logo=Instagram&logoColor=white)](https://www.instagram.com/nuyho_/)
<br>
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fyunhobb%2Fhit-counter&count_bg=%23378CA2&title_bg=%23555555&icon=gradle.svg&icon_color=%237DB4C6&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)


## :books: Latest Blog Post :books:
"""

resultREADME = f"{preREADME}{latest_posts}"

with open("README.md", "w", encoding='utf-8') as f :
  f.write(resultREADME)
