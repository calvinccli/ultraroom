"""Simple HTTP Server With Upload - test branch 1234.

This module builds on BaseHTTPServer by implementing the standard GET and HEAD requests in a fairly straightforward manner.

"""
__version__ = "0.1"
__all__ = ["SimpleHTTPRequestHandler"]
__author__ = "someone"
__home_page__= "Caution-http://li2z.test/ < Caution-http://li2z.test/ > "



import os
import posixpath
import BaseHTTPServer
import urllib
import cgi
import shutil
import mimetypes
import re
import postMultiPart
import sys
import socket
import ssl
import datetime
import subprocess
import xml.etree.ElementTree as ET
# This is the hostname of the server running this page   
HOST_NAME='localhost'
# This is the hostname of the other server which have that directory #HOST_NAME_TARGET=sys.argv[1] 
ssl_flag=sys.argv[1]
PORT_NUMBER=7036
ebsRoot={}
dictSOAPath={}
BPELProcesses=[]
BPELExt={}
dictDirServer={'/odaiso':'ucolhp2a','/tdaifo':'ucolhp2a','/ddaido':'ucolhp2b','/ddaico':'ucolhp1p','/xdaiso':'ucolhp1o','/xdaiio':'ucolhp1o','/xdaipo':'ucolhp1o','/tdaido':'/ucolhp1o'}

try:
  from cStringIO import StringIO
except ImportError:
  from StringIO import StringIO


class SimpleHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

  """Simple HTTP request handler with GET/HEAD/POST commands.

  This serves files from the current directory and any of its
  subdirectories.  The MIME type for files is determined by
  calling the .guess_type() method. And can reveive file uploaded
  by client.

  The GET/HEAD/POST requests are identical except that the HEAD
  request omits the actual contents of the file.

  """

  server_version = "SimpleHTTPWithUpload/" + __version__

  def do_GET(self):
      """Serve a GET request."""
      print 'serve get request'
      f = self.send_head()
      if f:
          self.copyfile(f, self.wfile)
          f.close()

  def do_HEAD(self):
      """Serve a HEAD request."""
      f = self.send_head()
      if f:
          f.close()

  def do_POST(self):
      global ssl_flag
      #global issued_to
      """Serve a POST request."""
      print 'serve post request'
      #if ssl_flag=='ssl':
      #   cert=  self.connection.getpeercert()
      #   subject = dict(x[0] for x in cert['subject'])
      #   issued_to = subject['commonName']

      self.initialize_list_dict()

      r, info = self.deal_post_data()
      print r, info, "by: ", self.client_address
      f = StringIO()
      f.write('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">')
      f.write("<html>\n<title>Upload Result Page</title>\n")
      f.write("<body>\n<h2>Upload Result Page</h2>\n")
      f.write("<hr>\n")
      if r:
          f.write("<strong>Success:</strong>")
      else:
          f.write("<strong>Failed:</strong>")
      f.write(info)
      ####f.write("<br><a href=\"%s\">back</a>" % self.headers['referer'])
      f.write("<hr><small>Powerd By: DAI")
      ####f.write("<a href=\"Caution-http://li2z.cn/?s=SimpleHTTPServerWithUpload < Caution-http://li2z.cn/?s=SimpleHTTPServerWithUpload > \">")
      f.write("here</a>.</small></body>\n</html>\n")
      length = f.tell()
      f.seek(0)
      self.send_response(200)
      self.send_header("Content-type", "text/html")
      self.send_header("Content-Length", str(length))
      self.end_headers()
      if f:
          self.copyfile(f, self.wfile)
          f.close()

  def deal_post_data(self):
      global ebsRoot
      global dictSOAPath
      global BPELProcesses
      global BPELExt
      fh = open("./uploadFileHistory.log","a")
      boundary = self.headers.plisttext.split("=")[1]
      remainbytes = int(self.headers['content-length'])
      line = self.rfile.readline()
      remainbytes -= len(line)
      if not boundary in line:
          return (False, "Content NOT begin with boundary")
      line = self.rfile.readline()
      remainbytes -= len(line)
      userName=re.findall(r'user+\w+',line)
      if not userName:
         return(False, "Can't find username...")
      line = self.rfile.readline()
      remainbytes -= len(line)
      line = self.rfile.readline()
      remainbytes -= len(line)
      issued_to = line.rstrip()

      line = self.rfile.readline()
      remainbytes -= len(line)
      line = self.rfile.readline()
      remainbytes -= len(line)
      ebsInstanceName=re.findall(r'ebs+\w+',line)
      if not ebsInstanceName:
         return(False, "Can't find ebs istance name...")

      line = self.rfile.readline()
      remainbytes -= len(line)
      line = self.rfile.readline()
      remainbytes -= len(line)
      ebs = line.rstrip()

      line = self.rfile.readline()
      remainbytes -= len(line)
      line = self.rfile.readline()
      remainbytes -= len(line)

      iName=re.findall(r'inter+\w+',line)
      if not iName:
         return(False, "Can't find interface name...")

      line = self.rfile.readline()
      remainbytes -= len(line)
      line = self.rfile.readline()
      remainbytes -= len(line)
      bpelProcessId = line.rstrip()

      line = self.rfile.readline()
      remainbytes -= len(line)
      line = self.rfile.readline()
      remainbytes -= len(line)
      fn = re.findall(r'Content-Disposition.*name="file"; filename="(.*)"', line)
      ofileName=fn
      if not fn:
          return (False, "Can't find out file name...")
      #### find the correct path based on filname 

      lastIndex = fn[0].rfind("\\")
      fn[0]= fn[0][lastIndex+1:]
      fileSegment=fn[0].split("_")
      try:
         relativePath="/"+dictSOAPath[bpelProcessId][0].rstrip()
         ##print 'key : ' + fileSegment[0] + '_' + fileSegment[3]
      except KeyError:
         ##try:
             ## for PRDS 
             ##if 'ORDERACPT' in fn[0]:
             ##    relativePath='/PRDS/ACPT'
             ##else:
             ##    if 'IN_PRDS' in fn[0]:
             ##       if 'ACK' in fn[0]:
             ##          relatviePath='/PRDS/ORDERACPTACK'
             ##       else:
             ##          relativePath='/PRDS/ORDER'
             ##    raise Exception("Can't locate inbound directory")
             ##                               
         #except:
            ##pass
         return (False,"Can't locate inbound directory for this file " + fn[0] + ". Please check if the file name is conformed to the DAI interface standard")

      ## check file extension 
      if fn[0][fn[0].rfind(".")+1:] not in BPELExt[bpelProcessId]:
         return (False,"Invalid file extension. File has to have following extension " + str(BPELExt[bpelProcessId]))
      absolutePath=ebsRoot[ebs]+'/infgex/dai_inbound/DS_'+ebs+relativePath
      path = self.translate_path(self.path)
      ##print path
      ##fn = os.path.join(path, fn[0])
      fn = os.path.join(absolutePath, fn[0]+'.1')
      line = self.rfile.readline()
      remainbytes -= len(line)
      line = self.rfile.readline()
      remainbytes -= len(line)
      try:
          if os.path.isdir(ebsRoot[ebs]):
             out = open(fn, 'wb')
      except IOError:
          return (False, "Can't create file to write, do you have permission to write?")

      preline = self.rfile.readline()
      remainbytes -= len(preline)
      fileValue=''
      while remainbytes > 0:
          line = self.rfile.readline()
          remainbytes -= len(line)
          if boundary in line:
              preline = preline[0:-1]
              if preline.endswith('\r'):
                 preline = preline[0:-1]
              fileValue=fileValue+preline
              # check if it is xml document
              if ofileName[0][ofileName[0].rfind(".")+1:] == 'xml':
                 try:
                   xm=ET.fromstring(fileValue)
                 except Exception as e:
                   out.close()
                   os.remove(out.name)
                   return(False,"This XML file is invalid  - " + str(e))
              if os.path.isdir(ebsRoot[ebs]):
                 ##out.write(preline)
                 out.write(fileValue)
                 out.close()
                 print >>fh ,  str(datetime.datetime.now()) + " " + str(fn) +  " uploaded successfully  by " + issued_to
                 return (True, "File '%s' upload success!" % fn)
              ##print fileValue 
              ## forward to other server for other directory
              if not os.path.isdir(ebsRoot[ebs]):
                 print 'post to ' + dictDirServer[ebsRoot[ebs]] + ".oob.disa.mil:" + str(PORT_NUMBER)
                 #(resultStatus,resultReason,resultDetail)=postMultiPart.post_multipart(HOST_NAME_TARGET+":"+str(PORT_NUMBER),"/",[('username',issued_to),('ebsInstance',ebs),('interface',bpelProcessId)],[('file',ofileName[0],fileValue)])
                 (resultStatus,resultReason,resultDetail)=postMultiPart.post_multipart(dictDirServer[ebsRoot[ebs]]+".oob.disa.mil:"+str(PORT_NUMBER),"/",[('username',issued_to),('ebsInstance',ebs),('interface',bpelProcessId)],[('file',ofileName[0],fileValue)])
                 if str(resultStatus)=='200':
                    print >>fh ,  str(datetime.datetime.now()) + " " + str(fn) +  " uploaded successfully  by " + issued_to
                    return (True, "File '%s' upload success!" % fn)
                 else:
                    return (False,resultDetail)

          else:
              ##if os.path.isdir(ebsRoot[ebs]):
              ##   out.write(preline)
              fileValue=fileValue+preline
              preline = line
      return (False, "Unexpect Ends of data.")

  def send_head(self):
      """Common code for GET and HEAD commands.

      This sends the response code and MIME headers.

      Return value is either a file object (which has to be copied
      to the outputfile by the caller unless the command was HEAD,
      and must be closed by the caller under all circumstances), or
      None, in which case the caller has nothing further to do.

      """
      global ssl_flag

      issued_to = 'UNKNOWN'
      if ssl_flag=='ssl':
         cert=  self.connection.getpeercert()
         ##subject = dict(x[0] for x in cert['subject'])
         ##issued_to = subject['commonName']
         subject = dict(cert['subjectAltName'])
         issued_to = subject['email']

      if self.path == '/uploadhistory':
         self.path='/uploadFileHistory.log'

      path = self.translate_path(self.path)
      f = None
      if os.path.isdir(path):
          if not self.path.endswith('/'):
              # redirect browser - doing basically what apache does
              self.send_response(301)
              self.send_header("Location", self.path + "/")
              self.end_headers()
              return None
          for index in "index.html", "index.htm":
              index = os.path.join(path, index)
              if os.path.exists(index):
                  path = index
                  break
          else:
              return self.upload_page(path,issued_to)
      ctype = self.guess_type(path)
      try:
          # Always read in binary mode. Opening files in text mode may cause
          # newline translations, making the actual size of the content
          # transmitted *less* than the content-length!
          f = open(path, 'rb')
      except IOError:
          self.send_error(404, "File not found")
          return None
      self.send_response(200)
      self.send_header("Content-type", ctype)
      fs = os.fstat(f.fileno())
      self.send_header("Content-Length", str(fs[6]))
      self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
      self.end_headers()
      return f

  def initialize_list_dict(self):

      global BPELProcesses
      global dictSOAPath
      global ebsRoot
      global BPELExt
      BPELProcesses=[]
      dictSOAPath={}
      ebsRoot={}
      BPELExt={}
      try:
         with open("./BPELProcess.properties") as bp:
          for line in bp:
              bitem = line.split(",")
              BPELProcesses.append((bitem[0],bitem[1]))
              dictSOAPath[bitem[0]]=[bitem[2]]
              BPELExt[bitem[0]]=bitem[3]
      except:
          self.send_error(500, "Error in reading BPELProcess.properties")
          return None
      try:
          with open("./soaconnection.properties") as sp:
           for line in sp:
               sitem = line.split(",")
               ebsRoot[sitem[0]]=sitem[1].rstrip()
      except:
          self.send_error(500, "Error in reading soaconnection.properties")
          return None
      return 'Success'

  def upload_page(self, path,issued_to):
      """Helper to produce a directory listing (absent index.html).

      Return value is either a file object, or None (indicating an
      error).  In either case, the headers are sent, making the
      interface the same as for send_head().

      """
      global BPELProcesses
      global dictSOAPath
      global ebsRoot

      #try:
      #    list = os.listdir(path)
      #except os.error:
      #    self.send_error(404, "No permission to list directory")
      #    return None

      #list.sort(key=lambda a: a.lower())
      try:
          soaReport=open("./SOAEBSStatus.html")
          soaContent=soaReport.read()
      except:
          soaContent=''
      r1 = self.initialize_list_dict()
      if r1 is None:
         return None

      f = StringIO()
      displaypath = cgi.escape(urllib.unquote(self.path))
      f.write('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">')
      f.write("<html>\n<title>Upload file to DAI </title>\n")
      f.write("<style>p.ex1 {font: italic bold 15px/30px Georgia, serif;} table {font-size: 70%; font-family: \"Myriad Web\", Verdana, Helvetica,Arial,sans-serif; border-collapse: collapse;} table, th, td {border:1px solid black;}</style>\n")
      f.write("<body>\n<h2>Upload file to DAI</h2>\n")
      f.write("<hr>\n")
      f.write("<form ENCTYPE=\"multipart/form-data\" method=\"post\">")
      f.write("<input type=\"hidden\" name=\"username\" value=\""+issued_to+"\"/>")
      f.write("<select name=\"ebsInstance\">")
      for key in sorted(ebsRoot):
          f.write("<option value=\""+key+"\">"+key+"</option>")
      f.write("</select>\n")        
      f.write("<select name=\"interface\">")
      for (bpelName,interfaceName) in sorted(BPELProcesses,key=lambda x:x[1]):
          f.write("<option value=\""+bpelName+"\">"+interfaceName+"</option>")
      f.write("</select>\n")        
      f.write("<input name=\"file\" type=\"file\"/>")
      f.write("<input type=\"submit\" value=\"upload\"/></form>\n")
      f.write("<hr>\n")
      f.write(soaContent[soaContent.find('<p'):soaContent.rfind('p>')+2])
      f.write("<hr>\n")
      #f.write("<hr>\n<ul>\n")
      #for name in list:
      #    fullname = os.path.join(path, name)
      #    displayname = linkname = name
      #    # Append / for directories or @ for symbolic links
      #    if os.path.isdir(fullname):
      #        displayname = name + "/"
      #        linkname = name + "/"
      #    if os.path.islink(fullname):
      #        displayname = name + "@"
              # Note: a link to a directory displays with @ and links with /
      #    f.write('<li><a href="%s">%s</a>\n'
      #            % (urllib.quote(linkname), cgi.escape(displayname)))
      #f.write("</ul>\n<hr>\n</body>\n</html>\n")
      f.write("</body>\n</html>\n")
      length = f.tell()
      f.seek(0)
      self.send_response(200)
      self.send_header("Content-type", "text/html")
      self.send_header("Content-Length", str(length))
      self.end_headers()
      return f

  def translate_path(self, path):
      """Translate a /-separated PATH to the local filename syntax.

      Components that mean special things to the local file system
      (e.g. drive or directory names) are ignored.  (XXX They should
      probably be diagnosed.)

      """
      # abandon query parameters
      path = path.split('?',1)[0]
      path = path.split('#',1)[0]
      path = posixpath.normpath(urllib.unquote(path))
      words = path.split('/')
      words = filter(None, words)
      path = os.getcwd()
      for word in words:
          drive, word = os.path.splitdrive(word)
          head, word = os.path.split(word)
          if word in (os.curdir, os.pardir): continue
          path = os.path.join(path, word)
      return path

  def copyfile(self, source, outputfile):
      """Copy all data between two file objects.

      The SOURCE argument is a file object open for reading
      (or anything with a read() method) and the DESTINATION
      argument is a file object open for writing (or
      anything with a write() method).

      The only reason for overriding this would be to change
      the block size or perhaps to replace newlines by CRLF
      -- note however that this the default server uses this
      to copy binary data as well.

      """
      shutil.copyfileobj(source, outputfile)

  def guess_type(self, path):
      """Guess the type of a file.

      Argument is a PATH (a filename).

      Return value is a string of the form type/subtype,
      usable for a MIME Content-type header.

      The default implementation looks the file's extension
      up in the table self.extensions_map, using application/octet-stream
      as a default; however it would be permissible (if
      slow) to look inside the data to make a better guess.

      """

      base, ext = posixpath.splitext(path)
      if ext in self.extensions_map:
          return self.extensions_map[ext]
      ext = ext.lower()
      if ext in self.extensions_map:
          return self.extensions_map[ext]
      else:
          return self.extensions_map['']

  if not mimetypes.inited:
      mimetypes.init() # try to read system mime.types
  extensions_map = mimetypes.types_map.copy()
  extensions_map.update({
      '': 'application/octet-stream', # Default
      '.py': 'text/plain',
      '.c': 'text/plain',
      '.h': 'text/plain',
      '.log': 'text/plain',
      })


def test(HandlerClass = SimpleHTTPRequestHandler,
       ServerClass = BaseHTTPServer.HTTPServer):
  print "Test12333"
  BaseHTTPServer.test(HandlerClass, ServerClass)

if __name__ == '__main__':
  ##test()
  ServerClass=BaseHTTPServer.HTTPServer
  print HOST_NAME
  cwd=os.getcwd()
  print cwd
  
  httpd=ServerClass((HOST_NAME,PORT_NUMBER),SimpleHTTPRequestHandler)    
  if  ssl_flag=='ssl': 
      httpd.socket= ssl.wrap_socket(httpd.socket, certfile='./sslkey/server_unencrypted.pem',server_side=True,cert_reqs=ssl.CERT_REQUIRED, ca_certs='./sslkey/clientCA.pem')
  try:
      print 'starting ' + HOST_NAME +':' + str(PORT_NUMBER)
      httpd.serve_forever()
  except KeyboardInterrupt:
      pass
  httpd.server_close()
