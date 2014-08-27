import sublime, sublime_plugin
import webbrowser
import urllib

class HuelyCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# base_url = "http://huely.co"
		base_url = "http://localhost:3000" # for development

		url = base_url + "/api/extract"
		
		# get the current view's contents
		data = {
			# 'text': "#333"
			'text': self.view.substr(sublime.Region(0, self.view.size()))
		}

		# urlencode the data to be sent
		data = urllib.parse.urlencode(data)
		# encode the text data into bytes data
		binary_data = data.encode("utf8")
		response = urllib.request.urlopen(url, binary_data)
		# decode the response. will be a palette ID if colors were extracted
		palette_id = response.read().decode()

		if palette_id:
			webbrowser.open_new_tab(base_url+"/palette/"+palette_id)
		else:
			print("No colors extracted")
