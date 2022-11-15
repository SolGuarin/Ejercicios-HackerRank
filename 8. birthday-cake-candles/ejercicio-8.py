def birthdayCakeCandles(candles):
    # Write your code here

    max_candle = candles[0]
    count_candles = 0

    for i in range(len(candles)):
        if candles[i] > max_candle:
            max_candle = candles[i]

    for i in range(len(candles)):
        if candles[i] == max_candle:
            count_candles += 1
    return count_candles


if __name__ == '__main__':
    candles = [3, 2, 1, 3]
    result = birthdayCakeCandles(candles)
    print(result)
