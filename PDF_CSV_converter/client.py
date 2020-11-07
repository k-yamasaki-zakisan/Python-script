import tabula
import pandas as pd
import collections

dfs = tabula.read_pdf("./sample1.pdf", stream=True, pages='all')

# convert PDF into CSV file
tabula.convert_into("./sample1.pdf", "output.csv", output_format="csv", stream=True,pages='all')