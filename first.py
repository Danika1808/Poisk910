import csv
import webbrowser
import requests
import time
import datetime


def take_2000_posts(token, domain):
    token = token
    version = 5.131
    domain = domain
    count = 100
    offset = 0
    file = open(f'{domain}.csv', 'w+', encoding="utf-8")
    all_posts = csv.writer(file)
    all_posts.writerow(['date', 'text'])

    while offset < 2000:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count': count,
                                    'offset': offset
                                }
                                )
        try:
            data = response.json()['response']['items']

            for item in data:
                if item['text'] != '':
                    formatted_date = datetime.datetime.fromtimestamp(item['date']).strftime('%Y-%m-%d')
                    all_posts.writerow([formatted_date, item['text']])
                    offset += 1

        except Exception as exception:
            print('Something Went Wrong (Check Domain or API Key)')
            raise Exception(exception)

        time.sleep(0.5)

    file.close()


if __name__ == '__main__':
    try:
        DOMAIN = 'bugurt_thread'
        TOKEN = "vk1.a.zFF1CnfuVqroCI8vtdIevugglrTMpA39ec2HIgrSqio9iWGFhuS6MTSj6wcbbZkJOVSaeWbOsaNPZx46xPqJmzUDzbmyRUQW_ItTwyRNy_sxsA97x7RMu4PmZczIsyDWQoIv8d3PATd3hheiIkDWPPavS936xwSeanb4IzneBLfe2rY-R-qnvCXeLRCaOvX4"
        take_2000_posts(TOKEN, DOMAIN)

    except Exception as e:
        print(f'Got an exception: {e}')
