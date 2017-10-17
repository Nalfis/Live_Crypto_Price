import datetime
cuenta = [x for x in range(1, 10)]

cuenta2 = [i*2 for i in cuenta]

LTC = [
    {
        "created_at": "2017-10-14T15:59:59.575Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "c486e0a0-2b2c-4172-a47b-12a667e664ad",
        "price": "65.50000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "5.00000000",
        "trade_id": 7541193,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-10-14T15:56:05.348Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "f210ed5b-2e14-4f65-aadb-750ddd1489f6",
        "price": "66.25000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "5.00000000",
        "trade_id": 7540010,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-10-14T02:35:37.356Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "bc30eb8f-b338-47b0-8339-3571177118f4",
        "price": "59.30000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "sell",
        "size": "27.48957868",
        "trade_id": 7505590,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-10-13T02:53:25.574Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "ca311ea0-cb81-43f6-a791-8847e37ac95e",
        "price": "58.38000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "27.48957868",
        "trade_id": 7438656,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-10-13T01:46:29.695Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "09b05863-c747-4111-98c6-1526c0490e28",
        "price": "59.30000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "sell",
        "size": "5.00000000",
        "trade_id": 7430471,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-10-13T00:57:57.302Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "484823ec-38d7-4b2f-a0a0-20c0861f7cee",
        "price": "58.50000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "5.00000000",
        "trade_id": 7426875,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-10-12T16:15:13.709Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "1d81e9ea-1ab6-4a40-8979-d21adb91b18a",
        "price": "56.00000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "sell",
        "size": "9.99418175",
        "trade_id": 7376378,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-10-12T16:08:32.625Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "79adadc4-c454-43de-afd2-f2ef6585d05a",
        "price": "55.00000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "sell",
        "size": "3.61450230",
        "trade_id": 7375152,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-10-12T16:08:32.513Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "79adadc4-c454-43de-afd2-f2ef6585d05a",
        "price": "55.00000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "sell",
        "size": "15.30549770",
        "trade_id": 7375151,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-10-02T21:51:37.979Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "5ac06182-9226-41f5-8460-1c6aa83e3792",
        "price": "53.07000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "18.91418175",
        "trade_id": 7032435,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-30T20:56:30.411Z",
        "fee": "0.0873232440000000",
        "liquidity": "T",
        "order_id": "c5dfe079-9913-4dde-91cd-dd3abed29f1e",
        "price": "55.52000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "0.52427500",
        "trade_id": 6954736,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-30T20:56:30.411Z",
        "fee": "0.0164951030400000",
        "liquidity": "T",
        "order_id": "c5dfe079-9913-4dde-91cd-dd3abed29f1e",
        "price": "55.52000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "0.09903400",
        "trade_id": 6954735,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-30T20:56:30.411Z",
        "fee": "0.6627894000000000",
        "liquidity": "T",
        "order_id": "c5dfe079-9913-4dde-91cd-dd3abed29f1e",
        "price": "55.51000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "3.98000000",
        "trade_id": 6954734,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-30T20:56:30.411Z",
        "fee": "0.0026478270000000",
        "liquidity": "T",
        "order_id": "c5dfe079-9913-4dde-91cd-dd3abed29f1e",
        "price": "55.51000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "0.01590000",
        "trade_id": 6954733,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-30T20:56:30.411Z",
        "fee": "0.0499590000000000",
        "liquidity": "T",
        "order_id": "c5dfe079-9913-4dde-91cd-dd3abed29f1e",
        "price": "55.51000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "0.30000000",
        "trade_id": 6954732,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-30T20:56:30.411Z",
        "fee": "0.0134541252300000",
        "liquidity": "T",
        "order_id": "c5dfe079-9913-4dde-91cd-dd3abed29f1e",
        "price": "55.51000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "0.08079100",
        "trade_id": 6954731,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-30T19:44:03.289Z",
        "fee": "0.0407954936700000",
        "liquidity": "T",
        "order_id": "7432eb59-43b4-430a-af33-6ae241453d3e",
        "price": "55.50000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "0.24501798",
        "trade_id": 6951908,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-30T19:44:03.289Z",
        "fee": "0.4727748000000000",
        "liquidity": "T",
        "order_id": "7432eb59-43b4-430a-af33-6ae241453d3e",
        "price": "55.49000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "2.84000000",
        "trade_id": 6951907,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-30T19:44:03.289Z",
        "fee": "0.3187870568694000",
        "liquidity": "T",
        "order_id": "7432eb59-43b4-430a-af33-6ae241453d3e",
        "price": "55.49000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "1.91498202",
        "trade_id": 6951906,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-27T18:15:00.893Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "0fbe5e7c-92f9-48af-84ee-6729c496d03b",
        "price": "54.80000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "sell",
        "size": "28.45082848",
        "trade_id": 6801086,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-26T12:27:55.234Z",
        "fee": "0.2065508082570000",
        "liquidity": "T",
        "order_id": "7cd55f0e-e056-4311-bfec-d97e21f1e041",
        "price": "53.86000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "1.27831915",
        "trade_id": 6756625,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-26T12:27:55.234Z",
        "fee": "0.0035031917430000",
        "liquidity": "T",
        "order_id": "7cd55f0e-e056-4311-bfec-d97e21f1e041",
        "price": "53.86000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "0.02168085",
        "trade_id": 6756624,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-26T12:26:48.279Z",
        "fee": "1.9626585881940000",
        "liquidity": "T",
        "order_id": "1bd43fbb-4d0b-421a-ba22-c4ee5c70910c",
        "price": "53.85000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "12.14892348",
        "trade_id": 6756608,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-26T12:26:48.279Z",
        "fee": "0.0164596956000000",
        "liquidity": "T",
        "order_id": "1bd43fbb-4d0b-421a-ba22-c4ee5c70910c",
        "price": "53.84000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "0.10190500",
        "trade_id": 6756607,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-25T14:50:16.108Z",
        "fee": "2.1877800000000000",
        "liquidity": "T",
        "order_id": "8c3099e1-dd7b-4bd2-982f-c804a5750073",
        "price": "52.09000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "sell",
        "size": "14.00000000",
        "trade_id": 6719074,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-21T00:55:35.182Z",
        "fee": "2.2447500000000000",
        "liquidity": "T",
        "order_id": "9976a2f6-0e63-4daf-8eef-33424afca9f0",
        "price": "51.25000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "14.60000000",
        "trade_id": 6526915,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-20T01:24:41.571Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "6fe062c4-95ef-4bb4-8810-cecded7461c1",
        "price": "53.10000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "sell",
        "size": "14.20000000",
        "trade_id": 6488208,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-19T19:29:40.813Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "0c0b46b9-e1cb-4194-99b4-e7c16112b39e",
        "price": "52.70000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "0.36806409",
        "trade_id": 6477773,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-19T19:29:33.935Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "0c0b46b9-e1cb-4194-99b4-e7c16112b39e",
        "price": "52.70000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "8.56090600",
        "trade_id": 6477766,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-19T19:29:27.511Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "0c0b46b9-e1cb-4194-99b4-e7c16112b39e",
        "price": "52.70000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "1.34454700",
        "trade_id": 6477765,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-19T19:29:24.891Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "0c0b46b9-e1cb-4194-99b4-e7c16112b39e",
        "price": "52.70000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "3.92648291",
        "trade_id": 6477764,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-19T11:58:30.923Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "0af5f927-6b45-423e-a87c-5aaeb30fe2fc",
        "price": "55.50000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "sell",
        "size": "13.38000000",
        "trade_id": 6466094,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-16T11:22:25.251Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "5f57f3dd-9cfa-4c91-9b9a-47c341bc41b8",
        "price": "54.25000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "10.89430158",
        "trade_id": 6309466,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-16T11:22:24.799Z",
        "fee": "0.0016786512000000",
        "liquidity": "T",
        "order_id": "5f57f3dd-9cfa-4c91-9b9a-47c341bc41b8",
        "price": "54.22000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "0.01032000",
        "trade_id": 6309465,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-16T11:22:24.799Z",
        "fee": "0.0016786512000000",
        "liquidity": "T",
        "order_id": "5f57f3dd-9cfa-4c91-9b9a-47c341bc41b8",
        "price": "54.22000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "0.01032000",
        "trade_id": 6309464,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-16T11:22:24.799Z",
        "fee": "0.0016786512000000",
        "liquidity": "T",
        "order_id": "5f57f3dd-9cfa-4c91-9b9a-47c341bc41b8",
        "price": "54.22000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "0.01032000",
        "trade_id": 6309463,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-16T11:22:24.799Z",
        "fee": "0.0016786512000000",
        "liquidity": "T",
        "order_id": "5f57f3dd-9cfa-4c91-9b9a-47c341bc41b8",
        "price": "54.22000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "0.01032000",
        "trade_id": 6309462,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-16T11:22:24.799Z",
        "fee": "0.0016786512000000",
        "liquidity": "T",
        "order_id": "5f57f3dd-9cfa-4c91-9b9a-47c341bc41b8",
        "price": "54.22000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "0.01032000",
        "trade_id": 6309461,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-16T11:22:24.799Z",
        "fee": "0.0016770246000000",
        "liquidity": "T",
        "order_id": "5f57f3dd-9cfa-4c91-9b9a-47c341bc41b8",
        "price": "54.22000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "0.01031000",
        "trade_id": 6309460,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-16T11:22:24.799Z",
        "fee": "0.0016770246000000",
        "liquidity": "T",
        "order_id": "5f57f3dd-9cfa-4c91-9b9a-47c341bc41b8",
        "price": "54.22000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "0.01031000",
        "trade_id": 6309459,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-16T11:22:24.799Z",
        "fee": "0.0016767153000000",
        "liquidity": "T",
        "order_id": "5f57f3dd-9cfa-4c91-9b9a-47c341bc41b8",
        "price": "54.21000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "0.01031000",
        "trade_id": 6309458,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-16T11:22:24.799Z",
        "fee": "2.7129286147764000",
        "liquidity": "T",
        "order_id": "5f57f3dd-9cfa-4c91-9b9a-47c341bc41b8",
        "price": "54.14000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "16.70316842",
        "trade_id": 6309457,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-16T01:38:55.693Z",
        "fee": "3.0406176659268000",
        "liquidity": "T",
        "order_id": "c2bab942-dee5-4cbf-97d7-1521b14b2a3f",
        "price": "53.08000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "sell",
        "size": "19.09455957",
        "trade_id": 6274697,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-15T14:21:53.827Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "9d4c2336-4620-4e52-9140-2dee5df44ee7",
        "price": "53.00000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "1.00497682",
        "trade_id": 6199402,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-15T14:09:21.594Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "86a0e2d0-8bc4-4f17-b5c2-f17db30dc057",
        "price": "56.00000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "18.08958275",
        "trade_id": 6196000,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-15T14:03:18.474Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "74559e7f-a14c-4aad-938d-f414a14e411d",
        "price": "55.50000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "sell",
        "size": "19.23033958",
        "trade_id": 6192946,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-15T13:56:38.626Z",
        "fee": "3.1666600186386000",
        "liquidity": "T",
        "order_id": "fb47f00c-fad7-42f1-8680-f05a4eb785df",
        "price": "54.89000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "19.23033958",
        "trade_id": 6191144,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-15T13:52:59.522Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "2d6c2bc9-20ed-4a4c-b411-0631b3c54871",
        "price": "50.00000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "sell",
        "size": "21.10000000",
        "trade_id": 6189932,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-14T11:38:37.575Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "ed672e62-71eb-4f58-a2ed-15b0f7139c02",
        "price": "55.50000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "21.10000000",
        "trade_id": 6061796,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-13T17:18:27.308Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "f562234f-8f0b-442d-b1b5-839b5828d8d7",
        "price": "61.95000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "sell",
        "size": "18.93647237",
        "trade_id": 6026896,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-12T13:01:38.881Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "d6913474-4f3b-46f3-828f-df9329670a10",
        "price": "70.30000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "5.50000000",
        "trade_id": 5940164,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-12T06:10:17.266Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "ffec95a1-b920-4efb-ad3a-a521cea7de71",
        "price": "70.60000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "sell",
        "size": "5.50005116",
        "trade_id": 5926664,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-10T12:31:32.46Z",
        "fee": "0.0040977056547000",
        "liquidity": "T",
        "order_id": "dd3dc907-9d16-4c2a-8538-14d9a564f674",
        "price": "66.39000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "0.02057391",
        "trade_id": 5845009,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-09T13:35:05.471Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "a0b8224d-2a77-4798-8288-7d126a758d98",
        "price": "70.65000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "4.98000000",
        "trade_id": 5792008,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-08T19:53:18.127Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "52801dc4-166d-4aee-a128-d1d80fc0a5c2",
        "price": "71.00000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "sell",
        "size": "4.95900000",
        "trade_id": 5746875,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-08T14:13:46.369Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "b947390f-ba7a-4e65-b64c-5cbb773ba400",
        "price": "73.00000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "4.50000000",
        "trade_id": 5720093,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-08T14:12:28.122Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "c241483a-eca6-4599-af05-80a14c06416a",
        "price": "73.50000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "buy",
        "size": "0.45900000",
        "trade_id": 5719840,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-06T17:44:37.044Z",
        "fee": "0.1220400000000000",
        "liquidity": "T",
        "order_id": "3ce33378-07d5-41d3-85c4-012fcd159d77",
        "price": "81.36000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "sell",
        "size": "0.50000000",
        "trade_id": 5628341,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-06T17:43:40.597Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "506249fd-244d-42f2-a39b-1389074d7727",
        "price": "81.20000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "sell",
        "size": "1.23577176",
        "trade_id": 5628243,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-06T17:43:39.706Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "506249fd-244d-42f2-a39b-1389074d7727",
        "price": "81.20000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "sell",
        "size": "0.76422824",
        "trade_id": 5628242,
        "user_id": "59ab04c5133ed700e4c1ce28"
    },
    {
        "created_at": "2017-09-06T11:56:47.371Z",
        "fee": "0.0000000000000000",
        "liquidity": "M",
        "order_id": "89f6c8fc-3bdd-44fb-a8d3-77111bd29278",
        "price": "80.20000000",
        "product_id": "LTC-USD",
        "profile_id": "e5f6bc57-9cb4-4d53-907a-a38ca990ab3e",
        "settled": True,
        "side": "sell",
        "size": "2.00000000",
        "trade_id": 5608489,
        "user_id": "59ab04c5133ed700e4c1ce28"
    }
]

