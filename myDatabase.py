import sqlite3

class AgendaDB:
    def __init__(self, file):
        self.conn = sqlite3.connect(file)
        self.cursor = self.conn.cursor()

    def insert(self, name, phone):
        command = 'INSERT OR IGNORE INTO agenda (name, phone) VALUES (?, ?)'
        self.cursor.execute(command, (name, phone))
        self.conn.commit()

    def edit(self, name, phone, id):
        command = 'UPDATE agenda SET name =?, phone=? WHERE id=?'
        self.cursor.connection(command, (name, phone, id))
        self.conn.commit()

    def exclude(self):
        command = 'DELETE FROM agenda WHERE id =?'
        self.cursor.execute(command(id,))
        self.conn.commit()

    def search(self, value):
        command = ('SELECT * FROM agenda WHERE nome LIKE ?')
        self.cursor.execute(command, (f'%{value}%'))

    def list(self):
        self.cursor.execute('SELECT * FROM agenda')

        for line in self.cursor.fetchall():
            print(line)

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    agenda = AgendaDB('db2.db')
    agenda.insert('Luiz', '111111')
    agenda.list()