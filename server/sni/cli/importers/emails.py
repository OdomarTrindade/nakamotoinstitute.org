from sni.cli.utils import JSONImporter
from sni.satoshi.emails.models import Email, EmailFile, EmailThread, EmailThreadFile
from sni.satoshi.emails.schemas import EmailJSONModel, EmailThreadJSONModel


class EmailThreadImporter(JSONImporter):
    filepath = "data/email_threads.json"
    item_schema = EmailThreadJSONModel
    model = EmailThread
    file_model = EmailThreadFile
    content_type = "email_threads"


def import_email_thread():
    importer = EmailThreadImporter()
    importer.run_import()


class EmailImporter(JSONImporter):
    filepath = "data/emails.json"
    item_schema = EmailJSONModel
    model = Email
    file_model = EmailFile
    content_type = "emails"


def import_email():
    importer = EmailImporter()
    importer.run_import()
