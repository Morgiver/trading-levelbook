# Trading Level Book
This package will provide tools to create and manage a trading level book.

With this you can manage an Order book for example, or a liquidations levels book or the three at the same time.

Example :
```Python
book = Book(columns = 3) # 3 columns for bids, asks and liquidations

bids = [
  [65000.1, 150],
  [65000.3, 95]
]

asks = [
  [65001.0, 98],
  [65001.2, 300]
]

liquidations = [
  [64500, 400],
  [65600, 200]
]

book.feed(bids, asks, liquidations)

# After that every level will be like
# [bid_volume, ask_volume, liquidation_volume]
```

Every data sended will update the volume in the right column as long as you respect the order when you send the datas in the feed() method
