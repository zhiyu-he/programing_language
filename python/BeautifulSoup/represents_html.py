# coding: utf-8


from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

html_doc_2 = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

if __name__ == '__main__':

    soup = BeautifulSoup(html_doc, 'html.parser')
    all_a_tag = soup.find_all('a')
    print "type of a: %s" % type(all_a_tag[0]) # <class 'bs4.element.Tag'>
    
    print soup.find(href="http://example.com/elsie")
    print soup.find(id="link2")
    
    # 对于bs4.element.Tag类型, 可以利用get获取其中的属性
    count = 0
    for a_tag in soup.find_all('a'):
        print "------------%s------------" % count
        print "href: %s" % a_tag.get('href')
        print "class: %s" % a_tag.get('class')
        print "id: %s" % a_tag.get('id')
        print "text: %s" % a_tag.text

        count += 1

    # Kinds of objects
    print "==============%s=============" % "Kinds Of Objects"
    soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
    tag = soup.b
    print "[Name] tag.name: %s" % tag.name
    tag.name = "abc"
    print "[Name] tag.name: %s" % tag.name
    
    print "[Attributes] %s" % tag['class']
    print "[Attributes] %s" % tag.attrs
    print "[Attributes] you can modify add, remove, del"


    soup = BeautifulSoup(html_doc_2, 'html.parser')
    
    # .contents and .children
    head_tag = soup.head
    print head_tag

    print "tag's children: %s" % head_tag.contents

    title_tag = head_tag.contents[0]
    print "title tag: %s" % title_tag

    print "title tag's children: %s" % title_tag.contents


    for child in title_tag.children:
         print(child)


    # .descendatns

    for child in head_tag.descendants:
         print(child)


    # .string


    # .parents
    print "===========.parents==========="
    links = soup.a
    for parent in links.parents:
        if parent is None:
             print(parent)
        else:
             print "parent detail: %s" % parent
             print(parent.name)
    
    
    # .next_sibling and ._sibling
    # todo 没看懂


