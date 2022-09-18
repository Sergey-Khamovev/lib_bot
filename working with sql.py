import sqlite3


def db_create_tables_authors():
    with sqlite3.connect("Books.db") as db:
        cursor = db.cursor()
        data = [('Agatha Cristy', 'New York'), ('Sergey Lukjanenko', 'Tver'), ('Nik Perumov', 'Rostov'),
                ('Oskar Wild', 'New York')]
        cursor.executemany("INSERT INTO authors(name,tag) VALUES(?,?)", data)
        db.commit()


def db_create_table_books():
    with sqlite3.connect("Books.db") as db:
        cursor = db.cursor()

        data = [('1', 'Magician', 'Nik Perumov', '2005'), ('2', 'The bomb', 'Agatha Cristy', '2010'),
                ('3', 'The cold iron', 'Sergey Lukjanenko', '2005'), ('4', 'Fess', 'Nik Perumov', '2005'),
                ('5', 'The sword', 'Nik Perumov', '2011'), ('6', 'The whore', 'Agatha Cristy', '2010'),
                ('7', 'The dog', 'Agatha Cristy', '2011'), ('8', 'The king', 'Sergey Lukjanenko', '2016'),
                ('9', 'The bitch', 'Sergey Lukjanenko', '2005'), ('10', 'The coconut', 'Oskar Wild', '2016')]

        cursor.executemany("INSERT INTO books(id,title,author,published) VALUES(?,?,?,?);", data)
        db.commit()


def db_show_table_authors():
    with sqlite3.connect("Books.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM authors")
        result = cursor.fetchall()
        print("Таблица 'Авторы'")
        for i in range(0, len(result)):
            print("№", i + 1, "Автор:", result[i][0], "Место рождения:", result[i][1])


def db_show_table_books():
    with sqlite3.connect("Books.db") as db:
        cursor = db.cursor()

        cursor.execute("SELECT * FROM books")
        print("Таблица 'Книги'")
        result = cursor.fetchall()
        for i in range(0, len(result)):
            print("№", i + 1, "ID:", result[i][0], ". Название книги:", result[i][1], "Автор:", result[i][2],
                  "Год издания:", result[i][3])


def db_search_by_birthplace():
    with sqlite3.connect("Books.db") as db:
        cursor = db.cursor()

        birthplace = input("Введите место рождения:")
        cursor.execute("""SELECT books.title,books.author,books.published FROM books,authors WHERE books.author=authors.name
         AND authors.place_of_birth=?""", [birthplace])
        result = cursor.fetchall()
        for i in range(0, len(result)):
            print("Наименование книги: ", result[i][0], " Автор книги: ", result[i][1], " Год издания: ", result[i][2])


def db_search_published():
    with sqlite3.connect("Books.db") as db:
        cursor = db.cursor()

        published = int(input("Введите год издания: "))
        cursor.execute("SELECT title FROM books WHERE published>=? ORDER BY published", [published])
        result = cursor.fetchall()
        for i in range(0, len(result)):
            print("Наименование книги: ", result[i][0])


def db_delete_book():
    with sqlite3.connect("Books.db") as db:
        cursor = db.cursor()
        bookid = int(input("Введите идентификатор книги в таблице:"))
        cursor.execute("DELETE FROM books WHERE id=?", [bookid])
        print("Книга успешно удалена")
        db.commit()


def db_add_book():
    with sqlite3.connect("Books.db") as db:
        cursor = db.cursor()

        id = int(input("Введите идентификатор книги:"))
        title = input("Введите название книги:")
        author = input("Введите имя автора:")
        published = int(input("Введите год публикации:"))
        cursor.execute("SELECT name FROM authors")
        names = cursor.fetchall()
        flag = False
        for i in range(0, len(names)):
            if author in names[i][0]:
                flag = True
        if flag:
            try:
                cursor.execute("INSERT INTO books(id,title,author,published) VALUES(?,?,?,?)",
                               (id, title, author, published))
                print("Книга успешно добавлена")
                db.commit()
            except:
                print("Ошибка добавления. Возможно такой идентификатор уже есть")
        else:
            print("Автор не найден. Добавьте автора в таблицу авторов")


def db_add_author():
    with sqlite3.connect("Books.db") as db:
        cursor = db.cursor()

    #    cursor.executemany("INSERT INTO authors(name,place_of_birth) VALUES(?,?)", data)
        name = input("Введите имя автора: ")
        place_of_birth = input("Введите место рождения автора: ")
        names = cursor.fetchall()
        flag = False
        for i in range(0, len(names)):
            if name in names[i][0]:
                flag = True
        if not flag:
            cursor.execute("INSERT INTO authors(name,place_of_birth) VALUES(?,?)", (name, place_of_birth))
            print("Автор успешно добавлен")
            db.commit()
        else:
            print("Такой автор уже в системе!")


def show_menu():
    print("")
    print("1 - показать все таблицы базы данных")
    print("2 - создать базу данных")
    print("3 - удалить книгу по идентификатору")
    print("4 - добавить книгу")
    print("5 - добавить автора")
    print("6 - поиск книг по месту рождения автора")
    print("7 - поиск книг по дате публикации")
    print("8 - Выход")


def create_db():
    with sqlite3.connect("Books.db") as db:
        cursor = db.cursor()
        # создаем таблицу books, для заполнения будем вызывать метод db_create_table_books()
        cursor.execute("""CREATE TABLE IF NOT EXISTS books(id integer PRIMARY KEY,title text NOT NULL, author text NOT NULL,
                        published integer NOT NULL, tag text);""")
        # создаем таблицу authors для заполнения будем вызывать метод db_create_tables_authors()
        cursor.execute("CREATE TABLE IF NOT EXISTS authors(name text PRIMARY KEY, tag text);")


def main():
    cycle = True
    while cycle:
        show_menu()
        choice = input("Ваш выбор: ")
        if choice == "1":
            db_show_table_authors()
            db_show_table_books()
        elif choice == "2":
            create_db()
        elif choice == "3":
            db_delete_book()
        elif choice == "4":
            db_add_book()
        elif choice == "5":
            db_add_author()
        elif choice == "6":
            db_search_by_birthplace()
        elif choice == "7":
            db_search_published()
        elif choice == "8":
            cycle = False


main()

