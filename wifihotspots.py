import folium
import pandas as pd

borough = input("Please enter the name of the bourough: ").title()
outfile = borough.lower() + "wifihotspots.html"

data = pd.read_csv("./NYC_Wi-Fi_Hotspot_Locations_20241121.csv")

map = folium.Map(location=[40.768731, -73.964915], tiles="Cartodb dark_matter")

for index, row in data.iterrows():
    if row["Borough Name"] == borough:
        lat = row["Latitude"]
        long = row["Longitude"]
        name = row["Name"]
        provider = row["Provider"]
        ssid = row["SSID"]
        remarks = row["Remarks"]
        location = row["Location"]

        newMarker = folium.Marker(
            location=[lat, long],
            popup=f'''
<html>
<p>Name: {name}</p>
<p>Provider: {provider}</p>
<p>SSID: {ssid}</p>
<p>Location: {location}</p>
<p>Remarks: {remarks}</p>
</html>
'''
        )

        newMarker.add_to(map)

map.save(outfile)