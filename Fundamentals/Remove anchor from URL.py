'''
Complete the function/method so that it returns the url with anything after the anchor (#) removed.
'''


def remove_url_anchor(url):
    return url.split('#')[0]


a = "www.codewars.com#about"
print(a.split('#')[0])