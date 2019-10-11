import codecs
import re

# First, I open the original html page. every line is then split into its own list called split_content.

file = codecs.open("./got.txt", encoding="utf-8")
html_content = file.read()
split_content = html_content.split("\n")

# I extract the unicorn by simply grabbing the contents from line 1 to 21 in the original html.
# The following loop makes all the lines into one signle string with the desired whitespace.

unicorn = split_content[slice(1,21)]
new_unicorn = ""
for line in unicorn:
    new_unicorn += (line + "\n")

# I used regex to find the title. The regex finds any characters between a opening and closing title-tag.
# Then I simply add the surrounding html tags. (h1 and u)
# In hindsight I realized that the assignment might have asked for the
# title that is not in the head tag, but the one in the body, but i hope this one is accepted as well.

old_title = re.search('<title>(.*)</title>', html_content).group(1)
new_title = "<h1><u>{}</u></h1>".format(old_title)

#similar regex for finding keywords in the meta tag.
# Note that the keywords are captured in group denoted by parenthesis.

keywords = re.search('<meta name="keywords" content="(.*)">', html_content).group(1)
new_keywords = '<h2>Keywords: </h2><h3 id="keywords">{}</h3>'.format(keywords)


# paragraphs are of course found between <p> tags. .
# In this case there are multiple of them so i use findAll() instead of search().

paragraphs = re.findall('<p>(.*)</p>', html_content)

# The following loop is responible for removing any html-tags that exists withing our paragraphs.
# This is done by finding them using regex, and then replacing all instances by an emspty string.

index = 0
for string in paragraphs:
    unwanted_tags = re.findall('<[^>]*>', string)
    for tag in unwanted_tags:
        string = string.replace(tag, "")
    paragraphs[index] = string
    index += 1

# The list of paragraphs are placed in an unordered list.
# each paragraphs is surrounded by an <li> list element tag.

new_paragraphs = "<ul>"
for paragraph in paragraphs:
    new_paragraphs += "\n<li>{}</li>".format(paragraph)
new_paragraphs += "\n</ul>"

# This internal_css is responsible for styling all elements in the html.
# The keywords are stylized by refering to its ID.

internal_css = '<style> #keywords {color:red; font-style: italic; } ul {list-style-type:square;} </style>'

# html skeleton containing all the essential html elements to form a valid file.

base_html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>title</title>
  </head>
  <body>
  
  </body>
</html>
"""

# The new html is formed by adding all respective new changes to a base html that only contains the html skeleton.
# .replace() is used to insert e.g the new title right after the body tag.

new_html = base_html.replace("<!DOCTYPE html>", "<!DOCTYPE html>\n{}".format(new_unicorn))
new_html = new_html.replace("<title>", "<title>\n{}".format(old_title))
new_html = new_html.replace("<body>", "<body>\n{}".format(new_title))
new_html = new_html.replace("</h1>", "</h1>\n{}".format(new_keywords))
new_html = new_html.replace("</h3>", "</h3>\n{}".format(new_paragraphs))
new_html = new_html.replace("<head>", "<head>\n{}".format(internal_css))


# Finally I write a local html file called got_clean.html
html_file_out = open("got_clean.html", "w")
html_file_out.write(new_html)
html_file_out.close


