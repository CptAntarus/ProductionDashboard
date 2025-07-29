import re

class Waterfall():
    def InitDataSection(section):
        DataFromTxt = {}
        sectionHeaderPat = re.compile(r"^\[(.+?)\]$")
        currentSection = None
        isInSection = False

        sectionPat = r"^\s*{.+}$"
        namePat = r"\{(.*?)\s*:"
        tagPat = r":\s*(.*?)\}"

        with open("Bob.txt","r") as file:
            for line in file:
                line = line.strip()
                headerMatch = sectionHeaderPat.match(line)

                if headerMatch:
                    currentSection = headerMatch.group(1)
                    isInSection = (currentSection == section)
                    continue

                if isInSection and re.match(sectionPat, line):
                    # print(line)
                    nameMatch = re.search(namePat, line)
                    tagMatch = re.search(tagPat, line)
                    if nameMatch and tagMatch:
                        name = nameMatch.group(1)
                        tag = tagMatch.group(1)

                        DataFromTxt[name] = tag
        
        return DataFromTxt
