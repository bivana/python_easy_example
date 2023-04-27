import os
import pandas as pd
import camelot 


# 读取pdf文件，获取pdf的表格数据，并保存为csv
pdfFilePath="foo.pdf"
csvFilePath="table.csv"
separate_coma=","

# 使用camelot解析table，all为解析所有的pdf page
tables= camelot.read_pdf(pdfFilePath,pages='all')
# 将所有的table 拼接为一个df
table_df=tables[0].df
for i in range(1,len(tables)):
     table_df=table_df._append(tables[i].df)
# 加入自定义字段
table_df['report_date']='2023-02-28'
# 调整顺序，放入第一个
table_df.insert(0,'report_date',table_df.pop('report_date'))
print(table_df)
# 保存为csv文件，为后续入库方便，去除index
table_df.to_csv(csvFilePath,index=None)
print("foo table data finished")
