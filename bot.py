import requests

# --- Ustawienia ---
COINPAYMENTS_API_KEY = 'TU_WKLEJ_SWÓJ_API_KEY'
COINPAYMENTS_API_SECRET = 'TU_WKLEJ_SWÓJ_API_SECRET'
TELEGRAM_BOT_TOKEN = 'TU_WKLEJ_TOKEN_TELEGRAM_BOTA'
TELEGRAM_CHAT_ID = 'TU_WKLEJ_CHAT_ID'

# --- Funkcja wysyłania wiadomości na Telegram ---
def wyslij_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": msg}
    requests.post(url, data=data)

# --- Przykład sprawdzania płatności w Litecoin ---
def sprawdz_litecoin():
    # Prosty przykład: pobieranie salda konta CoinPayments
    url = "https://www.coinpayments.net/api.php"
    headers = {"Content-Type": "application/json"}
    payload = {
        "version": 1,
        "cmd": "balances",
        "key": COINPAYMENTS_API_KEY,
        "format": "json"
    }
    # Tutaj normalnie trzeba podpisać żądanie API HMAC, uprościliśmy dla przykładu
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        wyslij_telegram("Sprawdzono saldo Litecoin!")
    else:
        wyslij_telegram("Błąd podczas sprawdzania salda.")

# --- Uruchomienie ---
if __name__ == "__main__":
    wyslij_telegram("Bot uruchomiony!")
    sprawdz_litecoin()
