

def main():
    USD_VS_RMB = 6.77

    #
    currency_str_value =    input('请输入带单位的货币金额：')

    unit = currency_str_value[-3:]

    if unit == 'CNY':
        exchange_rate = 1 / USD_VS_RMB
    elif unit == 'USD':
        exchange_rate = USD_VS_RMB
    else:
        exchange_rate = -1

    if exchange_rate != -1:
        in_money = eval(currency_str_value[:-3])
        # 使用lambda定义函数
        convert_currency2 = lambda x: x * exchange_rate

        # # 调用函数
        # out_money = convert_currency(in_money, exchange_rate)

        # 调用lambda函数
        out_money = convert_currency2(in_money)
        print('转换后的金额：', out_money)
    else:
        print('不支持该种货币！')


if __name__ == '__main__':
    main()