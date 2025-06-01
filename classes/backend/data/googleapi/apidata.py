# Api Class
class ApiData:
    """
    Manages basic data information about a Google Api.

    :param database: Database name as in the st.secrets toml file.
    :param spreadsheet: Spreadsheet name as in the st.secrets toml file.
    :return: Google Api Data object.
    """

    # Constructor
    def __init__(self, database: str, spreadsheet: str):
        self.database = database
        self.spreadsheet = spreadsheet
