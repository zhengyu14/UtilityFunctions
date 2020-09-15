import pandas as pd 

import StockPrice as SP
import SupportLine as SL

data = SP.get_close_price_1m('9939.hk')
convex, concave = SL.get_turnings(data)

# Visualization
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
plt.plot(data['High'], color='#2B7C2B')
plt.plot(data['Low'], color='#880000')
plt.scatter(convex.index, convex['High'], color='#ABE2AB')
plt.scatter(concave.index, concave['Low'], color='#FF8888')
ax.set_facecolor(color='#333333')
plt.grid(color='#666666')
plt.show()