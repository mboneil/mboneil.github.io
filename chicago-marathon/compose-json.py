import re, json

# A Python file to extract the coordinates from a XML/KML file into a JSON format for easy integration into a Google Maps page via their Javascript API


# helper function that separates a string based on commas, then returns a dictionary with longitude and latitude.
def extractLatLong(str):
	arr = str.split(',')
	return {'long': arr[0], 'lat': arr[1]}

# the main function, reads input xml file, parses it and writes output json file
def main():
	with open ("route.xml", "r") as myfile:
		data = myfile.read().replace('\n', '')
		matches = re.findall("<coordinates>\s+([\w.-]+,[\w.-]+,[\w.-]+)\s([\w.-]+,[\w.-]+,[\w.-]+)", data)

		paths = [ { 'start': extractLatLong(match[0]), 'end': extractLatLong(match[1]) } for match in matches]

		with open ("route.json", "w") as outFile:
			outFile.write(json.dumps(paths,  sort_keys=True, indent=4, separators=(',', ': ')))
		



# if run this from commandline "python compose-json.py", run the main function
if __name__ == "__main__":
	main()