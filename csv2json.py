import sublime, sublime_plugin,json

# Builds a JSON array in a new window given a comma separated file
# where the first row contains the column names.
# Example: Given the followin input
#
# BoxNo,BoxDescription,InputName
# 1,Name of Employee,eeName
# 2,Social Security Number (SSN),eeSSN
# 3,Street address (including apartment no.) ,eeStreet
# 4,City or town ,eeCity
#
# Generates the following output in a new window.
# [{"InputName": "eeName", "BoxDescription": "Name of Employee", "BoxNo": "1"}, {"InputName": "eeSSN", "BoxDescription": "Social Security Number (SSN)", "BoxNo": "2"}, {"InputName": "eeStreet", "BoxDescription": "Street address (including apartment no.) ", "BoxNo": "3"}, {"InputName": "eeCity", "BoxDescription": "City or town ", "BoxNo": "4"}]



class csv2jsonCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        output = []
        content = self.view.substr(sublime.Region(0, self.view.size()))
        lines = content.split("\n")
        keys = lines[0].split(",")
        for line in lines[1:]:
            if line.strip() != "":
                vals = line.split(",")
                dictionary = dict(zip(keys, vals))
                output.append(dictionary)
        currentWindow = self.view.window()
        print(dir(currentWindow))
        newView = currentWindow.new_file()
        newView.insert(edit,0,json.dumps(output))




