"""Show function -> list every property in the table."""
import db
import state
from helpers import clear_form


def Show():
    conn = db.get_connection()
    cursor = conn.cursor()

    # wipe whatever is currently displayed
    for child in state.listdisplay.get_children():
        state.listdisplay.delete(child)

    cursor.execute(
        'SELECT Property_id, Name, Description, Address, Size, Country, State, Price, '
        'Status FROM estate_info ORDER BY Date_listed DESC'
    )
    for record in cursor.fetchall():
        state.listdisplay.insert("", "end", values=record)

    conn.close()
    clear_form()
