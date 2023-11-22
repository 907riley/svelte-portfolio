import pandas as pd

def convert_date(date):
    months = {"1": "January", "2": "February", "3": "March", "4": "April", "5": "May", "6": "June", "7": "July", "8": "August", "9": "September", "10": "October", "11": "November", "12": "December"}
    date_split = date.split('/')
    date_string = months[date_split[0]] + " " + date_split[1] + ", " + date_split[2]
    return date_string

df = pd.read_csv('All Dev Blogs - Sheet1.csv')
df.reset_index()
df = df[::-1]

print(df.columns.values)
html_text = ""
for index, row in df.iterrows():
    temp = f"""<div class="content-wrapper">
    <div class="date-wrapper">
        {convert_date(row["Date"])}
    </div>
    <div class="one-liner-wrapper">
        {row["One Liner"]}
    </div>
    <div class="meat-wrapper">"""
        
    paragraphs = row["Content"].split("\r\n\r")
    paragraphs = [para.replace('\r', '').replace('\n', '') for para in paragraphs]
    print("PARAS", paragraphs)
    for para in paragraphs:
        temp += f"""
        <p class="paragraph-wrapper">
            {para}
        </p>"""
        temp += """
        <div></div>"""
    temp += f"""
    </div>
    <div class="divider-line"></div>
</div>
"""
    html_text += temp


f = open("htmlblog.txt", "w", encoding="utf8")
f.write(html_text)
f.close()

