# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version May 25 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import math

import matplotlib.pyplot as plt

from NlpToolKit import NlpToolKit
from Summarizer import TextProcessor

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		self.nlpToolKit = NlpToolKit()
		self.summarizer = TextProcessor()

		self.doc = ""

		wx.Frame.__init__( self, parent, id = wx.ID_ANY, title = u"Natural Language Processing", pos = wx.DefaultPosition, size = wx.Size( 1366,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))
		#self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer2.SetMinSize( wx.Size( -1,20 ) ) 
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Summarization with Porter Stemming", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetFont(wx.Font(15, 74, 90, 92, False, "Arial Black"))
		bSizer2.Add( self.m_staticText3, 0, wx.ALL|wx.CENTER, 5 )

		sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Input Text Here"), wx.VERTICAL)
		self.m_textCtrl3 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		sbSizer1.Add(self.m_textCtrl3, 1, wx.EXPAND|wx.ALL, 5)
		bSizer4.Add( sbSizer1, 1, wx.EXPAND|wx.ALL, 10 )

		sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Summary Result"), wx.VERTICAL)
		self.m_textCtrl4 = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		sbSizer2.Add(self.m_textCtrl4, 1, wx.EXPAND | wx.ALL, 5)
		bSizer4.Add( sbSizer2, 1, wx.EXPAND|wx.ALL, 10 )

		bSizer2.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Summarize", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button1, 0, wx.ALL|wx.CENTER, 5 )
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Token Freq"), wx.VERTICAL)
		self.m_textCtrl1 = wx.TextCtrl(  sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		sbSizer3.Add(self.m_textCtrl1, 1, wx.EXPAND | wx.ALL, 5)
		bSizer3.Add( sbSizer3, 1, wx.EXPAND|wx.ALL, 10 )

		sbSizer4 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"TF-IDF Each Sentences"), wx.VERTICAL)
		self.m_textCtrl2 = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		sbSizer4.Add(self.m_textCtrl2, 1, wx.EXPAND | wx.ALL, 5)
		bSizer3.Add( sbSizer4, 1, wx.EXPAND|wx.ALL, 10 )
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

		# self.m_gauge1 = wx.Gauge(self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL)
		# self.m_gauge1.SetValue(0)
		# bSizer1.Add(self.m_gauge1, 0, wx.EXPAND|wx.ALL, 5)
		
		self.SetSizer( bSizer1 )
		self.Layout()

		# self.m_menubar1 = wx.MenuBar(0)
		# self.m_menu1 = wx.Menu()
		# self.m_menuItem1 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"Save Text", wx.EmptyString, wx.ITEM_NORMAL)
		# self.m_menu1.AppendItem(self.m_menuItem1)
		#
		# self.m_menubar1.Append(self.m_menu1, u"File")
		#
		# self.SetMenuBar(self.m_menubar1)
		
		self.Centre( wx.BOTH )

		self.m_button1.Bind( wx.EVT_BUTTON, self.onClickStem )
		#self.Bind(wx.EVT_MENU, self.onSave, id=self.m_menuItem1.GetId())
		#self.m_menuItem1.Bind( wx.EVT_MENU, self.onSave )
		# wx.EVT_MENU( self, self.onSave, self.m_menu11 )
	
	def __del__( self ):
		pass

	def onClickStem( self, event ):
		# ambil text pada textbox
		source = self.m_textCtrl3.GetValue()
		# tokenize
		tokens = self.nlpToolKit.tokenize( source )
		# stemming menggunakan porter
		stems  = self.nlpToolKit.stem( tokens )
		# self.m_textCtrl2.SetValue( '\n'.join(stems) )

		#split dokumen setiap paragraf
		paragraphs = self.summarizer.splitParagraphs( source )
		#spot paragraf menjadi kalimat
		sentences  = [j for sub in [self.summarizer.splitSentences( sent ) for sent in [p for p in paragraphs]] for j in sub]
		sentences  = [i for i in sentences if i != '']

		#hasil kalimat yang sudah di di tokenize, stopword, dan di stemming
		tokenized_sentences = [self.nlpToolKit.stem( self.nlpToolKit.stopwords_removal( self.nlpToolKit.tokenize( sentence ) ) ) for sentence in sentences]

		#hasil idf dari setiap kalimat
		idf = self.nlpToolKit.inverse_document_frequencies( tokenized_sentences )

		#mencari tf-idf pada setiap kalimat
		tfidf_sentences = []

		for sentence in tokenized_sentences:
			sent_tfidf = []
			for term in idf.keys():
				tf = self.nlpToolKit.sublinear_term_frequency( term, sentence )
				sent_tfidf.append( tf * idf[term] )
			tfidf_sentences.append( sent_tfidf )

		our_tfidf_comparisons = []

		for count_0, doc_0 in enumerate( tfidf_sentences ):
			for count_1, doc_1 in enumerate( tfidf_sentences ):
				our_tfidf_comparisons.append(( self.nlpToolKit.cosine_similarity(doc_0, doc_1), count_0, count_1 ))

		sentences_count = int( math.sqrt( len( our_tfidf_comparisons ) ) )

		ranks = sorted( our_tfidf_comparisons, key = lambda x: int(x[1]))
		ranks = ranks[:sentences_count]
		ranks = zip(ranks, sentences)

		all_tokens = [token for sentence in tokenized_sentences for token in sentence]

		# menggabungkan kalimat dengan hasil tf-idf
		ranks_with_sentences = map(lambda x: [x[1], x[0][0]], ranks)
		print_to_text2 = ''

		for rws in ranks_with_sentences:
			str_value 		= rws[0] + ' [' + str(rws[1]) + ']\n\n'
			print_to_text2 += str_value

		print_to_text1 = ''

		#menggabungkan kata dengan hasil idf
		for term in idf:
			count = str(all_tokens.count(term))
			str_value = term + '    ' + count + '    ' + str(idf[term]) + '\n\n'
			print_to_text1 += str_value
		
		sum_len = int(math.ceil(0.3 * len(ranks)))

		ranks = sorted( ranks, key = lambda x: x[0][0], reverse=True )[:sum_len]
		ranks = sorted( ranks, key = lambda x: x[0][2] )

		# perbandingan nilai idf setiap token
		# plt.bar(range(len(idf)), list(idf.values()), align='center')
		# plt.xticks(range(len(idf)), list(idf.keys()))

		# self.m_textCtrl1.SetValue( '\n'.join([j for sub in tokenized_sentences for j in sub]) )
		#textbox output agar tidak bisa di edit
		self.m_textCtrl1.SetEditable(False)
		self.m_textCtrl2.SetEditable(False)
		self.m_textCtrl4.SetEditable(False)

		#menampilkan output sesuai textbox yang disiapkan
		self.m_textCtrl1.SetValue( print_to_text1 )
		self.m_textCtrl2.SetValue( print_to_text2 )
		self.m_textCtrl4.SetValue( '. '.join([sentence[1] for sentence in ranks]) )
		
		self.doc = "<source>", source, "</source>", "<tokens>", '\n'.join(tokens), "</tokens>", "<stems>", '\n'.join(stems), "</stems>"
		plt.show()

	#fungsi tombol save
	# def onSave( self, event ):
	# 	if self.doc != "" :
	# 		dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.SAVE | wx.OVERWRITE_PROMPT)
	#
	# 		if dlg.ShowModal() == wx.ID_OK :
	# 			itcontains = self.doc
	# 			self.filename=dlg.GetFilename()
	# 			self.dirname=dlg.GetDirectory()
	# 			filehandle=open(os.path.join(self.dirname, self.filename),'w')
	# 			filehandle.write(itcontains)
	# 			filehandle.close()
	# 		dlg.Destroy()
	#


#membuat aplikasi
app = wx.App(False)

#membuat objek MyFrame1
frame = MyFrame1(None)
#menampilkan frame
frame.Show(True)
#menjalankan aplikasi
app.MainLoop()
