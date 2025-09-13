import hashlib
url_mapping = {}
def shorten_url{long_url}:
   short_url_hash = hashlib.sha256(long_url.encode()).hexdigest()).hexdigest()[:6]
   short_url = f"https://short.url/{short_url_hash}"
   #store mapping in a dictionary
   url_mapping[short_url]=long_url
   return short_url
def main():
  #get user input
  long_url = input("input the long url to be shortened: ")
  #generate a shortened url
  short_url = shorten_url(long_url)
  #display shortened url
  print(f"Short URL : {short_url} ")

#run the url shortener program
main()
