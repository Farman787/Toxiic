import requests
import logging
from time import sleep

API_VERSION = 'v15.0'

HEADERS = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

logo = """
\033[1;34;40m  ______   __    __   ______   __    __  _______         __       __  ________  __    __  _______    ______  
\033[1;34;40m /      \ /  \  /  | /      \ /  \  /  |/       \       /  \     /  |/        |/  |  /  |/       \  /      \ 
\033[1;34;40m/$$$$$$  |$$  \ $$ |/$$$$$$  |$$  \ $$ |$$$$$$$  |      $$  \   /$$ |$$$$$$$$/ $$ |  $$ |$$$$$$$  |/$$$$$$  |
\033[1;34;40m$$ |__$$ |$$$  \$$ |$$ |__$$ |$$$  \$$ |$$ |  $$ |      $$$  \ /$$$ |$$ |__    $$ |__$$ |$$ |__$$ |$$ |__$$ |
\033[1;34;40m$$    $$ |$$$$  $$ |$$    $$ |$$$$  $$ |$$ |  $$ |      $$$$  /$$$$ |$$    |   $$    $$ |$$    $$< $$    $$ |
\033[1;34;40m$$$$$$$$ |$$ $$ $$ |$$$$$$$$ |$$ $$ $$ |$$ |  $$ |      $$ $$ $$/$$ |$$$$$/    $$$$$$$$ |$$$$$$$  |$$$$$$$$ |
\033[1;34;40m$$ |  $$ |$$ |$$$$ |$$ |  $$ |$$ |$$$$ |$$ |__$$ |      $$ |$$$/ $$ |$$ |_____ $$ |  $$ |$$ |  $$ |$$ |  $$ |
\033[1;34;40m$$ |  $$ |$$ | $$$ |$$ |  $$ |$$ | $$$ |$$    $$/       $$ | $/  $$ |$$       |$$ |  $$ |$$ |  $$ |$$ |  $$ |
\033[1;34;40m$$/   $$/ $$/   $$/ $$/   $$/ $$/   $$/ $$$$$$$/        $$/      $$/ $$$$$$$$/ $$/   $$/ $$/   $$/ $$/   $$/
"""

made_by_text = "\033[1;35;40mMADE BY AN9ND M3HR9\033[0m"
msg_bh3g_text = "\033[1;31;40mMSG BH3G D1Y9 AN9ND S1R\033[0m"
phantom_red_text = "\033[1;31mPHANTOM RED\033[0m"

def send_message(api_url, access_token, thread_id, message):
    parameters = {'access_token': access_token, 'message': message}
    try:
        response = requests.post(api_url, data=parameters, headers=HEADERS)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response
    except requests.exceptions.RequestException as e:
        logging.error(f"Error sending message: {e}")
        return None

def main():
    logging.basicConfig(level=logging.INFO)

    try:
        num_tokens = int(input("\033[1;33mEnter the number of access tokens: \033[0m"))
        access_tokens = [input(f"\033[1;33mEnter access token {i + 1}: \033[0m") for i in range(num_tokens)]

        num_threads = int(input("\033[1;33mEnter the number of thread IDs: \033[0m"))
        thread_ids = [input(f"\033[1;33mEnter thread ID {i + 1}: \033[0m") for i in range(num_threads)]

        mn = input("\033[1;33mEnter your haters name: \033[0m")
        time_interval = int(input("\033[1;33mEnter the time interval between messages (in seconds): \033[0m"))

        txt_file_path = input("\033[1;33mEnter the path to your message file (txt): \033[0m")

        with open(txt_file_path, 'r') as file:
            messages = file.read().splitlines()

        print(logo)
        print(made_by_text)
        print(msg_bh3g_text)
        print(phantom_red_text)

        while True:
            for access_token in access_tokens:
                for thread_id in thread_ids:
                    for message1 in messages:
                        api_url = f'https://graph.facebook.com/{API_VERSION}/t_{thread_id}/'
                        message = f'{mn} {message1}'
                        response = send_message(api_url, access_token, thread_id, message)

                        if response and response.status_code == 200:
                            logging.info(f"Message sent using token {access_token} to thread {thread_id}: {message}")
                        else:
                            logging.error(f"Failed to send message using token {access_token} to thread {thread_id}: {message}")

                        sleep(time_interval)

    except KeyboardInterrupt:
        logging.info("\nScript terminated by user.")

if __name__ == "__main__":
    main()
