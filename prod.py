from waitress import serve

import QuoteAPP

serve(QuoteAPP.app, host='0.0.0.0', port=8080)
