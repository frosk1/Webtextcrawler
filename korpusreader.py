#-*- coding: utf-8 -*-
import re

def filter(inputfile, outputfile):
    with open(inputfile, 'r') as inputs, open(outputfile, 'w') as output:
        count = 0
        for line in inputs:
            text = re.search("\{\"teaser\": \[\"(.*)\"\]\}", line)
            #print html_decode(text.group(1))
            output.write(str(count)+"\t"+"\t"+html_decode(text.group(1))+"\n")
            count += 1


def html_decode(s):
    htmlCodes = (
            ("ä", '\u00e4'),
            ('Ä', '\u00c4'),
            ('ö', '\u00f6'),
            ('Ö', '\u00d6'),
            ('ü', '\u00fc'),
            ('Ü', '\u00dc'),
            ('ß', '\u00df'))

    for code in htmlCodes:
        s = s.replace(code[1], code[0])
    return s


if __name__ == '__main__':

    filter("item.json","korpus.txt")
