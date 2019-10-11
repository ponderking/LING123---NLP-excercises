import codecs

# Reading of original text poem.
file = codecs.open("./shake.txt", encoding="utf-8")
poem = file.read()


# The poem is split into each stanza, which are separated by two new lines in a row.
stanza_list = poem.split("\n\n")

# The poem is further split into each line of each stanza.
index = 0
for stanza in stanza_list:
    stanza_list[index] = stanza.split("\n")
    index += 1


# DTD that defines structure rules. For instance all tokens must have a wordform and rhyme child-element.
#

DTD = """<!DOCTYPE poem [
<!ELEMENT poem (stanza+)>
<!ATTLIST poem title CDATA #IMPLIED >
<!ATTLIST poem author CDATA #IMPLIED >
<!ELEMENT stanza (token+)>
<!ATTLIST stanza s-id CDATA #REQUIRED >
<!ELEMENT token (wordform,rhyme)>
<!ATTLIST token t-id CDATA #REQUIRED >
<!ELEMENT wordform (#PCDATA)>
<!ELEMENT rhyme (#PCDATA)>
]>\n
"""


# Beginning of output xml. also inserts the DTD
final_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n
{}
<poem>\n""".format(DTD)


# This loop is resposible for going through creating the xml structure specified in the DTD
# and to insert the data from the poem.

stanza_counter = 1
token_counter = 1
rhyme_index = 1
for stanza in stanza_list:
    # stanza parent element that will contain token information.
    final_xml += '\t<stanza s-id="{}">\n'.format(stanza_counter)
    # There are three types of rhymes. A,B and C.
    # A belongs to line 1 and 2, B to 3 and 6, C to 4 and 5.
    for line in stanza:
        if rhyme_index == 1 or rhyme_index == 2:
            rhyme_type = "A"
        elif rhyme_index == 3 or rhyme_index == 6:
            rhyme_type = "B"
        else:
            rhyme_type = "C"
        # split each line into individual words.
        tokens = line.split(" ")
        for token in tokens:
            # escape character must not be ignored
            if "&" in token:
                token = token.replace("&", "&amp;")
            # fills in the required tags and data for the xml.
            final_xml += '\t\t<token t-id="{}-{}">' \
                         '\n\t\t\t<wordform>' \
                         '\n\t\t\t\t{}' \
                         '\n\t\t\t</wordform>' \
                         '\n\t\t\t<rhyme>' \
                         '\n\t\t\t\t{}' \
                         '\n\t\t\t</rhyme>' \
                         '\n\t\t</token>\n'.format(stanza_counter, token_counter, token, rhyme_type)
            token_counter += 1
        rhyme_index += 1
    final_xml += "\t</stanza>\n"
    # reset rhyme and token counter for the next stanza,
    rhyme_index = 0
    token_counter = 0
    # move on to next stanza.
    stanza_counter += 1
# end of xml
final_xml += "</poem>"


# Finally I write the finished xml to a local file called poem.xml
xml_file_out = open("poem.xml", "w")
xml_file_out.write(final_xml)
xml_file_out.close
