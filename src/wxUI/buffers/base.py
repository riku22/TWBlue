# -*- coding: utf-8 -*-
import wx
from multiplatform_widgets import widgets

class basePanel(wx.Panel):
 
 def create_list(self):
  self.list = widgets.list(self, _(u"User"), _(u"Text"), _(u"Date"), _(u"Client"), style=wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.LC_VRULES)
  self.list.set_windows_size(0, 30)
  self.list.set_windows_size(1, 160)
  self.list.set_windows_size(2, 55)
  self.list.set_windows_size(3, 42)
  self.list.set_size()

 def __init__(self, parent, name):
  super(basePanel, self).__init__(parent)
  self.name = name
  self.type = "baseBuffer"
  self.sizer = wx.BoxSizer(wx.VERTICAL)
  self.create_list()
  self.tweet = wx.Button(self, -1, _(u"Tweet"))
  self.retweet = wx.Button(self, -1, _(u"Retweet"))
  self.reply = wx.Button(self, -1, _(u"Reply"))
  self.dm = wx.Button(self, -1, _(u"Direct message"))
  btnSizer = wx.BoxSizer(wx.HORIZONTAL)
  btnSizer.Add(self.tweet, 0, wx.ALL, 5)
  btnSizer.Add(self.retweet, 0, wx.ALL, 5)
  btnSizer.Add(self.reply, 0, wx.ALL, 5)
  btnSizer.Add(self.dm, 0, wx.ALL, 5)
  self.sizer.Add(btnSizer, 0, wx.ALL, 5)
  self.sizer.Add(self.list.list, 0, wx.ALL, 5)
  self.SetSizer(self.sizer)
