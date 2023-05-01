## About the Project

**Predicting Market Boom and Bust Periods: A Multi-Year Analysis of Financial Metrics in Top Companies Across Major Industries**

#### Abstract

This study aims to investigate the predictability of market trends by analyzing the financial metrics of top companies in five major industries (technology, financial services, consumer goods, energy, and healthcare) over a 40-year period (1982-2022). We approach market cycle predictability as a reaction to impending market movements. Financial accounting data from top companies in each industry are analyzed to examine their ability to predict market boom and bust periods. By examining the interplay between company financial statistics and market trends, this study seeks to provide insights into the predictability of market fluctuations and its implications for investors and financial analysts. The findings of this study could inform investment strategies in a rapidly changing financial landscape and contribute to the ongoing discourse around market predictability, along with providing a better understanding of the relationship between company performance and market trends— particularly in the current economic climate where financial markets face a recession and the aftereffects of COVID-19.

#### Hypotheses

The financial performance of Healthcare companies will be a better predictor of market trends than the financial performance of companies in other industries.

#### Data

|                                                |                                                                                          |
| :--------------------------------------------- | :--------------------------------------------------------------------------------------: |
| Data file with `main` tab used for STATA       |      [link](https://github.com/keirkeenan/data-science-project/data/main_data.xlsx)      |
| Python script to scrape desired financial data |       [link](https://github.com/keirkeenan/data-science-project/data/parser.ipynb)       |
| Python code to create circle packing visual    | [link](https://github.com/keirkeenan/data-science-project/data/circle_packing_visual.py) |

#### Results

![Figure 1](https://github.com/keirkeenan/data-science-project/images/figure1.png)

**Figure 1:** Demonstrates the correlation between individual industry prediction models and the growth of the United States Gross Domestic Product (GDP) from 1984 to 2022. Emphasis is placed on the frames highlighting GDP spikes, which correspond to four distinct recessionary periods. Among the industry models, those representing technology and consumer discretionary sectors exhibited the strongest alignment with market fluctuations, attributable to their inherent volatility.

![Figure 2](https://github.com/keirkeenan/data-science-project/images/figure2.png)

**Figure 2:** Uses circle packing to demonstrate the relative weight of each variable as an indicator of market movements. The orange circles represent the weight of each industry, while the green circles represent the top financial data variables within each respective industry. Across the board, gross profit growth is the most influential indicator across five out of the six examined industries. In industries with lower volatility— like consumer discretionary— small percentage changes received a larger weight in the model compared to larger percent changes in more volatile industries like technology.

#### Conclusion

Forecasting market fluctuations is a crucial aspect of avoiding financial downturns and avoiding large financial losses. This study aimed to investigate the predictability of market trends by analyzing the financial metrics of top companies across five major industries over a 40-year period and provide a better understanding of the predictability of market fluctuations and its implications. Our research determined that no single industry was a significant predictor of recession throughout the observed time period. Each recession had unique origins tied to different geopolitical and economic factors that impacted respective industries in varied ways. We found it difficult to perform market trend predictions without the required macroeconomic context. Our findings inform investment strategies in a rapidly changing financial landscape and provide valuable insights into the relationship between company performance and market trends. As financial markets continue to face uncertainty, policymakers, businesses, and individuals can take data-driven approaches to prepare for and mitigate the catastrophic impacts of potential recession.

## Contributors

- Evan Kim
- Fraye Beyene
- Keir Keenan
- Nira Nair
