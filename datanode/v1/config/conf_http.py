
HTTP = "http"
HTTPS = "https"

HTTP_LISTENON = "0.0.0.0"

SERVER_NAME = "LEDGABLE/INDIGO"
SERVICE_VERSION = "1.001"
TIMEOUT = 3600
PACKET_SIZE = 2048

NO_TRACK = "NOTRACK"
NO_TRACK_IP = "0.0.0.0"
IP_LOCALHOST = "127.0.0.1"
NO_SESSION = "No Session"

RESPONSE_OK = "Ok"
RESPONSE_ACCESS_DENIED = "Access Denied"
RESPONSE_NO_PERMISSIONS = "No Permissions"
RESPONSE_NOT_LOGGED_IN = "Not logged In"
RESPONSE_MISSING_INFO = "Missing Information"
RESPONSE_PARAMETERS_INVALID = "Parameters Invalid"

TYPE_RAW = "raw"
TYPE_JSON = "json"
TYPE_XML = "xml"
TYPE_XMLS = "xmls"
TYPE_HTML = "html"
TYPE_CSV = "csv"
TYPE_CSS = "css"
TYPE_JS = "js"

TEXT_TYPES = [TYPE_HTML, TYPE_RAW, TYPE_JSON, TYPE_XML, TYPE_XMLS]

AJAX_TOKEN = "XMLHttpRequest"

HTTP_ACTIONS = {"get":"get", "head":"get", "put":"put", "post":"post", "delete":"delete", "gateway":"gateway"}

AUTOBLOCK_USERAGENTS = ["masscan"]
ALLOWED_USERAGENTS = ["chrome", "safari", "firefox", "microsoft", "msie", "opera", "gecko", "bot", "mozilla"]

COOKYMAP = {"session_id":"session_id", "device_id":"device_id", "language":"language"}

HTTP_OK = 200
HTTP_CREATED = 201
HTTP_ACCEPTED = 202
HTTP_NON_AUTH_ANSWER = 203
HTTP_NO_CONTENT = 204
HTTP_RESET_CONTENT = 205
HTTP_PARTIAL_CONTENT = 206

HTTP_REDIRECT = 301
HTTP_NOT_MODIFIED = 304

HTTP_BAD_REQUEST = 400
HTTP_SESSION_FAILURE = 401
HTTP_FORBIDDEN = 403
HTTP_PAGE_DOES_NOT_EXIST = 404
HTTP_METHOD_NOT_ALLOWED = 405
HTTP_NOT_ACCEPTABLE = 406

HTTP_ACTION_PUT = "put"
HTTP_ACTION_GET = "get"
HTTP_ACTION_POST = "post"
HTTP_ACTION_DELETE = "delete"
HTTP_ACTION_GATEWAY = "gateway"

HTML_NBSP = "&nbsp;"
