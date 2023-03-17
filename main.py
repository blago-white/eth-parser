import time
from parser import parser
from parser import price_logger
from bs4 import BeautifulSoup


def count_price_from_tag(text_page: str):
    bs4page = BeautifulSoup(text_page, "lxml")
    tag = bs4page.find_all('span', attrs={'class': 'latest-price din-pro rise'})

    if tag:
        return float(tag[0].text.replace(' ', '').replace('\n', ''))


def get_price(parser_instance: parser.BinanceParser):
    text_page = parser_instance.get_chart_page()
    return count_price_from_tag(text_page=text_page)


def main(url: str, recording_period: int):
    parser_instance = parser.BinanceParser(url=url)
    logger_instance = price_logger.PriceLogger()

    while True:
        logger_instance.add_log(log_value=get_price(parser_instance=parser_instance))

        if time.time() - logger_instance.get_log_time(0) >= recording_period:
            price_difference = abs(logger_instance.get_log_value(0) - logger_instance.get_log_value(-1))
            if price_difference >= logger_instance.get_log_value(0) / 100:
                print('Цена изменилась более чем на 1%')

            logger_instance.delete_latest_log()


if __name__ == '__main__':
    main('https://bingx.com/en-us/spot/ETHUSDT/', recording_period=3600)
