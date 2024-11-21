# 1-Up Workshop: Visualizing Wi-Fi Hotspots with Python and Folium

## **Overview**

In this 1-Up, we will use **Pytho**n and the **Folium** library to visualize free Wi-Fi hotspot locations on an interactive map, utilizing a data set from NYC's Open Data website. We'll walk through the code step-by-step, understanding the tools, parameters, and techniques used.

## **What You'll Learn**
- How to use Pandas to load and filter data from a CSV file.
- How to use Folium to create interactive maps.
- How to dynamically generate HTML maps based on user input.

## **Tools and Libraries**

### **1. Folium**
- **What is it?**
  - Folium is a Python library used for creating interactive maps.
- **What is it for?**
  - It allows you to visualize geospatial data by rendering Leaflet.js maps directly in Python.
- **When do we use it?**
  - When you need to display location-based data (e.g., points, polygons) interactively.
- **Features:**
  - Supports map tiles, markers, popups, and custom icons.
  - Generates HTML-based interactive maps.

### **2. Pandas**
- **What is it?**
  - Pandas is a powerful Python library for data manipulation and analysis.
- **What is it for?**
  - It provides DataFrame objects for handling tabular data, which are especially useful for filtering and organizing data for visualization.
- **When do we use it?**
  - When working with structured datasets (e.g., CSV files) that require filtering or preprocessing.

---
## **Code Walkthrough**

### **Objectives**
1. Take a borough name as input.
2. Filter Wi-Fi hotspot data for that borough from a CSV file.
3. Create an interactive map with markers for each Wi-Fi hotspot.
4. Save the map as an HTML file.

## **Steps in the Code**

### **1. Import Libraries**
We start by importing the necessary libraries:
```python
import folium  # Import Folium for map creation
import pandas as pd  # Import Pandas for data manipulation
```
- **Explanation**:
  - `folium` is used for creating the interactive map and adding markers.
  - `pandas` is used for loading and filtering the dataset (CSV file).

---

### **2. Take User Input**
Take the borough name from the user and format it properly:
```python
borough = input("Please enter the name of the borough: ").title()
```
- **Explanation**:
  - `input()` takes the borough name from the user (e.g., "Queens").
  - `.title()` ensures that the input matches the format in the dataset (e.g., "queens" becomes "Queens").

---

### **3. Generate Output File Name**
Create an output file name dynamically based on the borough:
```python
outfile = borough.lower() + "wifihotspots.html"
```
- **Explanation**:
  - Converts the borough name to lowercase using `.lower()`.
  - Concatenates it with `"wifihotspots.html"` to create a custom file name, e.g., `queenswifihotspots.html`.

---

### **4. Load the Data**
Load the Wi-Fi hotspot data from the CSV file into a Pandas DataFrame:
```python
data = pd.read_csv("./NYC_Wi-Fi_Hotspot_Locations_20241115.csv")
```
- **Explanation**:
  - `pd.read_csv()` reads the CSV file into a DataFrame.
  - The file contains Wi-Fi hotspot details, including location (latitude, longitude), provider, and borough.

---

### **5. Create the Base Map**
Initialize a base map centered on New York City:
```python
map = folium.Map(location=[40.768731, -73.964915])  # Centered around NYC coordinates
```
- **Explanation**:
  - `folium.Map()` creates the base map.
  - The `location` parameter sets the center of the map using latitude and longitude (here, coordinates for NYC).
  - `tiles`: (Optional) Specifies the map style (e.g., "Cartodb dark_matter" for a dark map).

---
### **6. Filter Data and Add Markers**
Loop through the dataset, filter rows for the specified borough, and add markers to the map.

```python
# Loop through each row of the DataFrame
for index, row in data.iterrows():
    # Check if the current row belongs to the specified borough
    if row["Borough Name"] == borough:
        # Extract the latitude, longitude, and Wi-Fi hotspot name
        lat = row["Latitude"]
        lon = row["Longitude"]
        name = row["Name"]

        # Create a marker for the hotspot
        newMarker = folium.Marker(
            location=[lat, lon],  # Latitude and longitude of the marker
            popup=f'''
            <html>
            <p>Name: {name}</p>
            <p>Provider: {row["Provider"]}</p>
            <p>SSID: {row['SSID']}</p>
            <p>Location: {row['Location']}</p>
            <p>Remarks: {row['Remarks']}</p>
            </html>
            '''  # Popup HTML containing hotspot details
        )
```

#### **Filter and Iterate Through the Data**
```python
for index, row in data.iterrows():
    if row["Borough Name"] == borough:
```
- **Explanation**:
  - `data.iterrows()` iterates through rows of a DataFrame, returning both the row index and the row data.
  - `row["Borough Name"] == borough` checks if the "Borough Name" column matches the user input.

#### **Extract Data for Each Wi-Fi Hotspot**
```python
lat = row["Latitude"]
lon = row["Longitude"]
name = row["Name"]
```
- **Explanation**:
  - Extracts the latitude, longitude, and name of the Wi-Fi hotspot from the current row.

#### **Create and Add a Marker**
```python
newMarker = folium.Marker(
    location=[lat, lon],  # Latitude and longitude of the marker
    popup=f'''
    <html>
    <p>Name: {name}</p>
    <p>Provider: {row["Provider"]}</p>
    <p>SSID: {row['SSID']}</p>
    <p>Location: {row['Location']}</p>
    <p>Remarks: {row['Remarks']}</p>
    </html>
    '''  # Popup HTML containing hotspot details
)
newMarker.add_to(map)
```
- **Explanation**:
  - `folium.Marker()` creates a marker at the specified latitude and longitude.
  - The `popup` parameter specifies the HTML content displayed when the marker is clicked.
  - `newMarker.add_to(map)` adds the marker to the map.

---

### **7. Save the Map**
Save the final map as an HTML file:
```python
map.save(outfile)
```
- **Explanation**:
  - `map.save()` generates an HTML file containing the interactive map.
  - The file can be opened in a web browser to view the map.

---

### **Complete Code Flow**
Here’s how the steps come together:
1. The user enters a borough name (e.g., "Manhattan").
2. The script filters Wi-Fi hotspot data for that borough.
3. A base map is created and centered on NYC.
4. Markers for each hotspot in the borough are added to the map.
5. The final map is saved as an HTML file, which can be shared or viewed in a browser.

## **Parameters and Customizations**

### **1. folium.Map**
- `location`: Specifies the center of the map as `[latitude, longitude]`.
- `tiles`: (Optional) Specifies the map style (e.g., `"Cartodb dark_matter"` for a dark map).

### **2. folium.Marker**
- `location`: `[latitude, longitude]` coordinates of the marker.
- `popup`: HTML content displayed when the marker is clicked.

### **3. Pandas `DataFrame.iterrows()`**
- Iterates through rows of a DataFrame, returning both the row index and the row data.

---

## **When and Why to Use It**
- **When**: Anytime you need to visualize geospatial data or present location-based data interactively.
- **Why**:
  - Makes geospatial data easier to understand and explore.
  - Allows dynamic customization and user-driven exploration.
