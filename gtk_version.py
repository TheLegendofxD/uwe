import gi, uwe

# Settings
VERSION = 2.0
WIN_TITLE = f"Uwe v{VERSION} (GTK3+)"
PRODUCT = "Uwe_GTK"

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self)
		self.set_border_width(10)
		
		header_bar = Gtk.HeaderBar()
		header_bar.set_show_close_button(True)
		header_bar.props.title = WIN_TITLE
		self.set_titlebar(header_bar)
		
		grid = Gtk.Grid()
		self.add(grid)
		
		# Creating widgets
		self.yt_url_lbl = Gtk.Label(label="YouTube-Url:   ")
		self.yt_url_input = Gtk.Entry()
		self.subtitle_settings_lbl = Gtk.Label()
		self.subtitle_settings_lbl.set_markup("\n<b>Subtitle Settings(Video-only):</b>")
		self.dwnld_subs_lbl = Gtk.Label(label="Download Subtitles:   ")
		self.dwnld_subs_chck = Gtk.CheckButton()
		self.dwnld_autosub_lbl = Gtk.Label(label="Use Auto-Subs:   ")
		self.dwnld_autosub_chck = Gtk.CheckButton()
		self.dwnld_embed_lbl = Gtk.Label(label="Embed Subs:   ")
		self.dwnld_embed_chck = Gtk.CheckButton()
		self.line_br = Gtk.Label(label="")
		self.vid_btn = Gtk.Button(label="Download Video")
		self.vid_btn.connect("clicked", self.download_file)
		self.aud_btn = Gtk.Button(label="Download Audio")
		self.link_lbl = Gtk.Label(label="")
		self.link_lbl.set_markup(f"\n<a href='https://github.com/TheLegendofxD/' title='TheLegendofxD on GitHub'>My GitHub</a>   <a href='https://github.com/TheLegendofxD/uwe#Changelog' title='README.md#Changelog'>Changelog</a>   <a href='mailto:legendxd@magenta.de?subject={PRODUCT}_v{str(VERSION)}_Feedback' title='Mail to legendxd@magenta.de'>Feedback</a>")
		self.aud_btn.connect("clicked", self.download_file)
		
		# Paking Widgets
		grid.add(self.yt_url_lbl)
		grid.attach(self.yt_url_input, 1,0, 1,1)
		grid.attach(self.subtitle_settings_lbl, 0,1, 2,1)
		grid.attach(self.dwnld_subs_lbl, 0,2, 1,1)
		grid.attach(self.dwnld_subs_chck, 1,2, 1,1)
		grid.attach(self.dwnld_autosub_lbl, 0,3, 1,1)
		grid.attach(self.dwnld_autosub_chck, 1,3, 1,1)
		grid.attach(self.dwnld_embed_lbl, 0,4, 1,1)
		grid.attach(self.dwnld_embed_chck, 1,4, 1,1)
		grid.attach(self.line_br, 0,5, 1,1)
		grid.attach(self.vid_btn, 0,6, 1,1)
		grid.attach(self.aud_btn, 1,6, 1,1)
		grid.attach(self.link_lbl, 0,7, 2,1)
		
		self.add_menu()
	def add_menu(self):
		pass
	def download_file(self, widget):
		url = self.yt_url_input.get_text()
		type = widget.get_label().replace("Download ", "")
		subs = self.dwnld_subs_chck.get_active()
		autosub = self.dwnld_autosub_chck.get_active()
		embed_subs = self.dwnld_subs_chck.get_active()
		
		uwe.download(url, type, subs, embed_subs, autosub)

App = MainWindow()
App.show_all()
App.connect("destroy", Gtk.main_quit)

Gtk.main()
