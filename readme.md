Hi,

This is my master (preperation year) Database Management homework project.
* My aim was in this project to analyze the requirements of book stores (chain) database desing, and create ER diagram.
* After this I have designed a website that can be used by the employees of this book chain so that they can do all the operations/ transactions.
* My aim was to make this project end to end, (yea still there is some little things to do)
* I made this project in about a week. (After working days and weekend)

---

There is some critical points for me:
* Employees should be able to record sales transactions.
* Customer informations must be recorded.
* Book informations must be recorded.
* And every informations should be recorded by branches.

I specified required tables and entities firstly on draw them on paper. And after this i design it on database.
I used SQL Server as database. And ER diagram of the tables is like this.

![](https://user-images.githubusercontent.com/70684994/124384823-b48cb180-dcdb-11eb-9f6e-7b07a3da5dae.png)

After this step, I added some constraints in order not to fall into logical errors.
This ones are like:
* Phone numbers should be contains exactly 10 characters (digits) like 5553332211.
* Books names and autoer names could be same, because different publishers could publishe them. But trinity of bookname-publisher-author could not be same. This mean we are about to save duplicated book. (Yea actually publishers could publish different editions of same book but I ignored this possibility)
* Price must be positive.
and more.
You can see the constraints:
![](https://user-images.githubusercontent.com/70684994/124385174-5d87dc00-dcdd-11eb-8f27-abe4c788601d.png)
---

After design the database I needed data that I could fill in the tables. Hardest one was book names and author names, I took them with web scraping. And later I found most populer turkish names and surnames on the internet and shuffle them, and later match them to use them my customers. And later I found cities and towns. I randomly designed the book titles, found them on my own mind. You can find them all in [writeIT.ipynb](https://github.com/bilative/bookStoreProjectDB/blob/main/writeIT.ipynb) file.
for example phoneNumbers are:
```python
randomNo=[str(random.randint(1000000,9999999)) for i in range(len(customers))]
opNo=[str(i) for i in np.arange(532,548)]
opNo_=[random.choice(opNo) for i in range(len(customers))]
phoeNos=[i+j for i,j in zip(opNo_, randomNo)]
```
---

After fill the tables I designed the web application. I used python for rest of all. I used only plotly dash for interface and back. Plotly dash is a flask based library. I'm using it mostly my data science projects to create stream, interactive data visualization outputs. It is so powerfull I thin, you can check [plotly dash](https://dash.plotly.com/introduction).

Sales Transaction Page:

![](https://user-images.githubusercontent.com/70684994/124386793-b444e400-dce4-11eb-8d72-f8b4c4ad3328.png)

Book Page:
![](https://user-images.githubusercontent.com/70684994/124386822-dd657480-dce4-11eb-92de-5a1d90259cd5.png)

Customer Page:
![](https://user-images.githubusercontent.com/70684994/124387092-e0149980-dce5-11eb-8c20-1008ef8b2074.png)

PAge for Other Tables:
![](https://user-images.githubusercontent.com/70684994/124387128-f9b5e100-dce5-11eb-84cb-f21e25399976.png)

Basic DashBoard:
![](https://user-images.githubusercontent.com/70684994/124387162-19e5a000-dce6-11eb-9ae0-509059c8159d.png)


You should set the connection infos by your own info, [here](https://github.com/bilative/bookStoreProjectDB/blob/main/libs/connection_.py).

