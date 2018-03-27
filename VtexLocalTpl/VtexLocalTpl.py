import sublime
import sublime_plugin
import re

"""
	Clean HTML to make a Vtex template

	Removes all content between <!-- delete --> and <!-- delete:end -->
"""
class CleanFileCommand(sublime_plugin.TextCommand):

	def clean(self, view, edit):
		regex = r".*<!--[\s]?delete((?s).*?)delete:end[\s]?-->"
		regions = view.find_all(regex)
		regions.sort(key=lambda region: region.a, reverse=True)

		for region in regions:
			view.erase(edit,region)

	def run(self, edit):
		if self.view.is_read_only() or self.view.size() == 0:
			return
		self.clean(self.view, edit)


"""
	Uncomment Vtex Tags
"""
class UncommentVtexTagsCommand(sublime_plugin.TextCommand):

	def uncomment_all(self, view, edit):
		regex = r"<![\s-]*(<vtex.*\/>)[\s-]*>"
		regions = view.find_all(regex)
		regions.sort(key=lambda region: region.a, reverse=True)

		for region in regions:
			commented_text = view.substr(region)
			vtex_tag_regex = r"(<vtex.*\/>)"
			vtex_tag = re.search(vtex_tag_regex,commented_text)
			if vtex_tag:
				view.replace(edit, region, vtex_tag.group())

	def run(self, edit):
		if self.view.is_read_only() or self.view.size() == 0:
			return
		self.uncomment_all(self.view, edit)
		

class SwapCommand(sublime_plugin.TextCommand):

	def swap_all(self, view, edit):
		regex = r"<(script|link)((?!<)[\s\S\w])*?(?:vtex=).*?>"
		regions = view.find_all(regex)
		regions.sort(key=lambda region: region.a, reverse=True)

		for region in regions:
			selection = view.substr(region)
			regex = r"[ ]?(href|src)=([\"\']).*?\2"
			selection = re.sub(regex,'',selection)
			regex = r"(vtex)=([\"\'].*?[\"\'])"
			if re.search(r"link",selection):
				selection = re.sub(regex,r"href=\2",selection)
			else:
				selection = re.sub(regex,r"src=\2",selection)
			view.replace(edit, region, selection)

	def run(self, edit):
		if self.view.is_read_only() or self.view.size() == 0:
			return
		self.swap_all(self.view, edit)


class FullCleanUpCommand(sublime_plugin.TextCommand):
	
	def run(self, edit):
		if self.view.is_read_only() or self.view.size() == 0:
			return

		sublime.active_window().run_command('clean_file')
		sublime.active_window().run_command('uncomment_vtex_tags')
		sublime.active_window().run_command('swap')
