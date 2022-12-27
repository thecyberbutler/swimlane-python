"""Contains various adapters encapsulating API logic for retrieving, searching, listing, or creating resource objects"""

from .app import AppAdapter
from .record import RecordAdapter
from .report import ReportAdapter
from .usergroup import UserAdapter, GroupAdapter
from .helper import HelperAdapter
from .app_revision import AppRevisionAdapter
from .record_revision import RecordRevisionAdapter
from .task import TaskAdapter
