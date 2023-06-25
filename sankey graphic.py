
import pandas as pd
import plotly.graph_objects as go
import plotly.colors as colors

# Excel dosyasını okuyoruz ve verileri bir DataFrame'e aktarıyoruz
# Kodun calismasi icin kaynak klasorde bulunan "datacut.xlsx" veya "data.xlsx" verisinin indirildiktan sonra dosya
# yolunun "file_path= " satirinda belirtilmesi lazım.
file_path = "/Users/talipfurkanozdemir/Desktop/datacut.xlsx"
df = pd.read_excel(file_path)

'''# Veri setinin ilk 5 satırını gösterme
print(df.head())

# Veri setinin sütunlarını ve özelliklerini gösterme
print(df.info())

# Veri setinin istatistiksel özetini gösterme
print(df.describe())

# Her sütundaki eksik değer sayısını bulma
print(df.isnull().sum())'''

# 'SCORE.8' sütununu sayısal değerlere dönüştürüyoruz
df['SCORE.8'] = pd.to_numeric(df['SCORE.8'], errors='coerce')

# 'SCORE.8' ve 'Unnamed: 3' sütunlarında NaN değerleri içeren satırları kaldırıyoruz
df = df.dropna(subset=['SCORE.8', 'Unnamed: 3'], how='any')

# Kaynak, ara ve hedef düğümleri belirliyoruz
source = df['Unnamed: 3']
a1 = df['RANK']
a2 = df['RANK.1']
target = df['SCORE.8']
value = df['SCORE.8']
data = df.drop(columns=['Unnamed: 3', 'RANK.3', 'RANK.4', 'RANK.5', 'SCORE.8'])

# Düğüm etiketlerini birleştirerek benzersiz kavramları elde ediyoruz
labels = pd.concat([source, a1, a2, target]).unique()

# Her kavrama bir indeks atıyoruz
node_dict = {label: index for index, label in enumerate(labels)}

# Renk skalasını belirliyoruz
color_scale = colors.sequential.Plasma

# Hedef düğümün renk indeksini hesaplıyoruz
color_index = (target - target.min()) / (target.max() - target.min()) * (len(color_scale) - 1)
color_index = color_index.astype(int)

# Düğüm renklerini belirliyoruz
node_colors = [color_scale[idx] for idx in color_index]

# Bağlantıları temsil eden bir liste oluşturuyoruz
links = []

# Hovertemplate formatını belirliyoruz
hovertemplate = '</i><b><i> %{customdata[2]}</i></b> <br>' + \
                 '2023WorldRank: <b>%{customdata[0]}</b><br>' + \
                 '2023WorldRank: <b>%{customdata[1]}</b><br>' + \
                 'Academic Reputation Rank: <b>%{customdata[10]}</b><br>' + \
                 'Faculty Student Rank: <b>%{customdata[15]}</b><br>' + \
                 'Citations per Faculty Rank: <b>%{customdata[17]}</b><br>' + \
                 'International Faculty Rank: <b>%{customdata[19]}</b><br>' + \
                 'International Students Rank: <b>%{customdata[21]}</b><br>'

# Her bir bağlantı için gerekli verileri kullanarak bağlantıları oluşturuyoruz
for src, a, b, tgt, val, color, row in zip(source, a1, a2, target, value, node_colors, data.itertuples()):

    # Kaynak düğümü ve ara düğümü birleştiren bağlantıyı ekliyoruz
    links.append(dict(
        source=node_dict[src],
        target=node_dict[a],
        value=val,
        color=color,
        customdata=row[1:],
    ))

    # Ara düğümü ve hedef düğümü birleştiren bağlantıyı ekliyoruz
    links.append(dict(
        source=node_dict[a],
        target=node_dict[b],
        value=val,
        color=color,
        customdata=row[1:]
    ))

    # Hedef düğümü ve SCORE.8 değerini birleştiren bağlantıyı ekliyoruz
    links.append(dict(
        source=node_dict[b],
        target=node_dict[tgt],
        value=val,
        color=color,
        customdata=row[1:]
    ))

# Plotly figürünü oluşturuyoruz
fig = go.Figure(data=[go.Sankey(
    node=dict(
        label=labels,
        color=node_colors
    ),
    link=dict(
        source=[link['source'] for link in links],
        target=[link['target'] for link in links],
        value=[link['value'] for link in links],
        color=[link['color'] for link in links],
        hovertemplate=hovertemplate,
        customdata=[link['customdata'] for link in links]
    )
)])

# Figürün arka plan ve kağıt arka plan renklerini belirliyoruz
fig.update_layout(
    plot_bgcolor='white',
    paper_bgcolor='white'
)

# Figürü görüntülüyoruz
fig.show()
