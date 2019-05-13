import urllib2
import base64

url = "https://scontent-bom1-1.xx.fbcdn.net/v/t1.0-9/11917782_938039246275692_2461622507350184663_n.jpg?_nc_cat=0&oh=6e58d7c9213b78d14a017563e97239ef&oe=5C25D83F"
contents = urllib2.urlopen(url).read()
image = base64.b64encode(contents)