# print cuenta
# print cuenta2
# cuenta3 = []
# for a, b in zip(cuenta, cuenta2):
#     cuenta3.append(a+b)
#
# print cuenta3
#
# cuenta4=[]
# for i in range(len(cuenta)):
#      cuenta4.append(cuenta[i] + cuenta2[i])
#
#
# print cuenta4

suma = 0
# for k in LTC:
#     print k['price']
#     suma += float(k['price'])

today = datetime.datetime.now()
calc_date = '2017-10-14'
buy_sum_size = 0
sell_sum_size = 0
buy_fee = 0
sell_fee = 0
buy_sum_price = 0
sell_sum_price = 0
buy_avg_price = 0
sell_avg_price = 0

for k in LTC:
    if k['product_id'] == "LTC-USD" and k['created_at'][:10] == calc_date and k['side'] == 'buy':
        print "side: {} - size: {} * price ${:3.5f} fee: ${:3.5f} - date: {}".format(k['side'],
                                                                                     k['size'],
                                                                                     float(k['price']),
                                                                                     float(k['fee']),
                                                                                     k['created_at'][:10])
        buy_sum_price += (float(k['size'])*(float(k['price'])+float(k['fee'])))
        buy_sum_size += float(k['size'])
        buy_fee += float(k['fee'])
    if k['product_id'] == "LTC-USD" and k['created_at'][:10] == calc_date and k['side'] == 'sell':
        print "side: {} - size: {} * price ${:3.5f} fee: ${:3.5f} - date: {}".format(k['side'],
                                                                                     k['size'],
                                                                                     float(k['price']),
                                                                                     float(k['fee']),
                                                                                     k['created_at'][:10])
        sell_sum_price += (float(k['size'])*(float(k['price'])+float(k['fee'])))
        sell_sum_size += float(k['size'])
        sell_fee += float(k['fee'])

if buy_sum_size > 0:
    buy_avg_price = buy_sum_price / buy_sum_size
else:
    buy_avg_price = 0
if sell_sum_size > 0:
    sell_avg_price = sell_sum_price / sell_sum_size
else:
    sell_avg_price = 0

print "\n\nTotal LTC Bought: {:2.3f} on {}".format(buy_sum_size, calc_date)
print "Total Price Paid: ${:3,.2f} on {}".format(buy_sum_price, calc_date)
print "Average Price Paid: ${:3,.2f}".format(buy_avg_price)
print "*" * 45
print "Total LTC Sould: {:2.3f} on {}".format(sell_sum_size, calc_date)
print "For a Total Of: ${:2,.2f} on {}".format(sell_sum_price, calc_date)
print "Average Price Sold: ${:3,.2f}".format(sell_avg_price)

