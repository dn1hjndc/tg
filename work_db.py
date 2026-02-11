import sqlite3

def show_all():
    print("ВЫВОД ВСЕГО")
    connection = sqlite3.connect("quiz.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * from users")
    quiz = cursor.fetchall()

    connection.close()
    print(quiz)
    return quiz



if __name__ == '__main__':
    show_all()