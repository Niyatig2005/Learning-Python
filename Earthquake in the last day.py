import urllib.request
import json


def MakingHTLM(title, work, count, location, magnitude, felt, theJSON):
    doesitwork = work.getcode()
    file = open("Earthquakes in the last day bigger than magnitude 2.5.html", "w+")
    file.write("<html>")
    file.write("<title>Earthquakes</title>")
    file.write("<h1>")
    file.write(title)
    file.write("</h1>")
    file.write("<body>")
    file.write("<h3>")
    file.write("Number of events recorded: {}".format(count))
    file.write("<p>----------------------------------------------------<p>")
    file.write("</h3>")
    for i in theJSON["features"]:
        location = i["properties"]["place"]
        magnitude = str(i["properties"]["mag"])
        felt = str(i["properties"]["felt"])
        file.write("<div>")
        file.write("<p>")
        file.write("Location: {}".format(location))
        file.write("</p>")
        file.write("<p>")
        file.write("Magnitude: {}".format(magnitude))
        file.write("</p>")
        file.write("<p>")
        file.write("Number of Felt Reports: {}".format(felt))
        file.write("</p>")
        file.write("<p>----------------------------------------------------<p>")
        file.write("</div>")
    file.write("</body>")
    file.write("</html>")




def Printing(data, work):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

    if "title" in theJSON["metadata"]:
        title = theJSON["metadata"]["title"]
        print(title, "\n")
    count = theJSON["metadata"]["count"]
    print("Number of events recorded: ", count, "\n")
    for i in theJSON["features"]:
        location = i["properties"]["place"]
        magnitude = str(i["properties"]["mag"])
        felt = str(i["properties"]["felt"])
        print("Location: ", location, "\n","Magnitude: ", magnitude, "\n", "Number of Felt Reports: ", felt, "\n")
    MakingHTLM(title, work, count, location, magnitude, felt, theJSON)

    
    
        
def main():
    website = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    # Website with earthquakes within the last day bigger than magnitude 2.5
    work = urllib.request.urlopen(website)
    print("Result code (404 means 'not found', 200 means it works!): " + str(work.getcode()) + "\n")
    if (work.getcode() == 200): #if 200, reaching website works
        data = work.read().decode("utf-8")
        Printing(data, work)
    else:
        print("Getting to website didn't work")
main()
