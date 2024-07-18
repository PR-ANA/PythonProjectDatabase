import sqlite3
con = sqlite3.connect("WebScraping.db")
cur = con.cursor()
query = """
create table Books
(SN int, Book_name varchar(50), Price varchar(50))
"""
try:
    cur.execute(query)
except Exception as e:
    print(e)

query = """
insert into Books
values
(1, 'A light in the Attic', '£51.77'),
(2, 'Tipping the Velvet', '£53.74'),
(3, 'Soumission', '£50.10'),
(4, 'Sharp Ojects', '£47.82'),
(5, 'Sapiens: A Brief History of Humankind', '£54.23'),
(6, 'The Requiem Red', '£22.65'),
(7, 'The Dirty Little Secrets of Getting Your Dream Job', '£33.34'),
(8, 'The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull', '£17.93'),
(9, 'The boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympic', '£22.60'),
(10, 'The Black Maria', '£52.15'),
(11, 'Starving Hearts (Triangular Trade Trilogy, #1)', '£13.99'),
(12, 'Shakespeare''s Sonnets', '£20.66'),
(13, 'Set Me Free', '£17.46'),
(14, 'Scott Pilgrim''s Precious Little Life (Scott Pilgrim #1)', '£52.29'),
(15, 'Rip it Up and Start Again', '£35.02'),
(16, 'Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991', '£57.25'),
(17, 'Olio', '£23.88'),
(18, 'Mesaerion: The Best Science  Fiction Stories 1800-1849', '£37.59'),
(19, 'Libertarianism for Beginners', '£51.33'),
(20, 'It''s Only the Himalayas', '£45.17')
"""
cur.execute(query)
cur.execute("select SN, book_name, price from Books")
cur.execute("select SN, book_name, price from Books").fetchall()
cur.execute("select * from Books where price > '£50'").fetchall()
print(query)
